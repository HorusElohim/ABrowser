from .selen import XPath, Chrome
from pathlib import Path
import os

PKG = 'ABrowser'
PKG_PATH = Path().home() / f'.{PKG}'
DRIVER_PATH = PKG_PATH / 'drivers'
os.makedirs(DRIVER_PATH, exist_ok=True)

from . import scripts
