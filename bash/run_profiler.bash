#!/bin/bash

# Define the number of times to run the command
TOTAL_RUNS=20 # adjust this to whatever you want. NOTE: This shit takes longgggg to run

# Command to be executed
COMMAND1="[your script]"
COMMAND2="[your script]"

# Loop to run the command multiple times
for (( i=1; i<=TOTAL_RUNS; i++ ))
do
    echo "Running iteration $i"
    # Execute the command and redirect the output to a file
    $COMMAND1 > "./profiles/[Your filename prefix]$i.txt"
    $COMMAND2 > "./profiles/[Your file name prefix]$i.txt"
done

echo "Completed $TOTAL_RUNS runs."