#!/bin/sh
killall python
#cd  telegram_market_reports/
cd telegram_market_reports/venv/bin/
activate
cd  telegram_market_reports/
python3 manage.py start_bot -st >> /root/telegram_market_reports/cronlog.txt 2>&1 &
