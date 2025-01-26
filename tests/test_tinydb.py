import pytest
from tinydb import TinyDB, Query


DB_STORAGE = 'db.json'


@pytest.fixture
def db():
    db = TinyDB(DB_STORAGE)
    yield db
    db.close()

@pytest.mark.tinydb
def test_create_db(db):
    assert db is not None

@pytest.mark.tinydb
def test_insert_user_or_update(db):
    user = {'name': 'John', 'age': 30}
    # check if user exists, if not insert, else update
    User = Query()
    result = db.table('users').search(User.name == 'John')
    if result:
        db.table('users').update(user, User.name == 'John')
    else:
        db.table('users').insert(user)
    # check if user is inserted
    result = db.table('users').search(User.name == 'John')
    assert len(result) == 1
    assert result[0]['name'] == 'John'


@pytest.mark.tinydb
def test_query_user(db):
    # user = {'name': 'John', 'age': 30}
    # db.table('users').insert(user)
    User = Query()
    result = db.table('users').search(User.name == 'John')
    assert len(result) >= 1
    assert result[0]['name'] == 'John'
    assert result[0]['age'] == 30

@pytest.mark.tinydb
def test_query_all_users(db):
    users = [
        {'name': 'Janet', 'age': 46},
        {'name': 'Jane', 'age': 25},
        {'name': 'Doe', 'age': 22}
    ]
    db.table('users').insert_multiple(users)
    result = db.table('users').all()
    assert len(result) >= 3
    # check for Janet, Jane, and Doe in the result
    assert any(user['name'] == 'Janet' for user in result)
    assert any(user['name'] == 'Jane' for user in result)
    assert any(user['name'] == 'Doe' for user in result)

@pytest.mark.tinydb
def test_remove_user(db):
    User = Query()
    db.table('users').remove(User.name == 'Jane')
    result = db.table('users').search(User.name == 'Jane')
    assert len(result) == 0


@pytest.mark.tinydb
def test_insert_order(db):
    order = {'item': 'book', 'quantity': 2}
    db.table('orders').insert(order)
    assert len(db.table('orders')) >= 1
