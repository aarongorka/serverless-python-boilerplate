#!/usr/bin/env python3.6
import os
import logging
import aws_lambda_logging
import json

aws_lambda_logging.setup(level=os.environ.get('LOGLEVEL', 'INFO'), env=os.environ.get('ENV'))

def {{ cookiecutter.repo_name }}_handler(event, context):
    """Handler for {{ cookiecutter.repo_name }}"""

    aws_lambda_logging.setup(level=os.environ.get('LOGLEVEL', 'INFO'), env=os.environ.get('ENV'))
    aws_lambda_logging.setup(level=os.environ.get('LOGLEVEL', 'INFO'), env=os.environ.get('ENV'))
    logging.debug(json.dumps({'message': 'initialising'}))
    try:
        logging.debug(json.dumps({'message': 'logging event', 'status': 'success', 'event': event}))
    except:
        logging.exception(json.dumps({'message': 'logging event', 'status': 'failed'}))
        raise

    try:
        # do a thing
        thing = event
        logging.debug(json.dumps({'message': 'thing', 'status': 'success', 'thing': thing}))
    except:
        logging.exception(json.dumps({"message": "thing", "status": "failed"}))
        response = {
            "statusCode": 503,
            'headers': {
                'Content-Type': 'application/json',
            }
        }
        return response


    response = {
        "statusCode": 200,
        "body": thing
        'headers': {
            'Content-Type': 'application/json',
        }
    }
    logging.info(json.dumps({'message': 'responding', 'response': response}))
    return response
