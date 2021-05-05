# lns-protobuf
This is a sandbox for [Google Protobuf](https://developers.google.com/protocol-buffers/docs/pythontutorial). This demo demonstrates sending alerts with common data as well as alert-specific data. And, the demo shows how the client can gracefully handle an alert that it has never seen before.

## Setup
First, install the protobuf compiler for your system:
1. On MacOS, run `brew install protobuf`
2. On Ubuntu, run `apt install protobuf-compiler`

Second, verify the version of the compiler:
```
protoc --version  # Ensure compiler version is 3+
```

Third, install the python requirements in your environment (venv, docker, etc.):
```
python -m pip install -r requirements.txt
```

## Compile .proto files
Use `protoc` command to compile the .proto files into usable python "headers" that can be imported into the runtime code. I put the correct commands into the Makefile:
```
make
```

## Run the demo
Open two terminals side-by-side and run these two commands in sequence.
1. In one terminal, run `python client.py`
2. In the other terminal, run `python lns.py`

Example output:

![Example output](https://github.com/matthewtrotter/lns-protobuf/blob/7b31fcda2684837cddb222896d33fac35a015585/example.png)