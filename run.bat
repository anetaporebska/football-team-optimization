@ECHO OFF
pip3 install -r requirements.txt || pip install -r requirements.txt
python3 main.py $1 || python main.py $1 || py main.py $1