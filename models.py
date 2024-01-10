import SQLAlchemy from Flask.SQLAlchemy
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class Admin(db.Model):
    __tablename__='admins'

    id= db.Column(db.Integer, primary_key=True)
    admin_id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    phone_number= db.Column(db.Integer)



class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String)
    last_name= db.Column(db.String)
    email= db.Column(db.String)
    password= db.Column(db.String)
    phone_number= db.Column(db.Integer)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class Profile(db.Model):
    __tablename__='profiles'

    id = db.Column(db.Integer, primary_key=True)
    phone_number= db.Column(db.Integer)
    date_of_birth= db.column(db.integer)
    place_of_work= db.column(db.string)
    age= db.column(db.integer)
    height= db.column(db.integer)
    weight= db.column(db.integer)
    body_mass_index= b.column(db.integer)
    body_fat = db.column(db.integer)
    v_fat= db.column(db.integer)
    kilo_calories= db.column(db.integer)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class Category(db.Model):
    __tablename__='categories' 
    iid = db.Column(db.Integer, primary_key=True)
    name =db.column(db.string)
    user_id= db.column(db.integer)




class Payment(db.Model):
    __tablename__='payments'

    id = db.Column(db.Integer, primary_key=True)
    payment_amount= db.column(db.integer)
    payment_date = db.column(db.integer)
    user_id = db.column(db.integer)
    category_id=db.column(db.integer)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())



class User_category(db.Model):
    __tablename__='usercategories' 
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.column(db.integer)
    category_id =db.column(db.integer)




    