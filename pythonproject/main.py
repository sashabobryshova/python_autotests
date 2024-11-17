import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6837b268f14fa6fb0024d14dd9fe2a72'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN} 
body_regitration = {
    "trainer_token": TOKEN,
    "email": "sashabobryshova@yandex.ru",
    "password": "070787AbC!"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Буль",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "135735",
    "name": "пух",
    "photo_id": 1
}

body_pokeball = {
    "pokemon_id": "135735"
}


# response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json= body_regitration)
# print(response.text)

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json= body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json= body_create)
print(response_create.text)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json= body_name)
print(response_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json= body_pokeball)
print(response_pokeball.text)