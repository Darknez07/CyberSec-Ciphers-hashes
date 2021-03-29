import English as E
import Transposition as T
import Files as F

def hack_transposition(message, quite=True):
    arr = dict()
    eng = E.English()
    key_ans=0
    dummy = tuple({0,0})
    for words in message:
        final = ""
        for key in range(1,len(words)):
            if not quite:
                print("Trying for key={}".format(key))
            ans = T.Transpose(key)
            check = ans.decrypt(words)
            res = eng.check_words([check])
            if res[0] > dummy[0]:
                key_ans = key
                final = check
            dummy = res
        arr[final] = key_ans
    return arr

def possible_ans():
    k = F.Files().use_files(11, True,filename='Notes.txt')
    mid = hack_transposition(k)
    ans = {i: 0 for i in set(mid.values())}
    for i in mid.values():
        ans[i] += 1
    inter = sorted(ans)
    fnames = []
    for i in inter[:3]:
        fnames.append('Ans '+str(i)+'.txt')
        middle = open('Ans '+str(i)+'.txt','w+')
        for j in k:
            middle.writelines(T.Transpose(i).decrypt(j)+'\n')
        middle.close()
    print("The best 3 answers are saved in:{}, {}, {}".format(fnames[0],fnames[1],fnames[2]))
