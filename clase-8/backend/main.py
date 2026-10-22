from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .auth import create_access_token, get_current_user, hash_password, verify_password
from .database import Base, engine, get_db
from .models import Item, User
from .schemas import ItemCreate, ItemPublic, Token, UserCreate, UserPublic

Base.metadata.create_all(bind=engine)
app = FastAPI(title="JWT Scopes API", version="1.0.0")


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/auth/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register(data: UserCreate, db: Session = Depends(get_db)):
    if data.role not in {"reader", "editor"}:
        raise HTTPException(400, "El rol debe ser reader o editor")
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(409, "El usuario ya existe")
    user = User(username=data.username, hashed_password=hash_password(data.password), role=data.role)
    db.add(user); db.commit(); db.refresh(user)
    return user


@app.post("/api/auth/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(401, "Usuario o contraseña incorrectos")
    return {"access_token": create_access_token(user), "token_type": "bearer"}


@app.get("/api/me", response_model=UserPublic)
def me(current_user: User = Security(get_current_user, scopes=["read"])):
    return current_user


@app.get("/api/items", response_model=list[ItemPublic])
def list_items(db: Session = Depends(get_db), _: User = Security(get_current_user, scopes=["read"])):
    return db.query(Item).all()


@app.post("/api/items", response_model=ItemPublic, status_code=201)
def create_item(data: ItemCreate, db: Session = Depends(get_db), _: User = Security(get_current_user, scopes=["write"])):
    item = Item(**data.model_dump()); db.add(item); db.commit(); db.refresh(item)
    return item


@app.put("/api/items/{item_id}", response_model=ItemPublic)
def update_item(item_id: int, data: ItemCreate, db: Session = Depends(get_db), _: User = Security(get_current_user, scopes=["write"])):
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(404, "Elemento no encontrado")
    item.name, item.description = data.name, data.description
    db.commit(); db.refresh(item)
    return item


@app.delete("/api/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db), _: User = Security(get_current_user, scopes=["write"])):
    item = db.get(Item, item_id)
    if not item:
        raise HTTPException(404, "Elemento no encontrado")
    db.delete(item); db.commit()
