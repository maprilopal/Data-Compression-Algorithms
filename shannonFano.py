import re


class ShannonFano:

    def __init__(self, textpath, encodepath, codespath):
        self.textpath = textpath
        self.encodepath = encodepath
        self.codespath = codespath


    def __shannonFanoIn(self, u, beg, end, p):
        for i in range(beg, end):
            sum1 = abs(sum(p[beg:i]) - sum(p[i:end]))
            sum2 = abs(sum(p[beg:i + 1]) - sum(p[i + 1:end]))
            if sum1 <= sum2:
                for j in range(beg, i):
                    u[j] += "0"
                for j in range(i, end):
                    u[j] += "1"
                if i - beg > 2:
                    self.__shannonFanoIn(u, beg, i, p)
                elif i - beg == 2:
                    u[beg] += "0"
                    u[i - 1] += "1"
                if end - i > 2:
                    self.__shannonFanoIn(u, i, end, p)
                elif end - i == 2:
                    u[i] += "0"
                    u[end - 1] += "1"
                break
        return u


    def shannonFano(self):
        try:
            f = open(self.textpath, "r", encoding="utf-8")
            text = re.sub('W+', ' ', f.read())
            f.close()
            freq = {}
            lent = len(text)
            for sign in text:
                if sign in freq:
                    freq[sign] += 1
                else:
                    freq[sign] = 1
            prob = {sign: fr / lent for sign, fr in freq.items()}
            p = dict(sorted(prob.items(), key=lambda item: item[1], reverse=True))
            u = ["" for i in range(len(p))]
            u = self.__shannonFanoIn(u, 0, len(p), list(p.values()))
            codes = dict(zip(p.keys(), u))
            encode = ""
            for sign in text:
                encode += codes[sign]
            try:
                fe = open(self.encodepath, "w")
                fe.write(encode)
                fe.close()
                try:
                    fcod = open(self.codespath, "w")
                    codeToWrite = []
                    for code in codes.keys():
                        codeToWrite.append(str(code) + " " + str(codes[code] + "\n"))
                    fcod.writelines(codeToWrite)
                except IOError:
                    print("File "+self.codespath+" not accessible")
            except IOError:
                print("File "+self.encodepath+" not accessible")
        except IOError:
            print("File" +self.textpath+" not accessible")


    def shannon_decode(self):
        try:
            f = open(self.textpath, "r", encoding="utf-8")
            text = f.read()
            f.close()
            try:
                fc = open(self.codespath, "r", encoding="utf-8")
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
                        fd = open(self.encodepath, "w")
                        fd.write(decode)
                        fd.close()
                    except IOError:
                        print("File "+self.encodepath+" not accessible")
                else:
                    print("File is not binary")
                    return -1
            except IOError:
                print("File "+self.encodepath+" not accessible")
        except IOError:
            print("File "+self.textpath+" not accessible")
