# Data-Compression-Algorithms
Implementation of four data compression algorithm: Shannon (https://en.wikipedia.org/wiki/Shannon_coding), Shannon-Fano (https://en.wikipedia.org/wiki/Shannon–Fano_coding), LZ78 (https://en.wikipedia.org/wiki/LZ77_and_LZ78) and LZW (https://en.wikipedia.org/wiki/Lempel–Ziv–Welch). Every file have one class with one algorithm. All works on files.


1. Shannon and Shannon-Fano
**To encode the text**
First argument is a path to a file, which text we want to encode. Second, is path to file where encoded text will be save. And the last is the file where all codes for every character will be save.
**To decode the text**
First argument is a path to a file, which text we want to decode. Second, is path to file where decoded text will be save. And the last is the file where all codes for every character are saved.

2. LZ78 and LZW
**To encode the text**
Only two arguments. First is the path to a file we want to encode and second is the path to a file, where we want to save the encoded text.
**To decode the text**
Similary, the first is the path to a file with the encoded text and second is the path to a file, where we want to save the decoded text.
