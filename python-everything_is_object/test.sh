#!/bin/bash

while true; do
    # Prompt for the filename
    read -p "Enter the filename (or type 'exit' to quit): " filename

    # Exit the loop if the user types 'exit'
    if [[ "$filename" == "exit" ]]; then
        echo "Exiting the script."
        break
    fi

    # Check if the file already exists
    if [[ -e "$filename" ]]; then
        echo "Error: '$filename' already exists. Please choose a different name."
        continue
    fi

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

    echo "File '$filename' created, committed, and pushed successfully."
done

