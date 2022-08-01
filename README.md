# AES/CBC/PKCS5

# AES-256
256-bit AES encryption refers to the process of concealing plaintext data using the AES algorithm and an AES key length of 256 bits. In addition, 256 bits is the largest AES key length size, as well as its most mathematically complex. It is also the most difficult to crack.

# CBC
The Cipher Block Chaining (CBC) mode is a typical block cipher mode of operation using block cipher algorithm. In this version, we provide Data Encryption Standard (DES) and Advanced Encryption Standard (AES) processing ability, the cipherkey length for DES should be 64 bits, and 128/192/256 bits for AES.
In this, we use AES-256.

# PKCS5
To perform encryption with a block cipher in CBC mode the length of the input to be encrypted must be an exact multiple of the block length B in bytes. For  all AES variants the length of block is 16 bytes (128 bits). If the length of the data to be encrypted is not an exact multiple of B, it must be padded to make it so. After decrypting, the padding needs to be removed.
If the block length is B then add N padding bytes of value N to make the input length up to the next exact multiple of B. If the input length is already an exact multiple of B then add B bytes of value B. Thus padding of length N between one and B bytes is always added in an unambiguous manner. After decrypting, check that the last N bytes of the decrypted data all have value N with 1 < N ≤ B. If so, strip N bytes, otherwise throw a decryption error.

Examples of PKCS5 padding for block length B = 8:

3 bytes: FDFDFD           --> FDFDFD0505050505<br />
7 bytes: FDFDFDFDFDFDFD   --> FDFDFDFDFDFDFD01<br />
8 bytes: FDFDFDFDFDFDFDFD --> FDFDFDFDFDFDFDFD0808080808080808

