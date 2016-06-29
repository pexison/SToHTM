from flask import Blueprint, json, request, session

from app.models.reputation import Reputation

reputation = Blueprint('reputation', __name__,)

@reputation.route('/reputation/create', methods=['POST'])
def create_reputation():
    contract = request.args.get('contract')
    ratedUser = request.args.get('ratedUser')
    value = request.args.get('value')
    user = session['email']
    if request.args.get('contract') is None or len(request.args.get('contract')) == 0:
        res = {'error': 'You must provide a valid contract number.'}
    if request.args.get('ratedUser') is None or len(request.args.get('ratedUser')) == 0:
        res = {'error': 'You must provide a valid user to rate.'}
    if request.args.get('value') is None or len(request.args.get('value')) == 0:
        res = {'error': 'You must provide a valid value.'}
    else:
        ReputationInstance = Reputation()
        result = ReputationInstance.createReputation(
            contract, user, ratedUser, value)
        res = result

    return json.dumps(res)

@reputation.route('/reputations', methods=['GET'])
def get_reputations():
    ReputationInstance = Reputation()
    reputations = ReputationInstance.getReputations()
    rescat = []
    for reputation in reputations:
        rescat.append({'id': reputation.reputationId,
                       'contract': reputation.contract,
                       'user': reputation.user,
                       'ratedUser': reputation.ratedUser,
                       'value': reputation.value})
    return json.dumps(rescat)

@reputation.route('/userReputations', methods=['GET'])
def get_user_reputations():
    user = session['email']
    ReputationInstance = Reputation()
    reputations = ReputationInstance.getReputationsByUser(user)
    rescat = []
    for reputation in reputations:
        rescat.append({'id': reputation.reputationId,
                       'contract': reputation.contract,
                       'user': reputation.user,
                       'ratedUser': reputation.ratedUser,
                       'value': reputation.value})
    res = {'result':rescat}
    return json.dumps(res)

@reputation.route('/reputation', methods=['GET'])
def get_reputation():
    reputationId = request.args.get('reputationId')
    if request.args.get('reputationId') is None or len(request.args.get('reputationId')) == 0:
        res = {'error': 'You must provide a valid reputation id.'}
    else:
        ReputationInstance = Reputation()
        reputation = ReputationInstance.getReputationById(reputationId)
        res = {'id': reputation.reputationId,
               'contract': reputation.contract,
               'user': reputation.user,
               'ratedUser': reputation.ratedUser,
               'value': reputation.value}
    return json.dumps(res)

@reputation.route('/reputations/delete', methods=['POST'])
def delete_reputation():
    reputationId = int(request.args.get('reputationId'))
    if request.args.get('reputationId') is None or len(request.args.get('reputationId')) == 0:
        res = {'error': 'You must provide a valid reputation id.'}
    else:
        ReputationInstance = Reputation()
        result = ReputationInstance.deleteReputation(reputationId)
        res = result

    return json.dumps(res)

@reputation.route('/reputations/update', methods=['POST'])
def update_reputation():
    reputationId = int(request.args.get('reputationId'))
    contract = request.args.get('contract') or None
    user = request.args.get('user') or None
    ratedUser = request.args.get('ratedUser') or None
    value = request.args.get('value') or None
    if request.args.get('reputationId') is None or len(request.args.get('reputationId')) == 0:
        res = {'error': 'You must provide a valid reputation id.'}
    else:
        ReputationInstance = Reputation()
        result = ReputationInstance.updateReputation(
            reputationId, contract, user, ratedUser, value)
        res = result

    return json.dumps(res)
