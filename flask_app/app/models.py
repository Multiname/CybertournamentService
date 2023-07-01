from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Moderator(db.Model):
    __tablename__ = 'moderators'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

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
    password = db.Column(db.String(30), nullable=False)
    points = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<{}:{}>'.format(self.id, self.nickname)
    
players_lineups = db.Table('players_lineups',
                           db.Column('player_id', db.Integer, db.ForeignKey('players.id')),
                           db.Column('lineup_id', db.Integer, db.ForeignKey('lineups.id')),
                           db.Column('is_owner', db.Boolean, nullable=False))

class Lineup(db.Model):
    __tablename__ = 'lineups'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    place = db.Column(db.Integer(), nullable=True)
    is_active = db.Column(db.Boolean(), nullable=False)
    
    tournament_id = db.Column(db.Integer(), db.ForeignKey('tournaments.id'))

    players = db.relationship('Player', secondary=players_lineups, backref='lineups')

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