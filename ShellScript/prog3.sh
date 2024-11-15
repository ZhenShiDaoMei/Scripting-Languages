#!/bin/bash

if [ "$#" -lt 1 ] || [ ! -f "$1" ]; then
    echo "missing data file"
    exit 1
fi

data_file="$1"
score_columns=$(head -1 $data_file | awk -F, '{print NF-1}')
weights=()
shift

#find weights
for (( i=1; i<=$score_columns; i++ )); do
    if [ "$1" ]; then
        weights+=($1)
        shift
    else
        weights+=(1)
    fi
done

weight_str=$(IFS=,; echo "${weights[*]}")

#get weighted average
awk -F, -v num_columns="$score_columns" -v weights="$weight_str" '
BEGIN { 
    total_weight = 0; total_score = 0; 
    split(weights, weight_array, ",");
}
{
    score = 0; weight = 0;
    for (i=2; i<=num_columns+1; i++) {
        w = weight_array[i-1];
        score += ($i * w);
        weight += w;
    }
    total_score += score;
    total_weight += weight;
}
END { 
    printf "%d\n", int(total_score / total_weight);
}
' "$data_file"