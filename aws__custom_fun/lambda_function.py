import json
from custom import my_user

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': {
            'data': json.dumps('Hello from AWS Lambda!'),
            'user': my_user(),
            'event': str(event),
            'context': str(context)
        },
        'non_body': 'This data not available outside!'
    }
