
import logging

# debug < info < warning < error < critical - log error's levels
logging.basicConfig(level=logging.DEBUG, filename='app.log')

logging.warning('test')
logging.info('info')
logging.error('error')
logging.debug('debug')