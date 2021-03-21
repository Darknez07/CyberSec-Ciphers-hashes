# !bin/bash
VAL=$(wc -l *.$1 | grep total)
if [[ $VAL ]]; then
    echo $VAL
else
    echo "Sorry! No files are present of that type"
fi