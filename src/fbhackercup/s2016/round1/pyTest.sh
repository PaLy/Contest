#!/bin/sh
problemName=$1
problemDir=$problemName'/'
problemSrc=$problemDir$problemName'.py'
problemInputExamples=$problemDir'*.in'
problemOutputExamples=$problemDir'*.out'

for test in $problemInputExamples
do
	echo 'Testing '$(basename "$test")'...'
	filenamePath="${test%.*}"
	python3 $problemSrc < $filenamePath'.in' > $filenamePath'.outPy'
	diff -y --unidirectional-new-file --suppress-common-lines $filenamePath'.out' $filenamePath'.outPy'
done

