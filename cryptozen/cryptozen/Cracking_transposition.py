import cryptozen.English as E
import cryptozen.Transposition as T
from concurrent.futures import ThreadPoolExecutor

class Hack_transposition:
    def __init__(self, threshold=200):
        self.fnames = []
        self.threshold = threshold
        self.eng = E.English()

    def do_transpose_key(self, key, message):
        ans = T.Transpose(key)
        check = ans.decrypt(message)
        chunks = check.split('\n')
        res = [0, 0]
        with ThreadPoolExecutor(100) as ex:
            out = ex.map(self.eng.check_words, [[chunk] for chunk in chunks])
        for i in list(out):
            res[0]+=i[0]
            res[1]+=i[1]
        return res, check

    def hack_transposition(self, message, quite=True):
        arr = dict()
        key_ans = 0
        dummy = tuple({0, 0})
        if message == "":
            raise Exception("Message cannot be empty")
        for key in range(1, len(message)):
            final = None
            if not quite:
                print("Trying for key={}".format(key))
            res,check = self.do_transpose_key(key, message)
            # print(res)
            if res[0] > dummy[0] and res[0] > (1/len(message)):
                key_ans = key
                final = check
                dummy = res
            if final:
                arr[tuple(dummy)] = [final, key_ans]
            if key > self.threshold:
                break
        return arr


    def possible_ans(self, k: str):
        if k == "" or k is None:
            raise Exception("Empty string is not allowed")
        mid = self.hack_transposition(k)
        inter = sorted(mid.items(), key=lambda k:k[0])
        for i in inter[:5]:
            self.fnames.append("Ans " + str(i[1][1]) + ".txt")
            middle = open("Ans " + str(i[1][1]) + ".txt", "w+")
            middle.writelines(T.Transpose(i[1][1]).decrypt(k))
            middle.close()
        st = "The best "+str(len(self.fnames))+" answers are saved in:"
        for i in self.fnames:
            st+=str(i)
            st+=", "
        print(st[:-2])
