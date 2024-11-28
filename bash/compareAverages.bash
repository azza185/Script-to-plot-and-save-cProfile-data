#!/bin/bash

# Define your commands
COMMAND1="python3 graph_average.py -d profiles/ -fp [The prefix of your filename]"
COMMAND2="python3 graph_average.py -d profiles/ -fp [The prefix of your filename]"

# Create a new tmux session named "my_session"
SESSION_NAME="my_session"
tmux new-session -d -s $SESSION_NAME

# Run COMMAND1 in the first pane
tmux send-keys -t $SESSION_NAME:0.0 "$COMMAND1" Enter

# Split the tmux window horizontally
tmux split-window -h -t $SESSION_NAME:0

# Run COMMAND2 in the new pane
tmux send-keys -t $SESSION_NAME:0.1 "$COMMAND2" Enter

# Attach to the tmux session
tmux attach -t $SESSION_NAME

