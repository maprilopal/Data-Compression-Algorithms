import numpy as np


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


def shannon(filepath, encodeTextpath, codepath):
    try:
        f = open(filepath, "r", encoding="utf-8")
        text = f.read()
        text = text.replace('\n', ' ')
        f.close()
        if len(text) > 0:
            freq = {}
            lent = len(text)
            for sign in text:
                if sign in freq:
                    freq[sign] += 1
                else:
                    freq[sign] = 1
            prob = {sign: fr / lent for sign, fr in freq.items()}
            prob = dict(sorted(prob.items(), key=lambda item: item[1], reverse=True))
            p = list(prob.values())
            letters = list(prob.keys())
            inv_p = [1 / prob[key] for key in prob.keys()]
            lengths = np.ceil(np.log2(inv_p))
            lengths = [int(i) for i in lengths]
            q = [sum(p[0:i]) for i in range(0, len(p))]
            codes = dict(zip(letters, map(fromDecToBin, q, lengths)))
            encodeText = ""
            for sign in text:
                encodeText += codes[sign]
            try:
                fct = open(encodeTextpath, "w")
                fct.write(encodeText)
                fct.close()
                try:
                    fcod = open(codepath, "w")
                    codeToWrite = []
                    for code in codes.keys():
                        codeToWrite.append(str(code) + " " + str(codes[code] + "\n"))
                    fcod.writelines(codeToWrite)
                    fcod.close()
                except IOError:
                    print("File " + codepath + " not accessible")
            except IOError:
                print("File "+encodeTextpath+" not accessible")
        else:
            print("File is empty")
            return -1
    except IOError:
        print("File "+filepath+" accessible")


def shannon_decode(filepath, codepath, decodepath):
    try:
        f = open(filepath, "r", encoding="utf-8")
        text = f.read()
        f.close()
        try:
            fc = open(codepath, "r", encoding="utf-8")
            codes = {}
            for line in fc:
                codes[line[2:-1]] = line[:1]
            fc.close()
            if sorted(list(set(text))) == ['0', '1']:
                word = text[0]
                decode = ""
                for i in range(1, len(text)):
                    word += text[i]
                    if word in codes.keys():
                        decode += codes[word]
                        word = ""
                try:
                    fd = open(decodepath, "w")
                    fd.write(decode)
                    fd.close()
                except IOError:
                    print("File "+decodepath+" not accessible")
            else:
                print("File is not binary")
                return -1
        except IOError:
            print("File "+codepath+" not accessible")
    except IOError:
        print("File "+filepath+" not accessible")
