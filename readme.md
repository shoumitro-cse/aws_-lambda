## for python
https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html


## url invocation
https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html
https://docs.aws.amazon.com/apigateway/latest/developerguide/call-api-with-api-gateway-lambda-authorization.html
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html


## Lambda function and curl
```
import json

def lambda_handler(event, context):
    message = json.loads(event['body'])
    result = None
    action = message['action']
    
    if action == 'increment':
        result = message['number'] + 1

    #response = { 'event': str(event), 'context': str(dir(context)) }
    response = { 'result': result}

    return response
    
curl -X POST 'https://bhq5yn2flx6dsj6b7zfqbqfl7m0vbwyf.lambda-url.us-east-2.on.aws/' -H 'content-type: application/json' -d '{ "action": "increment", "number": 3 }'

curl -X POST 'https://bhq5yn2flx6dsj6b7zfqbqfl7m0vbwyf.lambda-url.us-east-2.on.aws/?action=increment&number=3' -H 'content-type: application/json' -d '{ "example": "test" }'

```
