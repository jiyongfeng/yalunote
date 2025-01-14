#!/usr/bin/env python
# coding=utf-8

"""
* @Author       : JIYONGFENG jiyongfeng@163.com
* @Date         : 2025-01-14 16:59:45
* @Description  :
* @LastEditTime : 2025-01-14 17:51:03
* @LastEditors  : JIYONGFENG jiyongfeng@163.com
* @Copyright (c) 2025 by ZEZEDATA Technology CO, LTD, All Rights Reserved.
"""

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["config/settings.toml", "config/.secrets.toml"],
    env_switcher="ENV_FOR_DYNACONF",
    env_switcher_prefix="ENV_FOR_DYNACONF_",
    environment=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
