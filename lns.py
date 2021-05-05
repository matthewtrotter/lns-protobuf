

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
details2_packed.Pack(details2)  # Pack so that we can copy into the alert
alert2 = lnsalerts2_pb2.Alert()
alert2.ownerid = 0
alert2.code = 2000
alert2.subcode = 21
alert2.message = f"Certificate X expired at time {details2.expirationtime}"
alert2.details.CopyFrom(details2_packed)
alert2_bin = alert2.SerializeToString()

# Mux not responding alert
details3 = lnsalerts2_pb2.MuxsNotRespondingDetails()
details3.muxsid = "::-0"
details3_packed = Any()
details3_packed.Pack(details3)  # Pack so that we can copy into the alert
alert3 = lnsalerts2_pb2.Alert()
alert3.ownerid = 0
alert3.code = 3000
alert3.subcode = 6
alert3.message = f"Muxs {details3.muxsid} not responding."
alert3.details.CopyFrom(details3_packed)
alert3_bin = alert3.SerializeToString()


# Create publish socket
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5001")
time.sleep(1)

# Publish alerts
socket.send(alert1_bin)
print("SENT:")
print(alert1)
[print() for i in range(2)]

socket.send(alert2_bin)
print("SENT:")
print(alert2)
[print() for i in range(6)]

socket.send(alert3_bin)
print("SENT:")
print(alert3)
[print() for i in range(8)]

