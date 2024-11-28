# Graphing Tool

This tool will compare take the data that is outputed from both your profilers. It will then plot them in a graph. This works by either taking a average of all the poitns or taking just a specific run number.

This script will print out the numerical data for each function that ran while the profiling was happening. It will then open a tmux window and dispaly two graphs.

*NOTE: PLS RUN FROM THE SAME PLACE THIS README IS AS IT WONT WORK OTHERWISE*

## How to use

The folder `bash` will take care of running all the files pretty much and also running the profilers. 

### Run Profiler bash file
*NOTE: CHANGE THE NUMBER OF TIMES THE BASH FILE WILL RUN THE SCRIPTS AS IT CAN TAKE A WHILE DEPENDING ON HOW SLOW EACH PROFILER IS*.

This is just responsible for running the scripts a number of times and then saving the outputs of those runs to a .txt file (yes i know i could of used something better). This is set as a defualt at 20 runs of both profilers. *To have them save properly run the bash file from where this readme is and wehre the python files are.*

### Run All .bash file

This will just loop through every file in the directory calling the main.py function on them. The point of this function is just to store hte data in json I ahve not had a need for them as far but thought i would put them there.

### compareOneRun.bash

This will just take one of the files for both profilers depending on what number is assigned to `NUMBER` variable in the bash file. You cna change this to what ever you want.

### compareAverages.bash

This is the simple one to run you dont need to set variabels or anything just run the file and two graphs will open and data will print.