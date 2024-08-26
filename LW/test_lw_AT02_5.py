import pytest
from lw_AT02_5 import init_db, add_user, get_user


@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()


def test_add_and_get_user(db_conn):
    add_user(db_conn, 'Алексндр', 30)
    user = get_user(db_conn, 'Алексндр')
    assert user == (1, 'Алексндр', 30)
