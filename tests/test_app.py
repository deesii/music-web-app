from lib.database_connection import DatabaseConnection


'''
I want to see the list of albums once I just do a get
after calling GET / albums
'''

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get("/albums")


'''
When I add a new album, I will post it and it will return nothing, 
Then , when I retrieve the album list via the GET request, I will see the newly added album,
alongside the album that was already there.

'''

def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql") #seed the database! 
    post_response = web_client.post('/albums', data = {'title': "Voyage", 'release_year': "2022", 'artist_id' : "2"}) #add this please! Using the create
    get_response = web_client.get('/albums') #now retrieve the information from the database
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Album(1, Doolittle, 1989, 1)\n"\
        "Album(2, Voyage, 2022, 2)"
    

'''
For the case that there is an invalid input :

# POST /albums
#  Parameters (body):
        # 
        # release_year=2022 (integer)
        # artist_id=2 (integer)
#  Expected response (400 Bad Request), "One of the inputs is not filled in!"

'''

def test_post_submit_error_data(web_client):
    response = web_client.post('/albums', data = {'release_year': "2022", 'artist_id' : "2"})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'One of the inputs is not filled in!'

