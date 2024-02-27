import pytest
from lib.database_connection import DatabaseConnection
from app import app

# This is a Pytest fixture.
# It creates an object that we can use in our tests.
# We will use it to create a database connection.
@pytest.fixture
def db_connection():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn

# We'll also create a fixture for the client we'll use to make test requests.
@pytest.fixture
def web_client():
    app.config['TESTING'] = True # This gets us better errors
    with app.test_client() as client:
        yield client

# Now, when we create a test, if we allow it to accept a parameter called
# `db_connection` or `web_client`, Pytest will automatically pass in the objects
# we created above.

# For example:

# def test_something(db_connection, web_client):
#     # db_connection is now available to us in this test.
#     # web_client is now available to us in this test

# is db_connection an instance of the class DataConnection() ---> yes
# is web_client an object (instance of  the class?? , and if so what class??)
        
'''The function web_client() is designed
to create a test client for a Flask application. This is particularly 
useful for testing Flask applications without needing to run the server. 
Here's a breakdown of what each line does:

app is an instance of a Flask object ; in -built method config applied of the 
"testing" case, 
and set to true: when it does that, it allows you to run a series of tests
without being connected to the server ... 

When passed through as an argument, web_client can be considered an object, 
specifically an instance of a class or a result of a function call. 

In the context of the web_client function you provided earlier, when it's 
used as a fixture in pytest, it yields a test client object from the Flask 
application. This object is an instance of the FlaskClient class, which is 
part of the Flask framework. It allows you to simulate HTTP requests to your 
Flask application without needing to run the server, making it ideal for 
testing purposes.

The web_client fixture, when used in a test, would be an instance of FlaskClient 
that is passed as an argument to the test function. This instance provides methods 
to make requests to your Flask application, such as get(), post(), put(), etc., 
and then assert the responses to ensure your application behaves as expected under 
different conditions.

web_client --> returns an object of the FlaskClient class --> 
---> allows testing of Flask application (sending http requests) without a server
---> the object has methods .get(), .post(), ... 

'''
