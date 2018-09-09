import zmq

LOCALHOST='127.0.0.1'
PORT='3000'

def open_and_get_socket():
    print "started server"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://' + LOCALHOST + ':' + PORT)

    return socket

