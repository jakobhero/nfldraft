from flask import Flask
from models import Player, db
import csv

def parse_line(line):
    out={}
    out['rank']=int(line['RK'])
    out['tier']=int(line['TIERS'])
    out['name']=line['PLAYER NAME']
    out['team']=None if line['TEAM']=='FA' else line['TEAM']
    if(line['POS'][:2]=='QB'):
        out['pos']='QB'
        out['pos_rank']=int(line['POS'][2:])
    elif(line['POS'][:2]=='RB'):
        out['pos']='RB'
        out['pos_rank']=int(line['POS'][2:])
    elif(line['POS'][:2]=='TE'):
        out['pos']='TE'
        out['pos_rank']=int(line['POS'][2:])
    elif(line['POS'][:2]=='WR'):
        out['pos']='WR'
        out['pos_rank']=int(line['POS'][2:])
    elif(line['POS'][:1]=='K'):
        out['pos']='K'
        out['pos_rank']=int(line['POS'][1:])
    elif(line['POS'][:3]=='DST'):
        out['pos']='D/ST'
        out['pos_rank']=int(line['POS'][3:])
    out['bye']=None if line['BYE WEEK']=='-' else int(line['BYE WEEK'])
    out['sos']=None if line['SOS SEASON']=='-' else int(line['SOS SEASON'][:1])
    out['ecr_vs_adp']=None if line['ECR VS. ADP']=='-' else int(line['ECR VS. ADP'])
    return out

init_app=Flask('init_app')
init_app.app_context().push()
uri='sqlite:///nfl_fantasy.db'
init_app.config['SQLALCHEMY_DATABASE_URI']=uri
db.init_app(init_app)
db.create_all(app=init_app)

with open('player_rankings.csv', 'r') as player_csv:
    reader=csv.DictReader(player_csv)
    for line in reader:
        player=(parse_line(line))
        db_player=Player(
            rank=player['rank'],
            tier=player['tier'],
            name=player['name'],
            team=player['team'],
            pos=player['pos'],
            pos_rank=player['pos_rank'],
            bye=player['bye'],
            sos=player['sos'],
            ecr_vs_adp=player['ecr_vs_adp']
        )
        db.session.add(db_player)
db.session.commit()

