from .selen import XPath, BrowserFactory
from pathlib import Path
import os

PKG = 'ABrowser'
PKG_PATH = Path().home() / f'.{PKG}'
DRIVER_PATH = PKG_PATH / 'drivers'
OPTIONS_PATH = PKG_PATH / 'options'
os.makedirs(DRIVER_PATH, exist_ok=True)
os.makedirs(OPTIONS_PATH, exist_ok=True)

from . import scripts
