from utils import UDP_Client
import encoder
import time


if __name__ == "__main__":
    sender = UDP_Client("127.0.0.1",9988)
    lteconder = encoder.LTEncoder(32)
    test_str = "This is an implementation of a Luby Transform code in Python, consisting of two executables, one for each encoding and decoding files. These are thin wrappers around a core stream/file API."
    for block in lteconder._gen_blocks(test_str):
        # pass
        # time.sleep(1)
        sender.send(block, ("127.0.0.1",9987))
        print("Succesfully send data.")


