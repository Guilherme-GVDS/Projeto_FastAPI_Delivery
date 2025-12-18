# 📦 Projeto FastAPI Delivery

API RESTful de um sistema de Delivery construída com FastAPI, destinada a gerenciar pedidos, autenticação de usuários e rotas de produtos.

Este projeto foi desenvolvido como exemplo prático de backend com Python, utilizando as melhores práticas de API modernas, integração com banco de dados e estrutura organizada.


## 🧠 Tecnologias

O projeto utiliza as seguintes tecnologias:


* ⚡ [FastAPI](https://fastapi.tiangolo.com/) — framework web de alta performance para APIs RESTful (baseado em Starlette e Pydantic) 
fastapi.tiangolo.com

* 📦 [SQLAlchemy](https://www.sqlalchemy.org/) — para trabalhar com banco de dados

* 🛠️ [Alembic](https://alembic.sqlalchemy.org/en/latest/) — para migrações de banco de dados


## 🚀 Funcionalidades

Esse backend de delivery inclui:

* 🔐 Sistema de autenticação de usuários (login/cadastro)

* 📝 CRUD de pedidos (order_routes.py)

* 📊 Modelos e schemas claros para entrada e saída de dados

* 🧩 Organização de rotas por módulos

* 📦 Arquitetura com dependências separadas

* 📦 Migrações com Alembic


## 📁 Como rodar

* Rodar servidor FastAPI (uvicorn main:app --reload)

* A API ficará disponível em:

  http://127.0.0.1:8000

* 📜 Rotas e Endpoints

  Após iniciar a aplicação, você pode visualizar a documentação automática gerada pelo FastAPI em:

  http://127.0.0.1:8000/docs

  Esses dashboards permitem testar todos os endpoints diretamente no navegador.


## 🎯 Boas práticas

* Esse projeto segue conceitos como:

* Tipagem com Pydantic

* Modularização de rotas

* Validação automática de request/response

* Migrações de banco com Alembic


## 📌 Contribuições

Contribuições são bem-vindas!
Sinta-se à vontade para enviar issues, melhorar rotas ou adicionar novos recursos.


[Linkedin](https://www.linkedin.com/in/guilherme-v-848a1013a/)
