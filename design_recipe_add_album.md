
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

# Request:
POST /albums

# With body parameters:
title=Voyage (string)
release_year=2022 (integer)
artist_id=2 (integer)

# Expected response (200 OK)
(No content)

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

"""
No message --> 200

"""
# POST /albums
# Parameters:
    # With body parameters:
        # title=Voyage (string)
        # release_year=2022 (integer)
        # artist_id=2 (integer)

# Expected response (200 OK)

'''
One of the inputs is not filled in --> 400
'''


# POST /albums
#  Parameters (body):
        # 
        # release_year=2022 (integer)
        # artist_id=2 (integer)
#  Expected response (400 Bad Request), "One of the inputs is not filled in!"



'''
The input structure of the release year is not an integer --> 400

'''

# POST /albums
#  Parameters (body):
        # title=Voyage (string)
        # release_year=blobby (integer)
        # artist_id=2 (integer)
#  Expected response (400), "An intetger is required for the release year!"



'''
The input structure of the artist_id is not an integer --> 400

'''

# POST /albums
#  Parameters (body):
        # title=Voyage (string)
        # release_year=2023 (integer)
        # artist_id=blob (integer)
#  Expected response (400 Bad Request), "An intetger is required for the artist id!"


'''
The artist_id doesnt exist! --> 400
'''

# POST /albums
#  Parameters (body):
        # title=Voyage (string)
        # release_year=2023 (integer)
        # artist_id=8 (integer)
#  Expected response (400 Bad Request), "That artist_id doesnt exist!"


```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
# POST /albums
# Parameters:
    # With body parameters:
        # title=Voyage (string)
        # release_year=2022 (integer)
        # artist_id=2 (integer)

# Expected response (200 OK)
"""
def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql") #seed the database! 
    response = web_client.post('/albums', data = {'title': "Vogage", 'release_year': "2022", 'artist_id' : "2"})
    response_get = web_client.get('/albums')
    assert response.status_code == 200
    assert response_get.status_code == 200
    assert reponse_get.data.decode("utf-8") == Albums(....)



"""
# POST /albums
#  Parameters (body):
        # 
        # release_year=2022 (integer)
        # artist_id=2 (integer)
#  Expected response (400 Bad Request), "One of the inputs is not filled in!"

"""
def test_post_submit(web_client):
    response = web_client.post('/albums', data={"release_year": 2022 "artist_id" : 2})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'One of the inputs is not filled in!'





```

