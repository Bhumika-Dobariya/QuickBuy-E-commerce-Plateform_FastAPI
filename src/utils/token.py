from datetime import datetime,timedelta
from fastapi import HTTPException,status,Security
from dotenv import load_dotenv
import os
from jose import JWTError,jwt

from datetime import datetime,timedelta
from fastapi import HTTPException,status,Security
from dotenv import load_dotenv
import os
from jose import JWTError,jwt
load_dotenv()
SECRET_KEY = str(os.environ.get("SECRET_KEY"))
ALGORITHM = str(os.environ.get("ALGORITHM"))


def get_token(id):
    payload = {
        "user_id": id,
        "exp": datetime.now() + timedelta(minutes=15),
    }
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(type(access_token))
    return access_token


def get_token_logging(uname,password):
    payload = {
        "user_name": uname,
        "user_password" : password,
        "exp": datetime.now() + timedelta(minutes=15),
    }
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(type(access_token))
    return access_token


#_____________________decode_____________________

#id

def decode_token_user_id(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid token",)
        return user_id
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid token",)
        
   
#user_name     
  
def decode_token_uname(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_name = payload.get("user_name")
        if not user_name:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid token", )
        return user_name
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid token",)

#password

def decode_token_password(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_password = payload.get("user_password")
        if not user_password:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid token", )
        return user_password
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
        