#!/bin/sh
cd  telegram_market_reports/
source venv/bin/activate
python3 manage.py start_bot -st >> /root/telegram_market_reports/cronlog.txt 2>&1 &
