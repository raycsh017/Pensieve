# Bash Scripting Intro

## Basic Bash script structure

- Always include shebang (`#!`) at the first line of the script, without any spaces before (e.g. `#!/bin/bash`)
- Following the shebang needs to be the path to the interpreter that should be used to run the rest of the lines in the text file (for Bash scripts, it will be the path to Bash). You want to use an absolute path here, to ensure the script is reachable and runnable anywhere

## Variables

### Reading

Basic form follows this pattern `$variableName`

### Write

Basic form follows this pattern `variableName = value`

### Special variables

- `$0`: The name of the Bash script
- `$1` - `$9`: The first 9 arguments to the Bash script
- `$#`: How many arguments were passed to the Bash script
- `$@`: All the arguments supplied to the Bash script
- `$?`: The exit status of the most recently run process
- `$$`: The process ID of the current script
- `$USER`: The username of the user running the script
- `$HOSTNAME`: The hostname of the machine the script is running on
- `$SECONDS`: The number of seconds since the script was started
- `$RANDOM`: Returns a different random number each time it is referred to
- `$LINENO`: Returns the current line number in the Bash script

- ## 