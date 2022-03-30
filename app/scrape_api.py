"""API for scraping pages and creating Course objects."""

import logging

import requests
from requests import Response

from course import Course, Domain

logger = logging.getLogger(__name__)


class CanvasError(Exception):
    pass


class CanvasPageNotFound(CanvasError):
    pass


class CanvasAPI:
    """Higher-level API for getting information about Canvas courses."""
    pass
    # TODO: methods for creating Course objects etc.


class CanvasScrapeAPI:
    """Low-level API for performing Canvas scraping.

    Should usually not be called directly, use :class:`CanvasAPI` instead.
    """

    @classmethod
    def get_gu(cls, id: int) -> Response:
        url = f'{Domain.GU.value}/courses/{id}'
        return cls.get(url)

    @classmethod
    def get_chalmers(cls, id: int) -> Response:
        url = f'{Domain.CHALMERS.value}/courses/{id}'
        return cls.get(url)

    @classmethod
    def get(cls, url: str, headers=None) -> Response:
        return cls._http(url, 'GET', headers=headers)

    @classmethod
    def _http(cls, url: str, method: str, headers=None, data=None) -> Response:
        url = f'https://' + url.removeprefix('https://').removeprefix('http://')

        logger.debug('Making a request: %s %s %r %r', method, url, headers, data)
        resp = requests.request(method, url, headers=headers, data=data)

        if resp.status_code == 404:
            raise CanvasPageNotFound(f'Page at {url} could not be found')
        elif resp.status_code == 200:
            return resp
        else:
            raise CanvasError(f'Got unexpected HTTP response: {resp.content}')
