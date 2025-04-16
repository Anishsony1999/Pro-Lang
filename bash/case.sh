#! /bin/bash

case ${1,,} in
    anish | admin)
        echo "Welcome Boss"
        ;;
    help)
        echo "You can use this script to check if a user is the boss"
        ;;
    *)
        echo "You are not the boss"
        ;;
esac

