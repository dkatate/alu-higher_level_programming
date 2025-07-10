#!/bin/bash

# Prompt for the filename
read -p "Enter the filename: " filename

# Prompt for the file content
echo "Enter the content of the file (press Ctrl+D when done):"
content=$(cat)

# Create the file with the provided content
echo "$content" > "$filename"

# Make the file executable
chmod +x "$filename"

# Add the file to Git
git add "$filename"

# Commit with the first character of the filename as the message
git commit -m "${filename:0:1}"

# Push the changes
git push
