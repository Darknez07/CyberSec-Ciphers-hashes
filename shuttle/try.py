import sys

try:
    small = sys.argv[1]
except:
    small = ""
if small == "-U":
    small = "UDP"
elif small == "-I":
    small = "ICMP"
elif small == "-T":
    small = "TCP"
ask = " " * 15 + "---LAYERS OF FIREWALL FOR {} PROTOCOL---".format(small) + " " * 15
output = open("Report.txt", "w+")
output.writelines(ask)
output.writelines("\n")
print(ask)
with open("Treport.txt", "r+") as f:
    count = 0
    for i in f.readlines():
        mid = i.replace("*", "").replace("ms", "").split("  ")
        mid[-1] = mid[-1].replace("\n", "")
        arr = []
        for n in mid:
            try:
                q = float(n)
            except:
                x = n.split(" ")
                x[-1] = x[-1][1:-1]
                arr.append(x[-1])
        if arr[-1] == "" or arr[-1].isalpha():
            continue
        count = count + 1
        add = "Layer-{} ".format(count) + " --> ".join(arr)
        print(add)
        output.writelines(add)
        output.writelines("\n")
ask = " " * 25 + "----DONE----" + " " * 25
print(ask)
output.writelines(ask)
output.writelines("\n")
output.close()
