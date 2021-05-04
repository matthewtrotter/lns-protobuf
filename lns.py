

import lnsalerts2_pb2
from google.protobuf.any_pb2 import Any
import time
import zmq

######## Create alerts
# Generic alert without details
alert1 = lnsalerts2_pb2.Alert()
alert1.ownerid = 0
alert1.code = 1000
alert1.subcode = 13
alert1.message = f"Generic alert occured at time {time.time()}"
alert1_bin = alert1.SerializeToString()

# Certificate expired alert
details2 = lnsalerts2_pb2.CertificateExpiredDetails()
details2.pubkey = "ssh-ed25519 AAAAC3NzaC..."
details2.expirationtime = time.time() - 10000
details2_packed = Any()
details2_packed.Pack(details2)
alert2 = lnsalerts2_pb2.Alert()
alert2.ownerid = 0
alert2.code = 2000
alert2.subcode = 21
alert2.message = f"Certificate X expired at time {details2.expirationtime}"
alert2.details.CopyFrom(details2_packed)
alert2_bin = alert2.SerializeToString()

# Create publish socket
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5001")
time.sleep(1)

# Publish alerts
socket.send(alert1_bin)
print("SENT:")
print(alert1)
print(alert1_bin)
print()

socket.send(alert2_bin)
print("SENT:")
print(alert2)
print(alert2_bin)
print()

