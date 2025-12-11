import requests

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZXhwIjoxNzY1ODkyODgxfQ.IdLW2HkMApS7aS17JtSiwcq-sIFWGLQ7MJz0eomwers'

}

requisicao  = requests.get('http://127.0.0.1:8000/auth/refresh', headers = headers)
print(requisicao)
print (requisicao.json())