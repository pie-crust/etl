import getpass
import os
import json
import requests
 
 
# Vault Url
VAULT_URL = 'https://vault-dev.homegroup.com:8200'
# Update path as required, e.g. on home Linux should be /etc/pki/tls/certs/ca-bundle.crt
os.environ['REQUESTS_CA_BUNDLE'] = 'H:/git/vault.util/python/home.crt'
 
def login():
    password = getpass.getpass(prompt='Please enter your AD password: ')
    response = requests.post('{0}/v1/auth/ldap/login/{1}'.format(VAULT_URL, getpass.getuser()), json={'password': password})
    print(response)
    if response.status_code != 200:
        raise Exception('Please validate your credentials')
    json = response.json()
    print('Your token policies: {0}'.format(json['auth']['policies']))
    token = json['auth']['client_token']
    if token is None:
        raise Exception('Unable to retrieve a vault token: {0}'.format(response.text))
    return token

	
if __name__=="__main__":
	login()