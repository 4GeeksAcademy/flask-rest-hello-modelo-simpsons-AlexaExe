from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):#representa mi tabla personajes de mi base de datos
    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False) 
    quote: Mapped[str] =  mapped_column(String(200), nullable=False) 
    image:  Mapped[str] = mapped_column(String(255), nullable=False) 
    
    def serialize(self): #método    
        return {

            "id": self.id,
            "name": self.name,
            "quote": self.quote,
            "image": self.image

        }
  

class Location(db.Model):#representa mi tabla Lugares de mi base de datos
    __tablename__ = 'locations'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    quote: Mapped[str] = mapped_column(String(200), nullable=False)
    image:  Mapped[str] = mapped_column(String(255), nullable=False)

    
    
    def serialize(self): #método    
        return {

            "id": self.id,
            "name": self.name,
            "quote": self.quote,
            "image": self.image
        }
    

class Favorite(db.Model):   # representa mi tabla de favoritos del user
    __tablename__ = 'Favorites'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    character_id: Mapped[str] = mapped_column(db.ForeignKey('characters.id'))
    location_id: Mapped[str] = mapped_column(db.ForeignKey('locations.id'))
    
    
    def serialize(self): #método    
        return {

            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "location_id": self.location_id
        }
