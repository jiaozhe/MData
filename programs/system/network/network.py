from loguru import logger
from pprint import pprint
from beeprint import pp
import psutil


cons = psutil.net_connections()
pprint(cons)
