#!/bin/bash
pip3 install -r requirements.txt || pip install -r requirements.txt
python3 src/main.py $1 || python src/main.py $1 || py src/main.py $1