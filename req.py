# https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html

import requests

# my_fun
url = "https://lyreudii5qgfjhivcb4wnxw27m0vgyaa.lambda-url.us-east-2.on.aws/"

# another function
url = "https://bhq5yn2flx6dsj6b7zfqbqfl7m0vbwyf.lambda-url.us-east-2.on.aws/"

headers = {
    "type":"TOKEN",
    "authorizationToken":"allow",
    "methodArn":"arn:aws:lambda:us-east-2:544567456402:function:my_another_fun"
}

payload = {
	"action": "increment", 
	"number": 3
}

response = requests.request("GET", url, json=payload, headers=headers)
print(response.text)
