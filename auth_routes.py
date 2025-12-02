from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import sessionmaker
from models import User
from dependencies import get_session
from main import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix='/auth',tags=['auth'])

@auth_router.get('/')
async def home():
    '''
    Rota padrão de autenticação
    '''
    return {'Autenticar':'Rota de Autenticação'}

@auth_router.post('/create_user')
async def create_user(user_schema: UserSchema, 
                      session: Session = Depends(get_session)):
    user = session.query(User).filter(User.email==user_schema.email).first()
    if user:
        raise HTTPException (status_code=400, detail='E-mail já cadastrado')
    else:
        password_cript = bcrypt_context.hash(user_schema.password)
        new_user = User(user_schema.name, user_schema.phone_number, user_schema.email, 
                        password_cript, user_schema.admin)
        session.add(new_user)
        session.commit() 
        return {'mensagem': f'usuário cadastrado {user_schema.email}'}