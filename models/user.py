from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    name = pw.CharField(unique=False)
    email = pw.CharField()
    password = pw.CharField()

    

