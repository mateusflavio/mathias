# -*- coding: utf-8 -*-
import logging
from django.conf import settings

logger = logging.getLogger()

import json

class LogManager:

    extra = {
        'bztoken': settings.BZTOKEN,
        'version': settings.VERSION,
        'environment': settings.ENVIRONMENT
    }

    @staticmethod
    def log(self, level, message):

        log = 'application log'
        if type(message) == dict:
            LogManager.extra['logging'] = message
        elif type(message) == str:
            log = message

        if level == logging.INFO:
            logger.info(log, extra=LogManager.extra)
        elif level == logging.ERROR:
            logger.error(log, extra=LogManager.extra)
        elif level == logging.DEBUG:
            logger.debug(log, extra=LogManager.extra)
        elif level == logging.WARNING:
            logger.warning(log, extra=LogManager.extra)
        elif level == logging.CRITICAL:
            logger.critical(log, extra=LogManager.extra)
