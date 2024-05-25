from sqlalchemy.orm import Session
from models import medico
from schemas.user_schemas import UserSchema

def list_users(db: Session):
    return db.query(medico).all()

def create_user(db: Session, user: UserSchema):
    db_user = medico(email=user.email, name=user.name, hashed_password=user.password)  # Ensure you hash the password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(medico).filter(medico.id == user_id).first()


def get_user_by_usuario(db: Session, usuario: str):
    return db.query(medico).filter(medico.usuario == usuario).first()


def delete_user(db: Session, user_id: int):
    _user = get_user(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()
    return _user


def update_user(db: Session, user_id: int, user: UserSchema):
    _user = get_user(db=db, user_id=user_id)
    _user.name = user.usuario
    _user.password = user.usuario
    db.commit()
    db.refresh(_user)
    return _user