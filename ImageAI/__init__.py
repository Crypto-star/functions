import logging
import openai
import azure.functions as func

secret_key = ''

# {"prompt":"Goku Running through a field", "n":1, "size":"1024x1024"}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give OpenAI our secret_key to authenticate

    openai.api_key = secret_key

    # get variables from the HTTP request body
    
    req_body = req.get_json()

    # call the OpenAI API

    output = openai.Image.create(
        prompt=req_body['prompt'],
        n=req_body['n'],
        size=req_body['size']
    )

    # format the response

    output_text=output['data'][0]['url']

    # provide the response

    return func.HttpResponse(output_text, status_code=200)
