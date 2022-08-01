"""ISCC - EVM Smart Contract Toolkit"""
import os
from loguru import logger as log
from platformdirs import PlatformDirs
from iscc_evm.settings import settings

__version__ = "0.1.4"
APP_NAME = "iscc-evm"
APP_AUTHOR = "iscc"
dirs = PlatformDirs(appname=APP_NAME, appauthor=APP_AUTHOR)
os.makedirs(dirs.user_data_dir, exist_ok=True)


log.debug(f"loaded settings: {settings}")
from iscc_evm.connection import *
from iscc_evm.deploy import *
