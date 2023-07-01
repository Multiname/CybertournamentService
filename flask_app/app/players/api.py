from . import players
from ..models import Player, Lineup, Tournament, db

# JSON: {
#     nickname,
#     login,
#     password
# }
@players.route('/register/', methods=['POST'])
def register():
    return 'players.register: ok / login exists'

# JSON: {
#     login,
#     password
# }
@players.route('/login/', methods=['PUT'])
def login():
    return 'players.login: player.id, player.nickname, player.points / wrong data'

@players.route('/get_player/<int:id>', methods=['GET'])
def get_player(id):
    return 'players.get_player: player.nickname, player.points / wrong data'

@players.route('/get_players_by_lineup/<int:id>', methods=['GET'])
def get_players_by_lineup(id):
    return 'players.get_players_by_lineup: [ player.id ] / wrong data'

@players.route('/get_players/', methods=['GET'])
def get_players():
    return 'players.get_players: [ player.id ] / wrong data'

# JSON: {
#     name,
#     owner_id,
#     tournament_id
# }
@players.route('/add_lineup/', methods=['POST'])
def add_lineup():
    return 'players.add_lineup: ok / wrong data'

@players.route('/get_lineup/<int:id>', methods=['GET'])
def get_lineup(id):
    return 'players.get_lineup: lineup.name, lineup.place, lineup.is_active, lineup.owner_id, lineup.tournament_id / wrong data'

@players.route('/get_lineups_by_owner/<int:id>', methods=['GET'])
def get_lineups_by_owner(id):
    return 'players.get_lineups_by_owner: [ lineup.id ] / wrong data'

@players.route('/get_lineups_by_tournament/<int:id>', methods=['GET'])
def get_lineups_by_tournament(id):
    return 'players.get_lineups_by_tournament: [ lineup.id ] / wrong data'

# JSON: {
#     id,
#     name
# }
@players.route('/edit_lineup/', methods=['PUT'])
def edit_lineup():
    return 'players.edit_lineup: ok / wrong data'

# JSON: {
#     id
# }
@players.route('/remove_lineup/', methods=['POST'])
def remove_lineup():
    return 'players.remove_lineup: ok / wrong data'

@players.route('/get_tournament/<int:id>', methods=['GET'])
def get_tournament(id):
    return 'players.get_tournament: tournament.name, tournament.description, tournament.game, tournament.prize, ' + \
        'tournament.start_date, tournament.end_date, tournament.team_format, tournament.teams_count / wrong data'

@players.route('/get_tournaments/', methods=['GET'])
def get_tournaments():
    return 'players.get_tournaments: [ tournament.id ]'