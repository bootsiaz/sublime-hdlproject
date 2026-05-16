#!/bin/bash

# Get absolute path of the clicked .xpr file
FILEPATH="$(readlink -f "$1")"
DIRPATH="$(dirname "$FILEPATH")"

# Run the Sublime Text command with that path
subl --command "create_hdl_project_shell {\"project_file_path\" : \"$DIRPATH\"}"
