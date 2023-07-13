import sender_stand_request
import data,configuration
import requests


def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=data.headers,
                         json=data.user_body)

def get_order_by_number(track_n):
    param = {"t": track_n}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                         headers=data.headers,
                         params=param)



# Наталия Ситникова, 6-я когорта - Финальный проект. Инженер по тестированию плюс.

def test_client_order():
    track = create_order()
    track_number = track.json()["track"]
    response = get_order_by_number(track_number)
    assert response.status_code == 200
