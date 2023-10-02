# https://en.wikipedia.org/wiki/Transport_Layer_Security#SSL_1.0,_2.0,_and_3.0
"""Module provides basic REST operations for SSL connections."""

import logging
import ssl

import requests
import urllib3
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # disable warning

_log = logging.getLogger('HttpsWrapper')


def session_init(func):
    """
    Decorate functions to do session init before certain call.

    :param func: target function
    :return: function call
    """

    def wrapper(self, *args, **kwargs):
        if self._session is None:
            _log.debug('[RestClient] Session init...')
            self.initialize()
        return func(self, *args, **kwargs)

    return wrapper

class RestError(Exception):
    pass

class RestStatusError(Exception):
    pass


class SSLAdapter(HTTPAdapter):
    """HTTPS Transport Adapter that uses an arbitrary SSL version."""

    def __init__(self, ssl_version=ssl.PROTOCOL_TLS_CLIENT, **kwargs):
        """
        Init.

        :param ssl_version: ssl version that should be used by transport. Default ssl.PROTOCOL_TLS_CLIENT
        :param kwargs: additional transport parameters
        """
        self.ssl_version = ssl_version
        super(SSLAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
        """Parent class call overwrite."""
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=self.ssl_version)


class RestClient:
    """Provides interface to low level rest operations."""

    ALLOWED_METHODS = ('get', 'post', 'put', 'delete', 'head', 'patch')

    def __init__(self, url, ssl_version=ssl.PROTOCOL_TLS_CLIENT, **kwargs):
        """
        Init.

        :param url: rest api base url ex: https://127.0.0.1:443
        :param ssl_version: ssl version that should be used by transport. Default ssl.PROTOCOL_TLS_CLIENT
        :param kwargs: Optional additional rest client parameters. For example here can be stored credentials for login
        """
        self.url = url
        self.ssl_version = ssl_version
        self.kwargs = kwargs
        self._request_kwargs = kwargs.get('request_kwargs', {})
        self._session = None

    def initialize(self):
        """Create new requests session according url prefix https/http."""
        session = requests.Session()
        if self.url.lower().startswith('https'):
            ssl_adapter = SSLAdapter(ssl_version=self.ssl_version)
            session.verify = False
            session.mount(self.url, ssl_adapter)
        self._session = session

    @property
    def request_kwargs(self):
        """Get request kwargs."""
        return self._request_kwargs

    @request_kwargs.setter
    def request_kwargs(self, kwargs):
        """Set request kwargs."""
        self._request_kwargs = kwargs

    @property
    def cookies(self):
        """Get session cookies."""
        return self._session.cookies

    @cookies.setter
    def cookies(self, cookies):
        """Set session cookies."""
        self._session.cookies = cookies

    @property
    def headers(self):
        """Get session headers."""
        return self._session.headers

    @headers.setter
    def headers(self, headers):
        """Update session headers."""
        self._session.headers.update(headers)

    def clear_cookies(self):
        """Clear session cookies."""
        if self._session:
            self._session.cookies.clear()

    def _do_request(self, method_name, endpoint, **kwargs):
        """
        Dispatcher for rest calls.

        :param method_name: method name ex:'post', 'GET' etc
        :param endpoint: endpoint path after base url
        :param kwargs: rest call parameters
        :return: :py:meth:`~requests.Response` object
        :raises: :py:meth:`~RestError` in case of connection issue
        :raises: :py:meth:`~RestStatusError` in case raise_for_status kwarg defined and response has error status code
        """
        try:
            if not (method_name in self.ALLOWED_METHODS):
                raise RuntimeError(f'Not allowed method name "{method_name}"')
            if self._session is None:
                _log.warning('REST session not initialized. Initialization...')
                self.initialize()
            req_kwargs = {**self._request_kwargs, **kwargs}

            # separate rest client and rest call (used by requests) parameters
            raise_for_status = req_kwargs.pop('raise_for_status', True)
            clear_cookie = req_kwargs.pop('clear_cookie', False)

            response = getattr(self._session, method_name.lower())(self.url + endpoint, **req_kwargs)
            if clear_cookie:
                self.clear_cookies()
            if raise_for_status:
                response.raise_for_status()
            return response
        except requests.HTTPError as http_err:
            _log.error('[{0}] "{1}"'.format(http_err.response.status_code, http_err.response.text))
            raise RestStatusError(http_err.response, http_err.request)
        except requests.exceptions.Timeout:
            raise RestError('Timeout')
        except requests.exceptions.TooManyRedirects:
            raise RestError('URL is bad. Too many redirects')
        except requests.exceptions.RequestException as rest_exc:
            _log.error(rest_exc)
            raise RestError('Request failed: {0:}'.format(rest_exc))

    @session_init
    def post(self, endpoint_name, **kwargs):
        """
        Post request.

        :param endpoint_name: endpoint path after base url
        :param kwargs: For possible values see self._do_request call and L{requests.post} api
        :return: :py:meth:`~requests.Response` object
        :raises: :py:meth:`~RestError` in case of connection issue
        :raises: :py:meth:`~RestStatusError` in case raise_for_status param defined and response has error status code
        """
        return self._do_request('post', endpoint=endpoint_name, **kwargs)

    @session_init
    def get(self, endpoint_name, **kwargs):
        """
        Get request.

        :param endpoint_name: endpoint path after base url
        :param kwargs: For possible values see self._do_request call and L{requests.get} api
        :return: :py:meth:`~requests.Response` object
        :raises: :py:meth:`~RestError` in case of connection issue
        :raises: :py:meth:`~RestStatusError` in case raise_for_status param defined and response has error status code
        """
        return self._do_request('get', endpoint=endpoint_name, **kwargs)

    @session_init
    def head(self, endpoint_name, **kwargs):
        """
        Head request.

        :param endpoint_name: endpoint path after base url
        :param kwargs: For possible values see self._do_request call and L{requests.head} api
        :return: :py:meth:`~requests.Response` object
        :raises: :py:meth:`~RestError` in case of connection issue
        :raises: :py:meth:`~RestStatusError` in case raise_for_status param defined and response has error status code
        """
        return self._do_request('head', endpoint=endpoint_name, **kwargs)

    @session_init
    def put(self, endpoint_name, **kwargs):
        """
        Put request.

        :param endpoint_name: endpoint path after base url
        :param kwargs: For possible values see self._do_request call and L{requests.put} api
        :return: :py:meth:`~requests.Response` object
        :raises: :py:meth:`~RestError` in case of connection issue
        :raises: :py:meth:`~RestStatusError` in case raise_for_status param defined and response has error status code
        """
        return self._do_request('put', endpoint=endpoint_name, **kwargs)

    @session_init
    def patch(self, endpoint_name, **kwargs):
        """
        Patch request.

        :param endpoint_name: endpoint path after base url
        :param kwargs: For possible values see self._do_request call and L{requests.patch} api
        :return: :py:meth:`~requests.Response` object
        :raises: :py:meth:`~RestError` in case of connection issue
        :raises: :py:meth:`~RestStatusError` in case raise_for_status param defined and response has error status code
        """
        return self._do_request('patch', endpoint=endpoint_name, **kwargs)

    @session_init
    def delete(self, endpoint_name, **kwargs):
        """
        Delete request.

        :param endpoint_name: endpoint path after base url
        :param kwargs: For possible values see self._do_request call and L{requests.delete} api
        :return: :py:meth:`~requests.Response` object
        :raises: :py:meth:`~RestError` in case of connection issue
        :raises: :py:meth:`~RestStatusError` in case raise_for_status param defined and response has error status code
        """
        return self._do_request('delete', endpoint=endpoint_name, **kwargs)


