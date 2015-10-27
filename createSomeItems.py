from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dbsetup import Categories, Items, Users

engine = create_engine('sqlite:///catalog.db')
DBsession = sessionmaker(bind = engine)
session = DBsession()

Nate = Users(name = "nate", email = "nathanscamera@gmail.com")

Comics = Categories(name = "comics", userID = Nate.id)
session.add(Comics)
session.commit()

Superman = Items(name = "Superman", description = "An issue of the last son of kyptonite.", categories_id = Comics.id)
Batman = Items(name = "Batman", description = "An issue of the caped crusader.",
	categories_id = Comics.id)

session.add(Superman)
session.add(Batman)
session.commit()

Skateboarding = Categories(name = "manga", userID = Nate.id)
session.add(Manga)
session.commit()

One_piece = Items(name = "One Piece", description = "A funny young man and his crew explores the ocean in search of the world's ultimate treasure.", categories_id = Manga.id)
Naruto = Items(name = "Naruto", description = "An adolescent ninja who constantly searches for recognition.", categories_id = Manga.id)
Bleach = Items(name = "Bleach", description = "The adventures of the hotheaded teenager who obtains the powers of a Soul Reaper", categories_id = Manga.id)

session.add(One_piece)
session.add(Naruto)
session.add(Bleach)
session.commit()

print "success!"
