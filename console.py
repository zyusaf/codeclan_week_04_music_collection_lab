import pdb

from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Prince")
artist_repository.save(artist1)
# artist2 = Artist("Marvin Gaye")
# artist_repository.save(artist2)

artist_repository.select_all()

album1 = Album("Purple Rain", "Funk", artist1)
album_repository.save(album1)
# album2 = Album("What's Going On", "Soul", artist2)
# album_repository.save(album2)

pdb.set_trace()