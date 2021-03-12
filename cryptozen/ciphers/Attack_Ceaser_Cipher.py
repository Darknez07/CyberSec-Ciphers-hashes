import Ceaser_Cipher as Cs
rev = Cs.createkey()    
text = 'Xqp whh ahoa kb pda sknhz swo ejreoexha.'.upper()
for j in range(26):
    s = ""
    for i in text:
        if i.isalnum():
            s += rev[1][(rev[0][i] + j) % 26]
        else:
            s += " "
    print(s)

# One string which is simple english so only look at 26 encryptions.