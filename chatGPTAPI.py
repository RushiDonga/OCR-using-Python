import json
import openai


# Build the return response
def buildResponse(statusCode, body=None):
    
    response={
        'statusCode': statusCode,
        'headers':{
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    if body is not None:
        response['body'] = json.dumps(body)
        return response

def lambda_handler(event, context):
    print(event)
    
    medicineName = event["queryStringParameters"]["medicineName"]
    api_key = event['headers']['x-api-key']
    
    print("-----------")
    print(api_key)
    print(medicineName)

    # medicineName = body['medicine-name']
    # api_key = body['apiKey']

    openai.api_key=api_key

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Give me the Medicine Full Brand Name, Strength, Route, Drug Class, Drug Category and Manufacturer Name of the medicine brand named {medicineName}",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    data = response['choices'][0]['text']

    return buildResponse(
        200,
        {
            'Full Brand Name': data.split('\n')[2].split(':')[1],
            'Strength': data.split('\n')[3].split(':')[1],
            'Route': data.split('\n')[4].split(':')[1],
            'Drug Class': data.split('\n')[5].split(':')[1],
            'Drug Category': data.split('\n')[6].split(':')[1],
            'Manufacturer Name': data.split('\n')[7].split(':')[1]
        }
    )