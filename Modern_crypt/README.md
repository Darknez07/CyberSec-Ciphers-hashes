AES
===

AES algorithm implementation using C.<br>
This can be used with different block sizes 192,256,128.
```
Just uncomment  the box with intial permutation
```

# Example

Compile the source code (e.g. using GCC):

`gcc gmult.c aes.c main.c -o aes`

## Sample run
bash
```
./aes
Enter the filename which has to be encrypted: sample.txt
Your plain text file has been loaded....
Plaintext message:
00 1c 3f 3c f0 44 38 39 43 f0 39 43 f0 44 35 48
Enter the filename the encrypted text has to be saved: lol.txt
Ciphered message:
b2 d4 0d 15 9c 85 28 d2 c5 35 71 fa 93 a2 bb e6
Your encrypted file has been successfully saved in lol.txt
Original message (after inv cipher):
00 1c 3f 3c f0 44 38 39 43 f0 39 43 f0 44 35 48
```