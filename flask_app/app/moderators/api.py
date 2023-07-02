from . import moderators
from ..models import Moderator, Player, Lineup, Tournament, db
from flask import request
import json

# JSON: {
#     name,
#     login,
#     password
# }
@moderators.route('/add_moderator/', methods=['POST'])
def add_moderator():
    content = request.get_json()

    if db.session.query(Moderator).filter(Moderator.login == content['login']).first() != None:
        return 'login already exists', 400

    moderator = Moderator()
    moderator.name = content['name']
    moderator.login = content['login']
    moderator.set_password(content['password'])

    db.session.add(moderator)
    db.session.commit()

    return 'moderator has been created', 201

# JSON: {
#     login,
#     password
# }
@moderators.route('/login/', methods=['PUT'])
def login():
    content = request.get_json()

    moderator = db.session.query(Moderator).filter(Moderator.login == content['login']).first()

    if moderator == None:
        return 'wrong login', 400
    if not moderator.check_password(content['password']):
        return 'wrong password', 400
        
    return json.dumps({
        'id': moderator.id,
        'name': moderator.name
    })

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
    content = request.get_json()
    
    tournament = Tournament()
    tournament.name = content['name']
    tournament.description = content['description']
    tournament.game = content['game']
    tournament.prize = content['prize']
    tournament.start_date = content['start_date']
    tournament.end_date = content['end_date']
    tournament.team_format = content['team_format']
    tournament.teams_count = content['teams_count']

    db.session.add(tournament)
    db.session.commit()

    return 'tournament has been created', 201

# JSON: {
#     id,
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
    content = request.get_json()

    tournament = db.session.query(Tournament).filter(Tournament.id == content['id']).first()
    if tournament == None:
        return 'wrong id', 400

    if content['name'] != None:
        tournament.name = content['name'] 
    if content['description'] != None:
        tournament.description = content['description'] 
    if content['game'] != None:
        tournament.game = content['game'] 
    if content['prize'] != None:
        tournament.prize = content['prize'] 
    if content['start_date'] != None:
        tournament.start_date = content['start_date'] 
    if content['end_date'] != None:
        tournament.end_date = content['end_date'] 
    if content['team_format'] != None:
        tournament.team_format = content['team_format'] 
    if content['teams_count'] != None:
        tournament.teams_count = content['teams_count'] 

    db.session.add(tournament)
    db.session.commit()

    return 'tournament has been updated'

# JSON: {
#     id
# }
@moderators.route('/remove_tournament/', methods=['POST'])
def remove_tournament():
    content = request.get_json()

    tournament = db.session.query(Tournament).filter(Tournament.id == content['id']).first()
    if tournament == None:
        return 'wrong id', 400
    
    db.session.delete(tournament)
    db.session.commit()

    return 'tournament has been deleted'

# JSON: {
#     id,
#     status
# }
@moderators.route('/set_lineup_activity_status/', methods=['PUT'])
def set_lineup_activity_status():
    content = request.get_json()

    lineup = db.session.query(Lineup).filter(Lineup.id == content['id']).first()
    if lineup == None:
        return 'wrong id', 400

    lineup.is_active = content['status']
    db.session.add(lineup)
    db.session.commit()

    return 'lineup has been updated'

# JSON: {
#     id,
#     place
# }
@moderators.route('/set_lineup_place/', methods=['PUT'])
def set_lineup_place():
    content = request.get_json()

    lineup = db.session.query(Lineup).filter(Lineup.id == content['id']).first()
    if lineup == None:
        return 'wrong id', 400

    lineup.place = content['place']
    db.session.add(lineup)
    db.session.commit()

    return 'lineup has been updated'

# JSON: {
#     id,
#     points
# }
@moderators.route('/set_player_points/', methods=['PUT'])
def set_player_points():
    content = request.get_json()

    player = db.session.query(Player).filter(Player.id == content['id']).first()
    if player == None:
        return 'wrong id', 400

    player.points = content['points']
    db.session.add(player)
    db.session.commit()

    return 'player has been updated'