#!/bin/bash

if [ $# -ne 2 ]; then
    echo "src and dest dirs missing"
    exit 1
fi

src_dir="$1"
dest_dir="$2"

#check if the src_dir exists
if [ ! -d "$src_dir" ]; then
    echo "$src_dir not found"
    exit 0
fi

#create the dest_dir if it doesn't exist
if [ ! -d "$dest_dir" ]; then
    mkdir -p "$dest_dir"
fi

permission() {
    local user_input
    echo -n "Move this file? (y/n): "
    read -r user_input
    if [ "$user_input" = "y" ] || [ "$user_input" = "Y" ]; then
        return 0
    else
        return 1
    fi
}

#move .c files in directories with <= 3
find "$src_dir" -type f -name "*.c" | while read -r src_file; do
    dest_file="$dest_dir/${src_file#$src_dir}"
    c_file_count=$(find "$(dirname "$src_file")" -maxdepth 1 -type f -name "*.c" | wc -l)
    if [ "$c_file_count" -le 3 ]; then
        mkdir -p "$(dirname "$dest_file")"
        mv "$src_file" "$dest_file"
        echo "File moved to: $dest_file"
    fi
done

#process directories with more than 3 .c files
for src_file in $(find "$src_dir" -type f -name "*.c" -exec dirname {} \; | uniq); do
    for c_file in "$src_file"/*.c; do
        dest_file="$dest_dir/${c_file#$src_dir}"   
        echo "Moving file: $c_file"
        if permission; then
            mkdir -p "$(dirname "$dest_file")"
            mv "$c_file" "$dest_file"
            echo "File moved to: $dest_file"
        else
            echo "File skipped: $c_file"
        fi
    done
done