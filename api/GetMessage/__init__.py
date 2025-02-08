import logging

import azure.functions as func
from pathlib import Path


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    logging.info(f"{Path.cwd()}")
    message = Path("GetMessage/content.txt").read_text()
    return func.HttpResponse(message, status_code=200)
