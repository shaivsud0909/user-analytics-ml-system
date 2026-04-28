from app.db.models import User 
from app.auth.utils import hash_password,create_access_token,verify_password
from fastapi import HTTPException



def signup(request, db):
    # check password
    if request.password != request.confirm_password:
        return {"error": "Passwords do not match"}

    # check user exists
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        raise HTTPException(status_code=401, detail="User already exists")

    # create user
    new_user = User(
        email=request.email,
        password=hash_password(request.password),
        role="user"
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}






def login(request,db):
    #get user from db 
    user = db.query(User).filter(User.email == request.email).first()

    #Check if user exists
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    #Verify password
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    #Create JWT token
    token = create_access_token({
        "sub": user.email,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

