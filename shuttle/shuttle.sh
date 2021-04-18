# sshuttle --method=ipfw -D -v 0\0
echo "----OPEN TCP PORTS ARE AS FOLLOWS----"
nmap -sT $1 | grep -e ^[0-9].*
printf "\n"
#nmap -A $1 | grep -e Potentially
#nmap -A --script=exploit -d 192.168.43.39
#nmap -A --script=intrusive -d 192.168.43.39
#nmap -A --osscan-guess --fuzzy --script=broadcast-ping -d $1
FLAGS="-I -T -U"
FILE="out"
for f in $FLAGS
do
    sudo traceroute "$f" -p 443 $1 -N 32 -t 8 > Treport.txt
    grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' Treport.txt > "${FILE}${f}.txt"
    python3 try.py "$f"
    rm Treport.txt
    uniq "${FILE}${f}.txt" > "${FILE}${f}1.txt"
    rm "${FILE}${f}.txt"
done
FILES="out-I1.txt out-T1.txt out-U1.txt"
for f in $FILES
do
    if [[ $f =~ "I" ]]; then
        COMMAND="--script ipidseq"
   elif [[ $f =~ "T" ]]; then
        COMMAND="-sT"
    else
        COMMAND="-sU"
    fi
    while read p; do
        VAR=$(nmap $COMMAND $p | grep -e ^[0-9].*)
        if [[ $VAR ]]; then
            echo "----OPEN PORTS OF $p ARE AS FOLLOWS ----"
            echo "${VAR}"
            printf "\n"
        else
            echo "NO OPEN PORTS FOUND FOR $p"
        fi
    done < "${f}"
done
#echo $(nmap -A --script=broadcast-ping -d $1 | grep -e "DNS server") > out.txt
#echo "IPv4 DNS Server of target is: $(grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' out.txt)"
#rm out.txt
#printf "\n"
#nmap -sC 192.168.43.39

#Do a whois query
#Use process.py
#Before that extract all
#info

printf "The upcoming or following scan is helpful: \n"
printf "Notice the output carefully \n"
nmap -p80 --script ipidseq -iR 1000 $1 > outputofscan.txt
echo "---END---"