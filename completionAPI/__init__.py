import logging
import openai
import azure.functions as func

secret_key = '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'

# {"model":"text-davinci-003", "prompt":"Slogan for a confectionery shop", "max_tokens":200, "temperature":0}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give OpenAI our secret_key to authenticate

    openai.api_key = secret_key

    # get variables from the HTTP request body
    
    req_body = req.get_json()

    # call the OpenAI API

    output = openai.Completion.create(
        model=req_body['model'],
        prompt=req_body['prompt'],
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature']
    )

    # format the response

    output_text=output['choices'][0]['text']

    # provide the response

    return func.HttpResponse(output_text, status_code=200)
