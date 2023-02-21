#! /bin/bash

echo "Hey, you are in $0, and about to test fileio"

threads = ("2" "4" "8")
size = ("1G" "1G" "3G")
mode = ("rndwr" "seqrewr" "rndrw")
run = 5
testcase = 3

for ((i=0; i<$testcase;i++))
do
	echo "Testcase ${i+1}"
	for (( j=1; j <=$run; j++ ))
	do
		echo "Testcase ${i+1} Run ${j}"
		sysbench --threads=${threads[$i]} fileio --file-total-size=${size[$i]} --file-test-mode=${mode[i]} prepare
		sysbench --threads=${threads[$i]} fileio --file-total-size=${size[$i]} --file-test-mode=${mode[i]} run
		sysbench --threads=${threads[$i]} fileio --file-total-size=${size[$i]} --file-test-mode=${mode[i]} cleanup
	done
done