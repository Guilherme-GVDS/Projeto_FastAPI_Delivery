from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth',tags=['auth'])

@auth_router.get('/')
async def authenticate():
    '''
    Rota padrão de autenticação
    '''
    return {'Autenticar':'Rota de Autenticação'}