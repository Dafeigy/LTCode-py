from utils import UDP_Client
import decoder
import struct

if __name__ == "__main__":
    receiver = UDP_Client("127.0.0.1",9987)
    dec = decoder.LtDecoder()
    while True:
        data = receiver.receive()

        for block in decoder.udp_read_blocks(data):
            finish_tag = dec.consume_block(block)
            if dec.is_done():
                print(f"Received file {dec.file_name}: ")
                break
        
        if finish_tag:
            print(dec.bytes_dump().decode())
            receiver.send("Done".encode(), ("127.0.0.1",9922))
            break

