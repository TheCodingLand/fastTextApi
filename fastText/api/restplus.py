import logging
import traceback
import os
from flask_restplus import Api

log = logging.getLogger(__name__)

log.setLevel(logging.WARNING)

api = Api(version='1.0', title='fastText Api',
          description='full python fastText implementation')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    app_settings = os.getenv('APP_SETTINGS')

    if not app_settings.FLASK_DEBUG:
        return {'message': message}, 500
