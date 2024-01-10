from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import User,Profile,Payment,Category, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)

migrate = Migrate(app,db)

# db.init_app(app)

@app.route('/')
def index():
    return 'Hello World'


# class User(Resource):
#     def get (self, id):
#         users_dict_list = [user.to_dict() for user in User.query.all()]
#         response = make_response(
#             jsonify(users_dict_list),
#             200,
#         )
#         return response
#     def post(self):
#         form=request.get_json()  
#         new_user = User(
#             name=form["name"],
#             email=form["email"],
#             password=form["password"],
#             phone_number=form["phone"],
#         )  
#         db.session.add(new_user)
#         db.session.commit()

#         return make_response(
#             jsonify(new_user.to_dict()),
#             201,
#         )
    


if __name__ == "__main__":
    app.run(port="5555", debug=True) 