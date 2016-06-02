from flask import Blueprint, json, request, session

from app.models.profile import Profile

profile = Blueprint('profile', __name__,)


@profile.route('/user/profile/create', methods=['POST'])
def create_user_profile():
    email = request.args.get('email')
    gender = request.args.get('gender')
    age = request.args.get('age')
    vision = request.args.get('vision')
    abilities = request.args.get('abilities')
    skills = request.args.get('skills')
    formation = request.args.get('formation')
    experience = request.args.get('experience')
    courses = request.args.get('courses')
    workshops = request.args.get('workshops')
    seminars = request.args.get('seminars')
    papers = request.args.get('papers')
    publications = request.args.get('publications')
    scholarships = request.args.get('scholarships')
    if request.args.get('email') is None or len(request.args.get('email')) == 0:
        res = {'error': 'Debe proporcionar un e-mail válido.'}
    else:
        ProfileInstance = Profile()
        result = ProfileInstance.createProfile(
            email, gender, age, vision, abilities, skills, formation,
            experience, courses, workshops, seminars, papers, publications,
            scholarships)
        res = result

    return json.dumps(res)

@profile.route('/user/profile/update', methods=['PUT'])
def update_user_profile():
    email = request.args.get('email')
    gender = request.args.get('gender')
    age = request.args.get('age')
    vision = request.args.get('vision')
    abilities = request.args.get('abilities')
    skills = request.args.get('skills')
    formation = request.args.get('formation')
    experience = request.args.get('experience')
    courses = request.args.get('courses')
    workshops = request.args.get('workshops')
    seminars = request.args.get('seminars')
    papers = request.args.get('papers')
    publications = request.args.get('publications')
    scholarships = request.args.get('scholarships')
    if request.args.get('email') is None or len(request.args.get('email')) == 0:
        res = {'error': 'Debe proporcionar un e-mail válido.'}
    else:
        ProfileInstance = Profile()
        result = ProfileInstance.updateProfile(
            email, gender, age, vision, abilities, skills, formation,
            experience, courses, workshops, seminars, papers, publications,
            scholarships)
        res = result

    return json.dumps(res)

@profile.route('/user/profile', methods=['GET'])
def get_user_profile():
    email = request.args.get('email')
    if request.args.get('email') is None or len(request.args.get('email')) == 0:
        res = {'error': 'Debe proporcionar un e-mail válido.'}
    else:
        ProfileInstance = Profile()
        profile = ProfileInstance.getProfileByEmail(email)
        # Must send "English" object...
        result = {'email': profile.email,
                  'gender': profile.sexo,
                  'age': profile.edad,
                  'vision': profile.vision,
                  'abilities': profile.habilidades,
                  'skills': profile.destrezas,
                  'formation': profile.formacion,
                  'experience': profile.experiencia,
                  'courses': profile.cursos,
                  'workshops': profile.talleres,
                  'seminars': profile.seminarios,
                  'papers': profile.ponencias,
                  'publications': profile.publicaciones,
                  'scholarships': profile.becas}

    # trick to easily convert the class to something json serializable
    # we get the  __dict__ an remove the unserializable
    # result.__dict__.pop('_sa_instance_state', None)
    # return json.dumps(result.__dict__)
    return json.dumps(result)

@profile.route('/user/profile/delete', methods=['POST'])
def delete_user_profile():
    result = []
    id = request.args.get('id')
    if request.args.get('id') is None or len(request.args.get('id')) == 0:
        res = {'error': 'Debe proporcionar un id válido.'}
    else:
        ProfileInstance = Profile()
        result = ProfileInstance.deleteProfile(int(id))
    return json.dumps(result)

