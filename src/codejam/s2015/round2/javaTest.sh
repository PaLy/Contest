#!/bin/sh
problemName=$1
problemDiff=$2
problemNo=$3
problemFileName=$problemName$problemDiff$problemNo
#className=$problemName$problemDiff$problemNo
problemDir='source/'
problemInputExamples=$problemDir$problemFileName'*.in'
problemOutputExamples=$problemDir$problemFileName'*.out'

for test in $problemInputExamples
do
	echo 'Testing '$(basename "$test")'...'
	filenamePath="${test%.*}"
	java -cp ../../../../out/production/Contest/ codejam.s2015.r2.$problemFileName < $test > $filenamePath'.outT'
	diff -y --unidirectional-new-file --suppress-common-lines $filenamePath'.outT' $filenamePath'.out'
done

