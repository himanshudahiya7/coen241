#! /bin/bash

echo "Testing CPU"

max_prime = ("10000" "50000" "50000")
max_time = ("10" "30" "30")
threads = ("1" "1" "10")
run = 5
testcase = 3

for ((i=0; i<$testcase;i++))
do
	for (( j=1; j <=$run; j++ ))
	do
		echo "Testcase ${i+1} Run ${j}"
		sysbench cpu --threads=${threads[$i]} --cpu-max-prime=${max_prime[$i]} --time=${max_time[$i]} run
	done
done