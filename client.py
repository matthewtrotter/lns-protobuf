import lnsalerts2_pb2
from google.protobuf.any_pb2 import Any
import zmq

host = "127.0.0.1"
port = "5001"

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.SUB)

# Connects to a bound socket
socket.connect("tcp://{}:{}".format(host, port))

# Subscribes to all topics
socket.subscribe("")

while True:
    # Receive from socket
    alert_bin = socket.recv()

    # Parse into Alert type
    alert = lnsalerts2_pb2.Alert()
    alert.ParseFromString(alert_bin)

    print("RECEIVED:")
    print(alert)
    print(alert_bin)
    print()
    
    # Parse the details
    details_bin = Any()
    details_bin.CopyFrom(alert.details)
    try:
        if details_bin.Is(lnsalerts2_pb2.Alert.DESCRIPTOR):
            details = lnsalerts2_pb2.Alert()
        elif details_bin.Is(lnsalerts2_pb2.CertificateExpiredDetails.DESCRIPTOR):
            details = lnsalerts2_pb2.CertificateExpiredDetails()
        elif details_bin.Is(lnsalerts2_pb2.CertificateAlmostExpiredDetails.DESCRIPTOR):
            details = lnsalerts2_pb2.CertificateAlmostExpiredDetails()
        else:
            raise ValueError(f'Unknown alert type: {details_bin}')
        details_bin.Unpack(details)
    except ValueError as exc:
        print(exc)
        details = "Unknown - could not parse details"
    finally:
        print('Details:')
        print(details)
        print()



