## What is this

This is a python implementation of **Luby Transform code**, which contains encode & decode procesdures. 
Encoder and Decoder are reconstructed based on [@Anrosent](https://github.com/anrosent/LT-code)'s implementation, many thanks!

~~It will be used in a future project(Haven't decided name yet), which relies on no internet but only camera device to receive data from one device to another.~~

## Progress

- [x] LT Encoder: Key function and logics are done and tested. 

- [x] LT Decoder: Kye function and logics are tested. Code need to be reconstructed though, maybe later.

- [ ] Protobuf supported. ~~This can be done in a very short time.~~ Maybe Tomorrow?


UDP test are done perfectly! The next step will be using Protobuf and reconstruct Decoder!


To be continued ...

## To use

See `udp_sender.py` ahd `udp_receiver.py` . Doc will be written some day in the futures.

### Details

For encoder, `prng.get_src_blocks()` will return `(blockseed, d, ix_samples)`, where blockseed stands for the encoding block seed(I don't know whether it is of any use in future but still keep it), `d` represents the number of block that use to do XOR operations in current encoding procedure, and `ix_samples` shows which indice of the block(s) is used to XOR.

For decoder, no need to know further details unless  encoding procedures are changed.
