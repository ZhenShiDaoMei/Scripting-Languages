#!/bin/bash

if [ $# -ne 2 ]; then
    echo "data file or output file not found"
    exit 1
fi

data_file="$1"
output_file="$2"

if [ ! -f "$data_file" ]; then
    echo "$data_file not found"
    exit 0
fi

>"$output_file"

#compute column sums and write to the output file
awk -F '[,;:]' '{
    for (i = 1; i <= NF; i++) {
        col_sum[i] += $i
    }
    if (NF > max_cols) {
        max_cols = NF
    }
}
END {
    for (i = 1; i <= max_cols; i++) {
        printf "Col %d : %d\n", i, col_sum[i]
    }
}' "$data_file" > "$output_file"