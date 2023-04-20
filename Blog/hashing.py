from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password:str):
       hashedPassword = pwd_cxt.hash(password) 
       return hashedPassword
    
    def verify(hashedPassword:str, password:str):
        return pwd_cxt.verify(password, hashedPassword)
