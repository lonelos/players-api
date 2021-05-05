from app import db
from models import Club, Country, Player

db.create_all()

db.session.add(Country(name='Croatia'))
db.session.add(Country(name='France'))
db.session.add(Club(name='Dinamo Zagreb'))
db.session.add(Club(name='Lyon'))
db.session.add(Player(
    first_name='Melvin', last_name='Bard', preferred_position='LB',
    current_club_id=2, nationality_id=2, date_of_birth='2000-06-11',
))
db.session.add(Player(
    first_name='Malo', last_name='Gusto', preferred_position='LB',
    current_club_id=2, nationality_id=2, date_of_birth='2003-05-19',
))
db.session.add(Player(
    first_name='Lovro', last_name='Majer', preferred_position='MF',
    current_club_id=1, nationality_id=1, date_of_birth='1998-06-30',
))

db.session.commit()
