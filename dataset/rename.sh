#!/bin/bash
python3 rename.py
cd images/validation
pwd
mogrify *.png
cd ../testing
pwd
mogrify *.png
cd ../training
pwd
mogrify *.png
