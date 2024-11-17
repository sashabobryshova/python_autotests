import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6837b268f14fa6fb0024d14dd9fe2a72'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN} 
TRAINER_ID = '6916'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID} ) 
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TOKEN} ) 
    assert response.get.json()["data"][0]["trainer_name"] == 'Sasha'    