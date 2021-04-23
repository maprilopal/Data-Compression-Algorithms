# Data-Compression-Algorithms
Implementation of four data compression algorithm: 
1. Shannon (https://en.wikipedia.org/wiki/Shannon_coding), 
2. Shannon-Fano (https://en.wikipedia.org/wiki/Shannon–Fano_coding), 
3. LZ78 (https://en.wikipedia.org/wiki/LZ77_and_LZ78) and 
4. LZW (https://en.wikipedia.org/wiki/Lempel–Ziv–Welch). 
Every file have one class with one algorithm. All works on files.


* Shannon and Shannon-Fano

*To encode the text*
First argument is a path to a file, which text we want to encode. Second, is path to file where encoded text will be save. And the last is the file where all codes for every character will be save.

*To decode the text*
First argument is a path to a file, which text we want to decode. Second, is path to file where decoded text will be save. And the last is the file where all codes for every character are saved.


* LZ78 and LZW

*To encode the text*
Only two arguments. First is the path to a file we want to encode and second is the path to a file, where we want to save the encoded text.

*To decode the text*
Similary, the first is the path to a file with the encoded text and second is the path to a file, where we want to save the decoded text.
