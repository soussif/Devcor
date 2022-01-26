import requests
import urllib3
import json

urllib3.disable_warnings()

url = "https://sandbox-sdwan-1.cisco.com/"

headers = {"Content-Type": "application/x-www-urlencoded"}
credentials = {
    "j_username": "devnetuser",
    "j_password": "RG!_Yw919_83"
}
cookie_response = requests.post(url + "/j_security_check", headers=headers, data=credentials, verify=False)

device_response = requests.get(url + "/dataservice/device", cookie=cookie_response.cookies , verify=False)

if device_response.status_code == 200:
    json_list = json.loads(device_response.text)
else:
    if device_response.status_code == 403:
        err = 'Forbidden'
    elif device_response.status_code[0] == '4':
        err = 'Bad Request'
    elif device_response.status_code[0] == '5':
        err = 'Server Error'
    else:
        err = 'Unknown Error'
    print('Non-OK response returned, Status Code: {}, Error: {}'.format(str(device_response.status_code), err))
