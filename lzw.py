def fromDecToBin(num, length, less0=True):
    code = ""
    if less0 == True:
        for i in range(1, length + 1):
            if num >= 1 / 2 ** i:
                code += "1"
                num -= 1 / 2 ** i
            else:
                code += "0"
    else:
        for i in range(length - 1, -1, -1):
            if num >= 2 ** i:
                code += "1"
                num -= 2 ** i
            else:
                code += "0"
    return code


def lzw(filePath, codeFilePath):
    try:
        f = open(filePath, "r", encoding="utf-8")
        text = f.read()
        f.close()
        if text != "":
            text = text.lower()
            alph = [" ", "e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p",
                    "b", "v", "k", "j", "x", "q", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            t = ""
            for sign in text:
                if sign in alph:
                    t += sign
            n = 4
            lenCode = 1
            d = {}
            for i in range(len(alph)):
                d[alph[i]] = fromDecToBin(i + 1, lenCode, False)
                if "0" not in d[alph[i]]:
                    lenCode += 1
            c = t[0]
            code = ""
            s = ""
            lenD = len(d)
            for i in range(1, len(t)):
                s += t[i]
                if c + s in d.keys():
                    c = c + s
                else:
                    code += fromDecToBin(len(d[c]), n, False)
                    code += d[c]
                    lenD += 1
                    d[c + s] = fromDecToBin(lenD, lenCode, False)
                    if "0" not in d[c + s]:
                        lenCode += 1
                    c = s
                s = ""
            code += fromDecToBin(len(d[t[-1]]), n, False)
            code += d[t[-1]]
            try:
                fc = open(codeFilePath, "w")
                fc.write(code)
                fc.close()
            except IOError:
                print("File "+codeFilePath+" accessible")

        else:
            print("File "+filePath+" is empty")
            return -1
    except IOError:
        print("File "+filePath+" not accessible")


def lzw_decode(filePath, decodeFilePath):
    try:
        f = open(filePath, "r")
        text = f.read()
        f.close()
        if text != "":
            if sorted(list(set(text))) == ['0', '1']:
                alph = [" ", "e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y",
                        "p", "b", "v", "k", "j", "x", "q", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                lenCode = 1
                d = {}
                for i in range(len(alph)):
                    n = fromDecToBin(i + 1, lenCode, False)
                    d[n] = alph[i]
                    if "0" not in n:
                        lenCode += 1
                n = 4
                lenD = len(d)
                lenWord = int(text[:n], 2)
                old = text[n: n+lenWord]
                decode = d[old]
                i = n + lenWord
                while i < len(text):
                    lenWord = int(text[i:i+n], 2)
                    code = text[i+n:i+n+lenWord]
                    sym = fromDecToBin(lenD + 1, lenCode, False)
                    if "0" not in sym:
                        lenCode += 1
                    if code in d.keys():
                        decode += d[code]
                        d[sym] = d[old] + d[code][0]
                        lenD += 1
                        old = code
                    else:
                        outStr = d[old] + d[old][0]
                        decode += outStr
                        d[sym] = outStr
                        lenD += 1
                        old = code
                    i += n+lenWord
                try:
                    fde = open(decodeFilePath, "w")
                    fde.write(decode)
                    fde.close()
                except IOError:
                    print("File " + decodeFilePath + " accessible")
            else:
                print("Error: File is not binary")
                return -1
        else:
            print("File "+filePath+" is empty")
            return -1
    except IOError:
        print("File "+filePath+" not accessible")
