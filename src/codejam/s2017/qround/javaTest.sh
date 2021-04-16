#!/bin/sh

SEASON='s2017'
ROUND='qround'

problemName=$1
sourceFileName='Source'
problemDir=${problemName}'/'
problemInputExamples=${problemDir}'*.in'
problemOutputExamples=${problemDir}'*.out'

for test in $problemInputExamples
do
	echo 'Testing '$(basename "$test")'...'
	filenamePath="${test%.*}"
	java -cp ../../../../out/production/Contest/ codejam.${SEASON}.${ROUND}.${problemName}.${sourceFileName} < ${test} > ${filenamePath}'.outJava'
	diff -y --unidirectional-new-file --suppress-common-lines ${filenamePath}'.outJava' ${filenamePath}'.out'
done

