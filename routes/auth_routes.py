from fastapi import APIRouter, Depends
from core.config import get_db
from core.auth_token import create_token
from schemas.api_response import Response
from sqlalchemy.orm import Session
from schemas.user_schemas import UserSchema
from services.auth_validation import authenticate

router = APIRouter()


@router.post("/login")
async def login(request: UserSchema, db: Session = Depends(get_db)):

    _authentication = authenticate(db=db, user=request)

    if _authentication is not None:
        token = create_token(_authentication.usuario)

        return Response(
            code='Ok',
            status='200',
            message='Login Successful',
            result={'access_token': token, 'token_type': 'bearer'}
        )

    return Response(
        code='Error',
        status='401',
        message="Incorrect credentials"
    )
