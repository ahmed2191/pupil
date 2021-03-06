"""
Receive data from Pupil server broadcast over TCP
test script to see what the stream looks like
and for debugging  
"""
import zmq
 
#network setup
port = "5000"
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:"+port)
#filter by messages by stating string 'STRING'. '' receives all messages
socket.setsockopt(zmq.SUBSCRIBE, '')
 
while True:
    msg = socket.recv()

    items = msg.split("\n") 
    msg_type = items.pop(0)
    items = dict([i.split(':') for i in items[:-1] ])
    
    if msg_type == 'Pupil':
        try:
            print "norm_gaze:\t%s\napparent_pupil_size:\t%s" %(items['norm_gaze'], items['apparent_pupil_size'])
        except KeyError:
            pass
    else:
        # process non gaze position events from plugins here
        pass