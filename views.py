def player_json(player):
    return {
        "id": player.id,
        "first_name": player.first_name,
        "last_name": player.last_name,
        "last_modified": player.last_modified.isoformat(),
        "nationality": player.nationality.name,
        "current_club": player.current_club.name,
        "date_of_birth": str(player.date_of_birth),
    }


def country_json(country):
    return {
        "id": country.id,
        "name": country.name,
    }


def club_json(club):
    return {
        "id": club.id,
        "name": club.name,
    }
