from infra.configs.connection import DBConnectionHandler
from infra.entities.user import User
import bcrypt


class User_repository:
    def create_user(self, name, password, email):
        with DBConnectionHandler() as db:
            data = User(name, password, email)
            db.session.add(data)
            db.session.commit()
            

    def login(self, email, password):
        with DBConnectionHandler() as db:
            user = db.session.query(User).filter_by(email = email).first()
            hashed = str(user.userpasswords[0])
            return User_repository.check_password(password, hashed) 
    
    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(User).filter(User.id == id).delete()
            db.session.commit()

    @staticmethod    
    def check_password(password ,hashed):    
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


