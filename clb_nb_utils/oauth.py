'''This module gets fresh access tokens from the Jupyterhub Service to refresh access tokens.

See https://github.com/HumanBrainProject/jupyterhub-access-token-service
'''

import os

import requests

JUPYTERHUB_API_TOKEN = os.getenv("JUPYTERHUB_API_TOKEN")
# @TODO fix this
JUPYTERHUB_SERVICE_URL = 'http://jupyterhub:8080/services'


def get_token():
    headers = {'Authorization': f'Token {JUPYTERHUB_API_TOKEN}'}
    url = f'{JUPYTERHUB_SERVICE_URL}/access-token-service/access-token'
    resp = requests.get(url, headers=headers)
    return resp.json().get('access_token')
