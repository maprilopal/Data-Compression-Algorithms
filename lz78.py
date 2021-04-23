class LZ78:
    def __init__(self, textpath, encodepath):
        self.textpath = textpath
        self.encodepath = encodepath

    def __fromDecToBin(self, num, length, less0=True):
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


    def lz78(self):
        try:
            f = open(self.textpath, "r", encoding="utf-8")
            tex = f.read()
            f.close()
            if tex != "":
                tex = tex.lower()
                lenCode = 4
                alph = [" ", "e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p",
                        "b", "v", "k", "j", "x", "q", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                text = ""
                for sign in tex:
                    if sign in alph:
                        text += sign
                diction = {}
                for i in range(len(alph)):
                    diction[alph[i]] = self.__fromDecToBin(i + 1, lenCode, False)
                    if "0" not in diction[alph[i]]:
                        lenCode += 1
                t = ""
                for sign in text:
                    if sign in alph:
                        t += sign
                d = {}
                codes = []
                lenD = 1
                i = 0
                t1 = ""
                while i < len(text):
                    t2 = text[i]
                    if t1 + t2 not in d.keys():
                        if t1 == "":
                            d[t2] = lenD
                            codes.append([0, t2])
                        else:
                            codes.append([d[t1], t2])
                            d[t1 + t2] = lenD
                        lenD += 1
                        t1 = ""
                    else:
                        t1 = t1 + t2
                    i += 1
                output = ""
                n = 4
                for code in codes:
                    a = bin(code[0])[2:]
                    output += self.__fromDecToBin(len(a), n, False)
                    output += a
                    b = diction[code[1]]
                    output += self.__fromDecToBin(len(b), n, False)
                    output += b
                try:
                    fe = open(self.encodepath, "w")
                    fe.write(output)
                except IOError:
                    print("File "+self.encodepath + "not accessible")
        except IOError:
            print("File "+self.textpath+" not accessible")


    def lz78_decode(self):
        try:
            f = open(self.textpath, "r", encoding="utf-8")
            text = f.read()
            f.close()
            if sorted(list(set(text))) == ['0', '1']:
                lenCode = 4
                alph = [" ", "e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p",
                        "b", "v", "k", "j", "x", "q", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                diction = {}
                for i in range(len(alph)):
                    let = self.__fromDecToBin(i + 1, lenCode, False)
                    diction[let] = alph[i]
                    if "0" not in let:
                        lenCode += 1
                codes = []
                i = 4
                while i < len(text):
                    a = int(text[i-4:i], 2)
                    i += a
                    index = int(text[i-a:i], 2)
                    i += 4
                    b = int(text[i-4:i], 2)
                    i += b
                    letter = text[i-b:i]
                    codes.append([index, diction[letter]])
                    i += 4
                for code in codes:
                    if len(code) != 2:
                        print("Wrong text")
                        return -1
                d = {}
                output = ""
                for code in codes:
                    if code[0] == 0:
                        d[len(d)+1] = code[1]
                        output += code[1]
                    else:
                        output += d[code[0]]
                        output += code[1]
                        d[len(d)+1] = d[code[0]]+code[1]
                try:
                    fd = open(self.encodepath, "w")
                    fd.write(output)
                    fd.close()
                except IOError:
                    print("File "+self.encodepath+" not accessible")
            else:
                print("File is not binary")
                return -1
        except IOError:
            print("File " +self.textpath+" not accessible")
