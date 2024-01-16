from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin



db = SQLAlchemy()


class Admin(db.Model,SerializerMixin):
    __tablename__ = 'admins'

    # Serialize_rules= ('-users.admin',)
    id = db.Column(db.Integer, primary_key=True)
    admin_id= db.Column(db.Integer, unique=True)
    name= db.Column(db.String, nullable=False)
    phone_number= db.Column(db.Integer, nullable=False)

    # users= db.relationship('User', back_populates='admin')



class User(db.Model,SerializerMixin):
    __tablename__='users'
    Serialize_rules= ('-payments.user',)
    Serialize_rules= ('-categories.user',)
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String, nullable=False)
    last_name= db.Column(db.String, nullable=False)
    email= db.Column(db.String, unique=True)
    password= db.Column(db.String, unique=True)
    phone_number= db.Column(db.Integer, nullable=False)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # admin= db.Column(db.Integer, db.ForeignKey('admins.id'))
    payments= db.relationship('Payment', backref= 'user')
    categories= db.relationship('Category', backref= 'user')
    profile= db.relationship('Profile', back_populates='user', uselist=False)
    
    


class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    Serialize_rules= ('-payments.category',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    payments= db.relationship('Payment', backref= 'category')

    

class Profile(db.Model, SerializerMixin):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    place_of_work = db.Column(db.String(255))
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    body_mass_index = db.Column(db.Float, nullable=False)
    body_fat = db.Column(db.Float, nullable=False)
    v_fat = db.Column(db.Float, nullable=False)
    kilo_calories = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    user = db.relationship('User', back_populates='profile')



class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    payment_amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
  

   

    


    




    