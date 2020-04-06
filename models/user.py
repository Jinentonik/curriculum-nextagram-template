from models.base_model import BaseModel
import peewee as pw
import re
from werkzeug.security import generate_password_hash

def is_upper_case(word):
    arr = []
    for char in word:
        if char.isupper():
            arr.append(char)
    
    return len(arr)
            

def is_lower_case(word):
    arr = []
    for char in word:
        if char.islower():
            arr.append(char)
        
    return len(arr)

def no_special_case(word):
    if len(re.findall('[^a-zA-Z0-9]', word)) == 0:
        return True 
    else:
        return False


class User(BaseModel):
    name = pw.CharField(unique=False, null = False)
    email = pw.CharField(null = False)
    password = pw.TextField( null = False)

    def validate(self):
        duplicate_name = User.get_or_none(User.name == self.name)
        check_name_length = len(self.name)
        check_password_length = len(self.password)
        
        if duplicate_name:
            self.errors.append("This name has already exist.")
        if is_upper_case(self.password) == 0:
            self.errors.append("Password must have at least 1 upper case character.")
        if is_lower_case(self.password) == 0:
            self.errors.append("Password must have at least 1 lower case character.")
        if no_special_case(self.password):
            self.errors.append("Password must have at least 1 special character.")
        if check_name_length < 6:
            self.errors.append("username must be 6 characters and above")
        if check_password_length < 6:
            self.errors.append("password must be 6 characters and above")
        else:
            self.password = generate_password_hash(self.password)
        
        



    

