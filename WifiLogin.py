import argparse
import requests
from getpass import getpass

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help = 'enter the username', action = 'store')
#parser.add_argument('-p', '--password', help = 'enter the password', action = 'store')

cred = parser.parse_args()

password = getpass()

params = {'zone' : 'iiti_auth', 'auth_user' : cred.username, 'auth_pass' : password, 'accept' : 'Sign In'}

try:
    res = requests.post('https://fwiiti1.iiti.ac.in:8003/index.php?zone=iiti_auth', params)
except:
        print("Please check your network and try again!")
        exit(0)

if res.status_code == 200:
    if 'Invalid' in res.text:
        print("Could not sign in, check your login credentials and try again!")
    else :
        print("Successfully signed in!")
else :
    print("Unknown Error. \nCode: " +  str(res.status_code) + "\nResponse" + ": " + res.text)