from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.utils import get_db
from src.auth.crud import _create_user
from src.auth.schemas import UserOut


router_auth = APIRouter(prefix='/auth', tags=['auth'])


@router_auth.post('/',
                  summary='Создание пользоватея',
                  response_model=UserOut)
def create_user(username: str,
                db: Annotated[Session, Depends(get_db)]) -> UserOut:
    user = _create_user(username, db)
    return user
