#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

from enum import Enum, unique


@unique
class Deployment(Enum):
    DEPLOYMENT_IN_DIFFERENT_REGION = 1
    DEPLOYMENT_IN_SAME_REGION = 2


@unique
class ExecuteMode(Enum):
    LOCAL = "local_for_all"
    SQS = "local_for_sqs"
    AWS_LAMBDA = "local_for_aws_lambda"
