#!/bin/bash
# bashs script that displays all HTTP methods supported by the server
curl -sI "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
