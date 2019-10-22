import logging
import azure.functions as func

# Logging


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

# Variables

    num1 = req.params.get('int.num1')
    num2 = req.params.get('int.num2')
    num3 = 
    total = (num1+num2)


# Function

    if not num1:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            num1 = req_body.get('num1')

    if not num2:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            num2 = req_body.get('num2')

    if num1 & num2:
        return func.HttpResponse(f"{num1} - {num2} = {total}")
    else:
        return func.HttpResponse(
            "Addition Function - Enter two numbers labeled num1 and num2 on the query string or in the request body",
            status_code=400
        )
