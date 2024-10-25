from utils import UDP_Client
import encoder
import time
import socket
import select


if __name__ == "__main__":
    sender = UDP_Client("127.0.0.1",9988)
    flager = UDP_Client("127.0.0.1",9922)
    r, w, e = select.select([flager.sock], [sender.sock], [])

    lteconder = encoder.LTEncoder(32)
    test_str = "This is an implementation of a Luby Transform code in Python, consisting of two executables, one for each encoding and decoding files. These are thin wrappers around a core stream/file API."
    for block in lteconder._gen_blocks(test_str):
        # pass
        # time.sleep(1)
        sender.send(block, ("127.0.0.1",9987))
        # # print("Succesfully send data.")

        # 尝试接收数据
        # if flager.sock in r:
        ready_to_read, _, _ = select.select([flager.sock], [], [], 0)
        
        if ready_to_read:
            # 接收客户端的响应
            data = flager.receive()
            response = data.decode('utf-8')

            if response == "Done":
                print("Transition done. Shutdown Tunnel.")
                break


