from . import players
from ..models import Player, Lineup, PlayerLineup, Tournament, db
from flask import request
import json

# JSON: {
#     nickname,
#     login,
#     password
# }
@players.route('/register/', methods=['POST'])
def register():
    content = request.get_json()

    if db.session.query(Player).filter(Player.login == content['login']).first() != None:
        return 'login already exists', 400

    player = Player()
    player.nickname = content['nickname']
    player.login = content['login']
    player.set_password(content['password'])

    db.session.add(player)
    db.session.commit()

    return 'player has been registered', 201

# JSON: {
#     login,
#     password
# }
@players.route('/login/', methods=['PUT'])
def login():
    content = request.get_json()

    player = db.session.query(Player).filter(Player.login == content['login']).first()

    if player == None:
        return 'wrong login', 400
    if not player.check_password(content['password']):
        return 'wrong password', 400
        
    return json.dumps({
        'id': player.id,
        'nickname': player.nickname,
        'points': player.points
    })

@players.route('/get_player/<int:id>', methods=['GET'])
def get_player(id):
    player = db.session.query(Player).filter(Player.id == id).first()

    if player == None:
        return 'wrong id', 400

    return json.dumps({
        'nickname': player.nickname,
        'points': player.points
    })

@players.route('/get_players_by_lineup/<int:id>', methods=['GET'])
def get_players_by_lineup(id):
    players_lineups = db.session.query(PlayerLineup).filter(PlayerLineup.lineup_id == id).all()

    if players_lineups == None:
        return 'wrong id', 400

    playersIds = []
    for player_lineup in players_lineups:
        playersIds.append(player_lineup.player_id)

    return json.dumps(playersIds)

@players.route('/get_players/', methods=['GET'])
def get_players():
    players = db.session.query(Player).all()

    playersIds = []
    for player in players:
        playersIds.append(player.id)

    return json.dumps(playersIds)

# JSON: {
#     name,
#     owner_id,
#     tournament_id
# }
@players.route('/add_lineup/', methods=['POST'])
def add_lineup():
    content = request.get_json()

    tournament = db.session.query(Tournament).filter(Tournament.id == content['tournament_id']).first()
    if tournament == None:
        return 'wrong tournament id', 400
    
    for lineup in tournament.lineups:
        if lineup.name == content['name']:
            return 'the name is already taken', 400

        for player_lineup in lineup.players_lineups:
            if player_lineup.player_id == content['owner_id']:
                return 'player is already a member of the tournament', 400
    
    lineup = Lineup()
    lineup.name = content['name']
    lineup.tournament_id = content['tournament_id']

    player_lineup = PlayerLineup()
    player_lineup.is_owner = True
    player_lineup.player_id = content['owner_id']
    player_lineup.lineup = lineup

    db.session.add(lineup)
    db.session.add(player_lineup)
    db.session.commit()

    return 'lineup has been created', 201

@players.route('/get_lineup/<int:id>', methods=['GET'])
def get_lineup(id):
    lineup = db.session.query(Lineup).filter(Lineup.id == id).first()

    if lineup == None:
        return 'wrong id', 400
    
    owner_id = None
    for player_lineup in lineup.players_lineups:
        if player_lineup.is_owner:
            owner_id = player_lineup.player_id

    return json.dumps({
        'name': lineup.name,
        'place': lineup.place,
        'is_active': lineup.is_active,
        'owner_id': owner_id,
        'tournament_id': lineup.tournament_id
    })

@players.route('/get_lineups_by_owner/<int:id>', methods=['GET'])
def get_lineups_by_owner(id):
    players_lineups = db.session.query(PlayerLineup).filter(PlayerLineup.player_id == id and
                                                            PlayerLineup.is_owner).all()
    
    lineupsIds = []
    for player_lineup in players_lineups:
        lineupsIds.append(player_lineup.lineup_id)

    return json.dumps(lineupsIds)

@players.route('/get_lineups_by_tournament/<int:id>', methods=['GET'])
def get_lineups_by_tournament(id):
    lineups = db.session.query(Lineup).filter(Lineup.tournament_id == id).all()
    
    lineupsIds = []
    for lineup in lineups:
        lineupsIds.append(lineup.id)

    return json.dumps(lineupsIds)

# JSON: {
#     id,
#     name
# }
@players.route('/edit_lineup/', methods=['PUT'])
def edit_lineup():
    content = request.get_json()

    lineup = db.session.query(Lineup).filter(Lineup.id == content['id']).first()
    if lineup == None:
        return 'wrong id', 400

    lineup.name = content['name']
    db.session.add(lineup)
    db.session.commit()

    return 'lineup has been updated'

# JSON: {
#     id
# }
@players.route('/remove_lineup/', methods=['POST'])
def remove_lineup():
    content = request.get_json()

    lineup = db.session.query(Lineup).filter(Lineup.id == content['id']).first()
    if lineup == None:
        return 'wrong id', 400
    
    db.session.delete(lineup)
    db.session.commit()

    return 'lineup has been deleted'

# JSON: {
#     lineup_id,
#     member_id
# }
@players.route('/add_lineup_member/', methods=['POST'])
def add_lineup_member():
    content = request.get_json()

    if db.session.query(PlayerLineup).filter(PlayerLineup.lineup_id == content['lineup_id']).\
                                    filter(PlayerLineup.player_id == content['member_id']).first() != None:
        return 'This player is already a member of the lineup', 400

    lineup = db.session.query(Lineup).filter(Lineup.id == content['lineup_id']).first()
    if lineup == None:
        return 'wrong id', 400
    
    player_lineup = PlayerLineup()
    player_lineup.lineup_id = content['lineup_id']
    player_lineup.player_id = content['member_id']

    db.session.add(player_lineup)
    db.session.commit()

    return 'Player has been assigned to the lineup', 201

@players.route('/get_tournament/<int:id>', methods=['GET'])
def get_tournament(id):
    tournament = db.session.query(Tournament).filter(Tournament.id == id).first()

    if tournament == None:
        return 'wrong id', 400

    return json.dumps({
        'name': tournament.name,
        'description': tournament.description,
        'game': tournament.game,
        'prize': tournament.prize,
        'start_date': str(tournament.start_date),
        'end_date': str(tournament.end_date),
        'team_format': tournament.team_format,
        'teams_count': tournament.teams_count
    })

@players.route('/get_tournaments/', methods=['GET'])
def get_tournaments():
    tournaments = db.session.query(Tournament).all()

    tournamentsIds = []
    for tournament in tournaments:
        tournamentsIds.append(tournament.id)

    return json.dumps(tournamentsIds)