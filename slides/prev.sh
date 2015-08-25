#!/bin/bash
cd "$(dirname "$0")"
timestamp=$(date +%s)
echo $timestamp prev > slide_control.txt
