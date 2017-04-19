import logging
from logging.handlers import RotatingFileHandler
import sys
#sys.path.append('C:\proj1')
from module1 import addition
ret = -1

'''
log=logging.getLogger('proj1')
log.setLevel('INFO')
handle =  RotatingFileHandler('C:\proj1\module1\example.log', mode='a')
log.addHandler(handle)
log.info('this will not log')
#assert ret =' 1, log.info("this will log as an info message")
#raise AssertionError('failed', log.info('this is an assertion error'))
raise ValueError('Failed', log.info("this is a value error"))
log.error("this is an error which will be logged")
'''

'''

log2=logging.getLogger('proj1.mod1')
log2.setLevel('DEBUG')
handle2 =  RotatingFileHandler('C:\proj1\module1\example2.log', mode='a')
log2.addHandler(handle2)
log2.propagate = 1
log2.debug('this is my first debug message from child logger')
log2.debug('I do not want this to propogate:not propogated')
log2.info("this will log as an info message")
log2.error("this also should get logged")
'''

'''
log3=logging.getLogger('proj1.mod1.mod1_raw')
log3.setLevel('DEBUG')
handle3 =  RotatingFileHandler('C:\proj1\module1\example3.log', mode='a')
log3.addHandler(handle3)
log3.debug('I hope this will never propagate:from log3')
log3.debug('another message:I hope this will never propagate2:from log3')

log4=logging.getLogger('proj1.mod1.mod1_raw.log4')
log4.setLevel('DEBUG')
handle4 =  RotatingFileHandler('C:\proj1\module1\example4.log', mode='a')
log4.addHandler(handle4)
import pdb;pdb.set_trace()
log4.debug('I hope this has propagated to mod1_rawlog2:from log4')
log4.info('THis has also got propogated i know to mod1_raw:from log4')
'''
'''                                          
log2 = logging.getLogger('proj1.module1')

#logging.basicConfig(filename='C:\proj1\module1\example.log',level=logging.DEBUG)

log.debug('addtiion from module2 of proj1')
log.error('this is erorr log')
log2.info('will this propagate')
def addition(x,y):
    return x+y


if __name__== __name__:
    total=addition(3,4)
    log.debug('sum of given digits %d,%d is:%d',3,4,total)
    
'''


#################################################################

try:
    ret = addition("10.24.71.156", 23)
except Exception, e:
    import pdb;pdb.set_trace()
    print "inside Exception, caught:",e


print ret

    
