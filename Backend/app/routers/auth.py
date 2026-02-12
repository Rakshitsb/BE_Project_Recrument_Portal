from fastapi import APIRouter, HTTPException
from app.db.database import user_collection
from app.core.security import create_access_token
from app.schemas.user import UserCreate
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(email: str, password: str):
    user = user_collection.find_one({"email": email, "password": password})

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "email": user["email"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }



@router.post("/signup")
def signup(user: UserCreate):
    # Check duplicate email
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = {
        "name": user.name,
        "email": user.email,
        "password": user.password,  # plain text
        "role": user.role           # USER or HR only
    }

    user_collection.insert_one(new_user)

    return {
        "message": "Signup successful",
        "email": user.email,
        "role": user.role
    }

