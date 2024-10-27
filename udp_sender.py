from utils import UDP_Client
import encoder
import time
import socket
import select


if __name__ == "__main__":
    sender = UDP_Client("127.0.0.1",9988)
    flager = UDP_Client("127.0.0.1",9922)
    r, w, e = select.select([flager.sock], [sender.sock], [])
    file = "LICENSE"
    lteconder = encoder.LTEncoder(32,file)
    ## Processing File:
    f = open(file).read()
    for block in lteconder._gen_blocks(f):
    ## Processing Str
    # for block in lteconder._gen_blocks(test_str):
        sender.send(block, ("127.0.0.1",9987))
        # time.sleep(0.2)
        ready_to_read, _, _ = select.select([flager.sock], [], [], 0)

        if ready_to_read:
            # 接收客户端的响应
            data = flager.receive()
            response = data.decode('utf-8')

            if response == "Done":
                print("Transition done. Shutdown Tunnel.")
                break


