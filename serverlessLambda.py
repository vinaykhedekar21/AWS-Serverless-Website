
def lambda_handler(event, context):
    
    print(" Wow! Into my first Lambda function!")
    
    # TODO implement
    resp= {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Congrats! Vinay, You have created your first Lambda function"
    }
    
    return resp
