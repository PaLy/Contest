echo 'Testing ...'
filename=source/$1$2$3
python3 $filename'.py' < $filename'.in' > $filename'.outT'
diff -y --unidirectional-new-file --suppress-common-lines $filename'.out' $filename'.outT'

