#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

from enum import Enum, unique


@unique
class EventType(Enum):
    HTTP_API = 1
    REST_API = 2
    WEBSOCKET = 3
    S3 = 4
    SQS = 5
    SNS = 6
    DYNAMODB = 7
    COGNITO = 8
    EVENT_BRIDGE = 9
    CLOUDWATCH_LOG = 10
    UNKNOWN = 11
