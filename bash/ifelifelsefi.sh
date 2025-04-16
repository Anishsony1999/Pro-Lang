#! /bin/bash

if [ ${1,,} = anish ]; then
    echo "Welcome Back Boss "
elif [ ${1,,} = help ]; then
    echo "You can use this script to check if a user is the boss"
else
    echo "You are not the boss"
fi

