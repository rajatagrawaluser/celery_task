#!/bin/sh

echo celery task
apt update
apt install build-essential -y
pip install --no-cache-dir -r requirements.txt
ls -la
python setup.py build_ext --inplace
# python app/worker.py
sleep 1d