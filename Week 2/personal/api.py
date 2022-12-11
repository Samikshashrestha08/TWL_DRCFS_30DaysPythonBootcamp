import requests
respomse=requests.get('https://my-json-server.typicode.com/typicode/demo/posts')
print(respomse.json())