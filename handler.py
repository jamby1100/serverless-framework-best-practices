import json


def complete_order(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!!!!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def calculate_order(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!!!!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def complete_order(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!!!!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
