from classes.subscriber import *
from classes.event import *
import sys # to get cli args
import datetime
import logging
if len(sys.argv) == 3:
	esAddr = sys.argv[1]
	topic = sys.argv[2]
else:
	logging.debug( 'no arguments provided, resorting to defaults')
	esAddr = '127.0.0.1'
	topic = 'book'

#create a subscriber
s1 = Subscriber(esAddr)
# set the variables from the arguments passed
#subscribe to a topic
srvAddress = s1.lookup(topic)
s1.register(topic, srvAddress)
s1.subscribe(topic)


logger = logging.getLogger('subscribeLog')
hdlr = logging.FileHandler('subscribeLog.log',mode='w')
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

while True:
	msg = s1.socket.recv()
	logger.info('recieved: '+ msg)
