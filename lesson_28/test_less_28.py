import pytest

class DBConnection():
    count = 0

    def __init__(self) -> None:
        self.__class__.count = self.count + 1
        self.connection = "You connect to Pentagon DB"

    def __repr__(self) -> str:
        return f"{self.connection}: {self.count} time(s)"


@pytest.fixture(scope="module") # autouse=True  # scope="function"
def connect_to_database():
    connection = DBConnection()
    return connection


def test_connection(connect_to_database):
    assert isinstance(connect_to_database, DBConnection)
    pass
    assert connect_to_database.connection == "You connect to Pentagon DB"


def test_connection_2(connect_to_database):
    assert isinstance(connect_to_database, DBConnection)
    pass
    assert connect_to_database.connection == "You connect to Pentagon DB"
    assert connect_to_database.count == 1