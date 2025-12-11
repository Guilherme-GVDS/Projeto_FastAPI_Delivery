from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_session, verify_token
from schemas import OrderSchema, ItemOrderSchema, ResponseOrderSchema
from models import Order, User, ItemOrder
from typing import List

order_router = APIRouter(prefix='/orders', tags=['orders'], 
                         dependencies= [Depends(verify_token)])

@order_router.get('/')
async def orders():
    '''
    Rota de pedidos
    '''
    return {'teste':'Solicitação realizada com sucesso'}

@order_router.post('/order')
async def create_order(order_schema: OrderSchema, session: Session = Depends(get_session)):
    new_order = Order(user=order_schema.id_user)
    session.add(new_order)
    session.commit()
    return {'mensagem': f'Pedido criado com sucesso. ID do pedido: {new_order.id}'}

@order_router.post('/order/cancel/{id_order}')
async def cancel_order(id_order: int, session: Session = Depends(get_session), 
                       user: User = Depends(verify_token)):
    order = session.query(Order).filter(Order.id == id_order).first()
    if not order:
        raise HTTPException(status_code=400, detail='Pedido não encontrado')
    if not user.admin and user.id != order.user:
        raise HTTPException(status_code=401, 
                            detail='Você não tem autorização para fazer essa modificação')
    order.status = 'Cancelado'
    session.commit()
    return {
        'Mensagem': f'Pedido: {order.id} cancelado com sucesso',
        'Pedido': order
    }

@order_router.get('/list')
async def order_list (session: Session = Depends(get_session), 
                       user: User = Depends(verify_token)):
    if not user.admin:
        raise HTTPException (status_code=401, 
                             detail='Você não tem autorização para acessar essa página')
    else:
        orders = session.query(Order).all()
        return {
            'Pedidos': orders
        }
    
@order_router.post('/order/add-item/{id_order}')
async def add_item_order(id_order: int, 
                         item_order_schema: ItemOrderSchema, 
                         session: Session = Depends(get_session), 
                        user: User = Depends(verify_token)):
    order = session.query(Order).filter(Order.id==id_order).first()
    if not order:
        raise HTTPException (status_code=400, detail='Pedido não existe')
    if not user.admin and user.id != order.user:
        raise HTTPException(status_code=401, detail='Você não tem autorização para fazer essa modificação')
    item_order = ItemOrder(item_order_schema.item, item_order_schema.unit_price,
                           item_order_schema.quantity, id_order)
    session.add(item_order)
    order.calc_price()
    session.commit()
    return {
        'mensagem': 'Item criado com sucesso',
        'item_id': item_order.id,
        'preco_pedido': order.price 
    }

@order_router.post('/order/remove-item/{id_item_order}')
async def add_item_order(id_item_order: int, 
                         session: Session = Depends(get_session), 
                        user: User = Depends(verify_token)):
    item_order = session.query(ItemOrder).filter(ItemOrder.id==id_item_order).first()
    order = session.query(Order).filter(Order.id==item_order.order).first()
    if not item_order:
        raise HTTPException (status_code=400, detail='Item não existe no pedido')
    if not user.admin and user.id != order.user:
        raise HTTPException(status_code=401, detail='Você não tem autorização para fazer essa modificação')
    session.delete(item_order)
    order.calc_price()
    session.commit()
    return {
        'mensagem': 'Item removido com sucesso',
        'preco_pedido': len(order.items),
        'pedido': order
    } 

@order_router.post('/order/finish/{id_order}')
async def finish_order(id_order: int, session: Session = Depends(get_session), 
                       user: User = Depends(verify_token)):
    order = session.query(Order).filter(Order.id == id_order).first()
    if not order:
        raise HTTPException(status_code=400, detail='Pedido não encontrado')
    if not user.admin and user.id != order.user:
        raise HTTPException(status_code=401, 
                            detail='Você não tem autorização para fazer essa modificação')
    order.status = 'Finalizado'
    session.commit()
    return {
        'Mensagem': f'Pedido: {order.id} finalizado com sucesso',
        'Pedido': order
    }

@order_router.get('/order/{id_order}')
async def get_order(id_order: int, session: Session = Depends(get_session), 
                       user: User = Depends(verify_token)):
    order = session.query(Order).filter(Order.id == id_order).first()
    if not order:
        raise HTTPException(status_code=400, detail='Pedido não encontrado')
    if not user.admin and user.id != order.user:
        raise HTTPException(status_code=401, 
                            detail='Você não tem autorização para fazer essa modificação')
    return {
        'quantidade_itens_pedido': len(order.items),
        'pedido': order

    }

@order_router.get('/list/user-orders', response_model=List[ResponseOrderSchema])
async def orders_user (session: Session = Depends(get_session), 
                       user: User = Depends(verify_token)):
    orders = session.query(Order).filter(Order.user == user.id).all() 
    return orders