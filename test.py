from Handler.Handler import Handler

import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG)


handler = Handler()

handler.ExecuteBrightnessSensor()