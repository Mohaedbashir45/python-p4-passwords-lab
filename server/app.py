def post(self):
        return user.to_dict(), 201

class CheckSession(Resource):
    pass
    def get(self):
        # user = User.query.filter(User.id == session.get('user_id')).first()
        # if user:
        #     return user.to_dict()
        # else:
        #     return '', 204

        if 'user_id' in session and session['user_id'] is not None:
            user_id = int(session['user_id'])
            user = db.session.get(User, user_id)
            if user:

                return user.to_dict(), 200

        return {'': ''}, 204



class Login(Resource):
    pass
    def post(self):

        json = request.get_json()
        user = User.query.filter_by(username=json['username']).first()

        if user and user.authenticate(json['password']):
            session['user_id'] = user.id
            session['page_views'] = 0
            return user.to_dict(), 200
        else:
            return {}, 401

class Logout(Resource):
    pass
    def delete(self):
        session['page_views'] = None
        session['user_id'] = None
        return {}, 204

api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)