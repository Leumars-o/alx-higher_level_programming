#!/bin/bash
# bash script that sends a POST request to a url
curl -sd "email=test@gmail.com&&subject=I will always be here for PLD" -X POST "$1"