if __name__ == '__main__':
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    _log.addHandler(console_handler)
    _log.setLevel(logging.DEBUG)

    # online resource to check full list of rest methods
    device_url = 'https://jsonplaceholder.typicode.com'
    rc = RestClient(device_url)
    rc.request_kwargs = {'raise_for_status': False, 'clear_cookie': True, 'headers': {'X-Request': 'test'}}
    resp = rc.post('/posts', data={'userId': 10, 'id': 101, '"title': '123'})
    _log.info(' === Post request results ===')
    _log.info(resp.status_code)
    _log.info(resp.json())

    resp = rc.get('/posts/1')
    _log.info('=== Get request results ===')
    _log.info(resp.status_code)
    _log.info(resp.json())

    resp = rc.head('/posts/1')
    _log.info('=== Head request results ===')
    _log.info(resp.status_code)

    resp = rc.put('/posts/1', data={'userId': 10, 'id': 101, '"title': '123'})
    _log.info(' === Put request results ===')
    _log.info(resp.status_code)
    _log.info(resp.json())
    #
    # resp = rc.delete('/posts/1', data={'userId': 10, 'id': 101, '"title': '123'})
    # _log.info(' === Delete request results ===')
    # _log.info(resp.status_code)
    # _log.info(resp.json())
    #
    # resp = rc.patch('/posts/1', data={'userId': 10, 'id': 101, '"title': '123'})
    # _log.info(' === Patch request results ===')
    # _log.info(resp.status_code)
    # _log.info(resp.json())
