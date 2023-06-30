from . import moderators

# CRUD турниров
# Подтверждение команды
# Назначение победителей
# Выставление очков

# JSON: {
#     name,
#     login,
#     password
# }
@moderators.route('/add_moderator/', methods=['POST'])
def add_moderator():
    return 'moderators.add_moderator: ok / password exists'

# JSON: {
#     login,
#     password
# }
@moderators.route('/login/', methods=['PUT'])
def login():
    return 'moderators.login: moderator.id, moderator.name / wrong data'

# JSON: {
#     name,
#     description,
#     game,
#     prize,
#     start_date,
#     end_date,
#     team_format,
#     teams_count
# }
@moderators.route('/add_tournament/', methods=['POST'])
def add_tournament():
    return 'moderators.add_tournament: ok / wrong data'

@moderators.route('/get_tournament/<int:id>', methods=['GET'])
def get_tournament(id):
    return 'moderators.get_tournament: tournament.name, tournament.description, tournament.game, tournament.prize, ' +\
        'tournament.start_date, tournament.end_date, tournament.team_format, tournament.teams_count / wrong data'

@moderators.route('/get_tournaments/<int:id>', methods=['GET'])
def get_tournaments(id):
    return 'moderators.get_tournaments: [ tournament.id ] / wrong data'

# JSON: {
#     name,
#     description,
#     game,
#     prize,
#     start_date,
#     end_date,
#     team_format,
#     teams_count
# }
@moderators.route('/edit_tournament/', methods=['PUT'])
def edit_tournament():
    return 'moderators.edit_tournament: ok / wrong data'

# JSON: {
#     id
# }
@moderators.route('/remove_tournament/', methods=['POST'])
def remove_tournament():
    return 'moderators.remove_tournament: ok / wrong data'

# JSON: {
#     id,
#     status
# }
@moderators.route('/set_lineup_activity_status/', methods=['PUT'])
def set_lineup_activity_status():
    return 'moderators.set_lineup_activity_status: ok / wrong data'

# JSON: {
#     id,
#     place
# }
@moderators.route('/set_lineup_place/', methods=['PUT'])
def set_lineup_place():
    return 'moderators.set_lineup_place: ok / wrong data'

# JSON: {
#     id,
#     points
# }
@moderators.route('/set_player_points/', methods=['PUT'])
def set_player_points():
    return 'moderators.set_player_points: ok / wrong data'