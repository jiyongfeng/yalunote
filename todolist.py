#!/usr/bin/env python
# coding=utf-8

"""
* @Author       : JIYONGFENG jiyongfeng@163.com
* @Date         : 2025-01-14 18:17:18
* @Description  :
* @LastEditTime : 2025-01-15 13:58:33
* @LastEditors  : JIYONGFENG jiyongfeng@163.com
* @Copyright (c) 2025 by ZEZEDATA Technology CO, LTD, All Rights Reserved.
"""

import asyncio
import logging
import os
import time
from datetime import datetime

import requests
from pydantic import BaseModel, Field
from todoist_api_python.api import TodoistAPI
from todoist_api_python.api_async import TodoistAPIAsync
from typing_extensions import Annotated

from config.config import settings

# logging init,logfile to stdout and logs folder
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().addHandler(
    logging.FileHandler(f"logs/todolist_{time.strftime('%Y-%m-%d_%H-%M-%S')}.log")
)


TODOIST_TOKEN = settings.TODOIST_TOKEN


class TODOLIST_TASK(BaseModel):
    content: Annotated[str, Field(default="")]
    description: Annotated[str | None, Field(default="")]
    due_string: Annotated[str | None, Field(required=True, default="")]
    due_lang: Annotated[str | None, Field(min_length=2, max_length=2, default="en")]
    priority: Annotated[int | None, Field(ge=1, le=4, default=1)]
    labels: Annotated[list[str] | None, Field(default=[])]


# Fetch tasks asynchronously
async def get_tasks_async():
    api = TodoistAPIAsync(TODOIST_TOKEN)
    try:
        tasks = await api.get_tasks()
        logging.info(tasks)
    except Exception as error:
        logging.error(error)


# Fetch tasks synchronously
def get_tasks_sync():
    api = TodoistAPI(TODOIST_TOKEN)
    try:
        tasks = api.get_tasks()
        logging.info(tasks)
    except Exception as error:
        logging.error(error)


async def main():
    # 使用 await 来等待协程
    await get_tasks_async()
    # add_task()


# 如果是在同步环境中调用
if __name__ == "__main__":
    # 使用 asyncio.run() 来运行异步函数

    if not os.path.exists("logs"):
        os.makedirs("logs")
    logging.info("Starting todolist")
    # asyncio.run(main())
    api = TodoistAPI(TODOIST_TOKEN)
    try:
        todolist_task = TODOLIST_TASK(
            content="开发deepseek2todo",
            description="test",
            due_string="今天下午4点",
            due_lang="cn",
            priority=4,
            labels=["test", "dev"],
        )
        add_task = api.add_task(
            content=todolist_task.content,
            description=todolist_task.description,
            due_string=todolist_task.due_string,
            due_lang=todolist_task.due_lang,
            priority=todolist_task.priority,
            labels=todolist_task.labels,
        )
        logging.info(add_task)
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTPError: {e}")
        print(f"HTTPError: {e}")
    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"Error: {e}")
    logging.info("todolist finished")
