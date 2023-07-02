from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Moderator(db.Model):
    __tablename__ = 'moderators'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<{}:{}>'.format(self.id, self.name)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.String(30), nullable=False)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    points = db.Column(db.Integer(), nullable=False, default=0)

    players_lineups = db.relationship('PlayerLineup', backref='player')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<{}:{}>'.format(self.id, self.nickname)
    
class PlayerLineup(db.Model):
    __tablename__ = 'players_lineups'

    id = db.Column(db.Integer(), primary_key=True)
    is_owner = db.Column(db.Boolean(), nullable=False, default=False)

    player_id = db.Column(db.Integer(), db.ForeignKey('players.id'), nullable=False)
    lineup_id = db.Column(db.Integer(), db.ForeignKey('lineups.id'), nullable=False)

    def __repr__(self):
        return '<{}:{}>'.format(self.player_id, self.lineup_id)

class Lineup(db.Model):
    __tablename__ = 'lineups'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    place = db.Column(db.Integer(), nullable=True)
    is_active = db.Column(db.Boolean(), nullable=False, default=False)
    
    tournament_id = db.Column(db.Integer(), db.ForeignKey('tournaments.id'), nullable=False)

    players_lineups = db.relationship('PlayerLineup', backref='lineup', cascade='all,delete-orphan')

    def __repr__(self):
        return '<{}:{}>'.format(self.id, self.name)
    
class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(), nullable=False)
    game = db.Column(db.String(50), nullable=False)
    prize = db.Column(db.Integer(), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    team_format = db.Column(db.Integer(), nullable=False)
    teams_count = db.Column(db.Integer(), nullable=False)

    lineups = db.relationship('Lineup', backref='tournament')

    def __repr__(self):
        return '<{}:{}>'.format(self.id, self.name)