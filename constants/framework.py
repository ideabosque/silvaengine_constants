#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

from enum import Enum, unique


@unique
class Framework(Enum):
    DEPLOYMENT_IN_DIFFERENT_REGION = 1
    DEPLOYMENT_IN_SAME_REGION = 2
