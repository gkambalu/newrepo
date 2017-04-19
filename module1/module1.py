'''
import logging
from logging import handlers
log=logging.getLogger('pytest-logs')
print logging.basicConfig(filename='example.log',level=logging.DEBUG)
log.debug('this is the first message goining in')


def  get_logger(module='pytest-logs'):
    log=logging.getLogger(module)
    formatter = logging.Formatter(fm, "%Y-%m-%d %H:%M:%S")
    fh = logging.handlers.RotatingFileHandler(module, mode='a',
                              maxBytes = 8*1024*10, backupCount = 100)
    fh.setFor
    return log/
'''
import time
print time.time()
dic = {'x':'y','a':'b','c':'d','e':'f','g':'h','i':'j','k':'l','m':'n'}
#print dic['x']
for x in dic.keys():
    print x, dic[x]

    

print time.time()
