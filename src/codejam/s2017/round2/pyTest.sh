#!/usr/bin/env bash

problemDir=$1'/'
problemSrc=$problemDir'source.py'
problemInputExamples=$problemDir'*.in'
problemOutputExamples=$problemDir'*.out'

for test in $problemInputExamples
do
	echo 'Testing '$(basename "$test")'...'
	filenamePath="${test%.*}"
	python3 $problemSrc < $filenamePath'.in' > $filenamePath'.outPy'
	diff -y --unidirectional-new-file --suppress-common-lines $filenamePath'.out' $filenamePath'.outPy'
done