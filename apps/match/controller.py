import json
from flask import request, jsonify, make_response
from . import match
from apps.common.dataUtils import obj_to_dict
from apps.model import User, Match
from apps.database import db_session

# user object -> dictionary
def get_user_match_dict( match ):
    dict = obj_to_dict(match)
    return dict

def get_match( match_id = 0):
    if match_id == 0 :
        return Match.query.all()

    return Match.query.filter_by(match_id=match_id ).first()

@match.route('/', methods=['GET'])
def select_list():
    print("[match] list ")

    response = []
    matches = get_match()
    for match in matches:
        response.append( get_user_match_dict( match ))

    # print( response )
    return json.dumps( response )

# [nouse] 의미가 없음
@match.route('/<int:match_id>/', methods=['GET'])
def select(match_id ):
    print("[match] get  = ", match_id )
    match = get_match( match_id )
    return json.dumps( get_user_match_dict( match ))

@match.route('/', methods=['POST'])
def post():
    channel_id = request.form['channel_id']
    host_user_id = request.form['host_user_id']
    guest_user_id = request.form['guest_user_id']

    print("[post] match = ( host_user:%s, guest_user:%s, channel_id:%r)" % (host_user_id, guest_user_id, channel_id ))

    match = Match( host_user_id, guest_user_id, channel_id )
    try:
        db_session.add(match)
        db_session.commit()
        print("match was commited")
        # db_session.close()
    except:
        db_session.rollback()

    match = get_match( match.match_id)
    return json.dumps(obj_to_dict(match))


# [nouse] 의미가 없음
@match.route('/<int:match_id>/', methods=['PUT'])
def update(match_id ):
    print("[match] update ")
    return make_response( {}, 404)


@match.route('/<int:match_id>/', methods=['DELETE'])
def delete(match_id):
    print("[match] delete = ( match_id:%r)" % ( match_id ))

    try:
        db_session.query(Match).filter_by(match_id=match_id).delete()
        print("commit : match was deleted")
        db_session.commit()
    except Exception as e:
        print("[EXCEPTION] match delete, message = %s" % ( e ))
        db_session.rollback()

    data = { 'success' : True }
    return make_response( jsonify(data), 200 )