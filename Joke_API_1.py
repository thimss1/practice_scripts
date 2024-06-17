import requests

for i in range(10):
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    data = response.json()
    if data['type'] == 'single':
        print(data['joke'])
    else:
        print(data['setup'])
        print(data['delivery'])