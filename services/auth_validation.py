from core.config import get_db
from schemas.user_schemas import UserSchema
from services.user_crud import get_user_by_usuario
from sqlalchemy.orm import Session




def authenticate(db: Session, user: UserSchema):
    _user = get_user_by_usuario(db=db, usuario=user.usuario)

    if _user is None:
        return None

    if _user.password == user.password:
        return _user
