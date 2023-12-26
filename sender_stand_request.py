import configuration
import requests
import data

def post_new_user(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
def get_token():
    response = post_new_user(data.user_body)
    response_data = response.json()
    return response_data['authToken']

def create_kit(kit_body):
    auth_token = get_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, headers=headers,
                             json=kit_body)

    return response