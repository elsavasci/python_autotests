import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'  #задаем переменные
TOKEN = 'c46e9070164678b5e6471b975819af49' 
HEADER = {'Content-Type':'application/json', "trainer_token":TOKEN}
TRAINER_ID = '2470'

#проверка, что в ответе co списком тренеров приходит статус код 200 ОК
def test_status_code():
    response_trainers = requests.get(url = f'{URL}/trainers')
    assert response_trainers.status_code == 200

#проверка, что в ответе приходит строчка с именем твоего тренера
def test_part_of_response():
    response_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}) 
    assert response_trainers.json()['data'][0]['trainer_name'] == 'Ash' 