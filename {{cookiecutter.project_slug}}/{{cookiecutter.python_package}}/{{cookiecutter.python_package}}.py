#!/usr/bin/env python3.6
import os
import logging
import aws_lambda_logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
import json
import uuid
from dateutil.tz import tzlocal
from dateutil.tz import tzutc

patch_all()  # instrument libraries with xray

aws_lambda_logging.setup(level=os.environ.get('LOGLEVEL', 'INFO'), env=os.environ.get('ENV'))
logging.info(json.dumps({'message': 'initialising'}))
aws_lambda_logging.setup(level=os.environ.get('LOGLEVEL', 'INFO'), env=os.environ.get('ENV'))


def {{ cookiecutter.handler }}(event, context):
    """Handler for {{ cookiecutter.repo_name }}"""
    correlation_id = get_correlation_id(event=event)
    aws_lambda_logging.setup(level=os.environ.get('LOGLEVEL', 'INFO'), env=os.environ.get('ENV'), correlation_id=correlation_id)

    try:
        logging.debug(json.dumps({'message': 'logging event', 'event': event}))
    except:
        logging.exception(json.dumps({'message': 'logging event'}))
        raise

    try:
        # do a thing
        thing = event
        logging.debug(json.dumps({'message': 'thing', 'thing': thing}))
    except:
        logging.exception(json.dumps({"message": "thing"}))
        response = {
            "statusCode": 503,
            'headers': {
                'Content-Type': 'application/json',
            }
        }
        return response

    response = {
        "statusCode": 200,
        "body": json.dumps(thing),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
    logging.info(json.dumps({'message': 'responding', 'response': response}))
    return response


def get_correlation_id(body=None, payload=None, event=None):
    correlation_id = None
    if event:
        try:
            correlation_id = event['headers']['X-Amzn-Trace-Id'].split('=')[1]
        except:
            pass

    if body:
        try:
            correlation_id = body['trigger_id'][0]
        except:
            pass
    elif payload:
        try:
            correlation_id = payload['trigger_id']
        except:
            pass

    if correlation_id is None:
        correlation_id = str(uuid.uuid4())
    return correlation_id
