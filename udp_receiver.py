from utils import UDP_Client
import decoder
import struct

if __name__ == "__main__":
    receiver = UDP_Client("127.0.0.1",9987)
    dec = decoder.LtDecoder()
    while True:
        data = receiver.receive(("127.0.0.1",9987))
        # print(data)
        # header = struct.unpack("!III",data[:12])
        # block_data = int.from_bytes(data[12:], 'big')
        # print(header,block_data)
        # header = struct.unpack("!III")
        for block in decoder.udp_read_blocks(data):
            finish_tag = dec.consume_block(block)
            if dec.is_done():
                break
        if finish_tag:
            print(dec.bytes_dump())
            break
        
        # break

