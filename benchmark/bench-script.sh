#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <python_path> <script_path> <num_executions>" >&2
    exit 1
fi

PYTHON_PATH=$1
SCRIPT_PATH=$2
NUM_EXECUTIONS=$3

# Input validation
command -v "$PYTHON_PATH" >/dev/null 2>&1 || { echo "Error: Python path '$PYTHON_PATH' is not executable" >&2; exit 1; }
[ -f "$SCRIPT_PATH" ] || { echo "Error: Script '$SCRIPT_PATH' not found" >&2; exit 1; }
[[ "$NUM_EXECUTIONS" =~ ^[0-9]+$ ]] && [ "$NUM_EXECUTIONS" -ge 1 ] || { echo "Error: Number of executions must be a positive integer" >&2; exit 1; }

TOTAL_TIME=0
MAX_TIME=0
MIN_TIME=""

echo "Starting execution..."

for ((i=1; i<=NUM_EXECUTIONS; i++)); do
    START_TIME=$(date +%s%N)
    
    "$PYTHON_PATH" "$SCRIPT_PATH" >/dev/null 2>&1 || { echo -e "\nError: Python script failed with exit code $?" >&2; exit 1; }
    
    ELAPSED=$(( ($(date +%s%N) - START_TIME) / 1000000 ))
    
    TOTAL_TIME=$((TOTAL_TIME + ELAPSED))
    
    [ -z "$MIN_TIME" ] || [ "$ELAPSED" -lt "$MIN_TIME" ] && MIN_TIME=$ELAPSED
    [ "$ELAPSED" -gt "$MAX_TIME" ] && MAX_TIME=$ELAPSED
    
    PERCENT=$((i * 100 / NUM_EXECUTIONS))
    FILLED=$((PERCENT / 2))
    
    printf "\r[%-50s] %d%% Complete" "$(printf '#%.0s' $(seq 1 $FILLED))" "$PERCENT"
done

printf "\n\nExecution completed.\n\n"

AVG_TIME=$(echo "scale=9; $TOTAL_TIME / ($NUM_EXECUTIONS * 1000)" | bc)
MIN_TIME=$(echo "scale=9; $MIN_TIME / 10000" | bc)
MAX_TIME=$(echo "scale=9; $MAX_TIME / 10000" | bc)

echo "Performance Statistics over $NUM_EXECUTIONS runs:"
echo "----------------------------------------"
echo "Time (seconds):"
printf "  Average: %.9f\n" "$AVG_TIME"
printf "  Minimum: %.9f\n" "$MIN_TIME"
printf "  Maximum: %.9f\n" "$MAX_TIME"

