#!/bin/bash

BASE_URL="https://jsonplaceholder.typicode.com"

echo "Rutas..."
wfuzz -c -w ../SecLists/Discovery/Web-Content/common.txt --sc 200,403 -u "$BASE_URL/FUZZ"  > JPH/rutes.txt

echo "Archivos comunes..."
wfuzz -c -w ../SecLists/Discovery/Web-Content/raft-large-files.txt --sc 200 "$BASE_URL/FUZZ" > JPH/docs.txt 


echo "Parámetros GET ocultos..."
wfuzz -c -z file,../SecLists/Discovery/Web-Content/burp-parameter-names.txt --sc 200 "$BASE_URL/posts?FUZZ=test" > JPH/parameters.txt


