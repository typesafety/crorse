from importlib import reload
import logging
from pprint import pprint

from bs4 import BeautifulSoup
import requests

# Show all logging levels in the shell
logging.basicConfig(level=logging.DEBUG)

import crorse.course
from crorse.course import Course, Domain
import crorse.scrape_api
from crorse.scrape_api import CanvasAPI, CanvasScrapeAPI

