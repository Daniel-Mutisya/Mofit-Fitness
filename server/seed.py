from app import create_app, db, User, Profile, Payment, Category


def seed_data():
    app = create_app()
    
    app.app_context().push()
    
    with app.app_context():
        db.create_all()

   
    # Create sample users
    user1 = User(first_name='DANIEL', last_name='MUTISYA', email='danielmutisya203@gmail.com', password='dan12345', phone_number='0705919657') 
    user2 = User(first_name='ARNOLD', last_name= 'MOSE', email='arnold@mofit.co.ke', password='arnold2030', phone_number='0728723866')

    # Create sample profiles
    profile1 = Profile(name='DANIEL', user=user1, phone_number='0705919657', date_of_birth=19980307, place_of_work='Office', age=25, height=180, weight=60, body_mass_index=25, body_fat=15, v_fat=10, kilo_calories=2000)
    profile2 = Profile(name='ARNOLD', user=user2, phone_number='0728723866', date_of_birth=19900101, place_of_work='Office', age=35, height=175, weight=70, body_mass_index=25, body_fat=15, v_fat=10, kilo_calories=2000)

    # Create sample payments
    payment1 = Payment(amount=3000, user=user1)
    payment2 = Payment(amount=3500, user=user2)

    # Create sample categories
    category1 = Category(name='Gym Only')
    category2 = Category(name='Gym and Nutrition')

    # Add data to the session
    db.session.add_all([user1, user2, profile1, profile2, payment1, payment2, category1, category2])

    # Commit the changes to the database
    db.session.commit()

if __name__ == "__main__":

    # Seed the data
    seed_data()