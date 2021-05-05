import datetime
from flask import request, jsonify
from init import create_app
from models import Player, Country, Club, db
from views import player_json, club_json, country_json

app = create_app()


@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    all_players = []
    for player in players:
        all_players.append(player_json(player))
    return jsonify(all_players), 200


@app.route('/players', methods=['POST'])
def create_player():
    data = request.get_json()

    player = Player(
        first_name=data['first_name'],
        last_name=data['last_name'],
        date_of_birth=data['date_of_birth'],
        nationality_id=data['nationality_id'],
        current_club_id=data['current_club_id'],
        preferred_position=data['preferred_position'],
    )
    db.session.add(player)

    db.session.commit()
    return jsonify(data), 201


@app.route('/player/<id>', methods=['GET'])
def get_by_id(id):
    player = Player.query.get_or_404(id)
    return jsonify(player_json(player)), 200


@app.route('/player/<id>', methods=['PUT'])
def edit_player(id):
    data = request.get_json()
    player = Player.query.get_or_404(id)

    player.first_name = data['first_name'],
    player.last_name = data['last_name'],
    player.date_of_birth = data['date_of_birth'],
    player.nationality_id = data['nationality_id'],
    player.current_club_id = data['current_club_id'],
    player.preferred_position = data['preferred_position'],
    player.last_modified = datetime.datetime.utcnow()
    db.session.add(player)

    db.session.commit()
    return jsonify({'message': 'updated'}), 200


@app.route('/player/<id>', methods=['DELETE'])
def delete_player(id):
    Player.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'message': 'deleted'}), 204


@app.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    all_countries = []
    for country in countries:
        all_countries.append(country_json(country))
    return jsonify(all_countries), 200


@app.route('/clubs', methods=['GET'])
def get_clubs():
    clubs = Club.query.all()
    all_clubs = []
    for club in clubs:
        all_clubs.append(club_json(club))
    return jsonify(all_clubs), 200
