# https://docs.paramiko.org/en/2.4/api/client.html
import logging
import paramiko
import inspect

_log = logging.getLogger('Main.SshClient')


class SshClient:
    def __init__(self, hostname, username, password, port=22, timeout=5, **kwargs):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self._timeout = timeout
        self.kwargs = kwargs
        self._ssh_client = None
        self.log = _log

    def connect(self):
        if self._ssh_client is not None:
            return True
        try:
            self._ssh_client = paramiko.SSHClient()
            self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self._ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password,
                                     port=self.port, timeout=self._timeout, look_for_keys=False, **self.kwargs)
            self.log.info('Connection established')
        except Exception as g_exc:
            self.log.error(g_exc)
            raise
        return True

    def run_cmd(self, cmd, timeout=10):
        try:
            _stdin, _stdout, _stderr = self._ssh_client.exec_command(cmd, timeout=timeout)
            _stdin.channel.shutdown_write()
            std_out = _stdout.read()
            err_out = _stderr.read()
        except Exception as ssh_exc:
            self.log.exception(ssh_exc)
            raise
        return std_out, err_out

    def __getattr__(self, attr):
        if hasattr(self._ssh_client, attr):
            def wrapper(*args, **kwargs):
                result = getattr(self._ssh_client, attr)(*args, **kwargs)
                return result

            return wrapper
        raise AttributeError(attr)

    def __getattribute__(self, attr):
        if attr in super().__getattribute__('__dict__'):
            _log.debug(f'---> Wrapper instance {attr=}')
        elif attr in [el for el, _ in inspect.getmembers(SshClient, predicate=inspect.isfunction)]:
            _log.info(f'---> Wrapper class method {attr=}')
        else:
            _log.info(f'----> Low level call {attr=}')
        return super().__getattribute__(attr)

    def __setattr__(self, key, value):
        if key == '_timeout':
            if value % 5 != 0:
                value = (value // 5 + 1) * 5
        super().__setattr__(key, value)


if __name__ == '__main__':
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    _log.addHandler(console_handler)
    _log.setLevel(logging.INFO)

    ssh_client = SshClient(hostname='127.0.0.1', username='test', password='newconnection')
    ssh_client.connect()
    _log.info(ssh_client.run_cmd('uptime'))
    ssh_client._timeout = 7
    _log.info(f'Timeout: {ssh_client._timeout}')

    # non existing attributes
    _stdin, _stdout, _stderr = ssh_client.exec_command('uname -a')
    _stdin.channel.shutdown_write()
    std_out = _stdout.read()
    _log.info(std_out)

    # attribute error
    ssh_client.smth_else('123')
