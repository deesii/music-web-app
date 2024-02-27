
import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album


app = Flask(__name__)


@app.route('/albums', methods = ["POST"])
def post_albums():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return 'One of the inputs is not filled in!', 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    album = Album(None,                             #from the inputs, put this into a variable containing these details
                request.form['title'],
                request.form['release_year'],
                request.form['artist_id']
                   )
    repository.create(album) #now create this album in the repository with those details
    return '', 200
    



@app.get('/albums')
def get_albums():
    connection = get_flask_database_connection(app) #opening a connection between the web server (flask) and the database
    repository = AlbumRepository(connection) # using the open connection to run a instanciate a repository
    albums = repository.all()
    return "\n".join(
        f"{album}" for album in albums 
    )

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))