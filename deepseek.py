#!/usr/bin/env python
# coding=utf-8

"""
* @Author       : JIYONGFENG jiyongfeng@163.com
* @Date         : 2025-01-08 14:25:06
* @Description  :
* @LastEditTime : 2025-01-14 22:40:05
* @LastEditors  : JIYONGFENG jiyongfeng@163.com
* @Copyright (c) 2025 by ZEZEDATA Technology CO, LTD, All Rights Reserved.
"""

import logfire
from pydantic import BaseModel, Field
from config.config import settings
from datetime import datetime

logfire_write_token = settings.LOGFIRE_TOKEN

logfire.configure(token=logfire_write_token)
logfire.instrument_pydantic(record="failure")


# 定义一个模型
class Delivery(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]


# this will record details of a successful validation to logfire
m = Delivery(timestamp="2020-01-02T03:04:05Z", dimensions=["10", "20"])
print(repr(m.timestamp))
# > datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
# > (10, 20)

Delivery(timestamp="2020-01-02T03:04:05Z", dimensions=["10", "202"])
