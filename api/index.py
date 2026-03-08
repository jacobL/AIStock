from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.schemas import UserRegister, UserLogin
from app.auth import hash_password, verify_password, create_token
#uvicorn index:app --host 127.0.0.1 --port 81 --reload
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing = db.query(User).filter(User.email == user.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="email exists")

    new_user = User(
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "register success"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="invalid login")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="invalid login")

    token = create_token(db_user.email)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
