# manage.py
# this initializes the flask app to prepare the api configuration and logging

import unittest


from flask_script import Manager

from fastText import create_app

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('/data/logs/logs.log')
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)



app = create_app()
manager = Manager(app)





if __name__ == '__main__':
    manager.run()