# Loop through each file in the directory
for file in profiles/*.txt
do
  # Check if it's a regular file
  if [ -f "$file" ]
  then
    # Run the Python script with the file as an argument
    python3 main.py "$file"
    echo "Running $file"
  fi
done