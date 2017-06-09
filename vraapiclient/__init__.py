#You should disable this in production
import requests
requests.packages.urllib3.disable_warnings() 

import log, os
# set up logging
logger = log.setup_custom_logger(source="console")
logger.info('My PID is: %d' %os.getpid())