from bs4 import BeautifulSoup
import requests
import json
import time


fc_username = 'xiyonis536@runfons.com'
fc_password = 'throwaway1234'


fc_payload = {'user': fc_username, 'password': fc_password}

with requests.Session() as session:
    post = session.post('https://www.freecycle.org/login', data=fc_payload)
    r = session.get('https://www.freecycle.org/home/my-towns')
    print(r.text)



# I could not get this to work

# username = 'johndoe123422'
# password = 'Throwaway1234'

# header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

# with requests.Session() as session:
#     get_token = session.get('https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/', headers=header)
#     soup = BeautifulSoup(get_token.content, 'html.parser')
#     token = soup.find('input', {'name': '_token'})['value']
#     payload = {'_username': username, '_password': password,'login': '', '_target_path': 'https://www.chess.com/', '_token': token}
#     print(token)
    
#     login = session.post('https://www.chess.com/login_check', data=payload, headers=header)
#     print(login.status_code)

    # dash = session.get('https://www.chess.com/settings', headers=header )
    # dash_soup = BeautifulSoup(dash.content, 'html.parser')
    # print(dash_soup.prettify())