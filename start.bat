@echo off
chcp 65001 >nul
title Leergut-Profi SLZ 2025 – Modular & Profi

echo.
echo       Leergut-Profi SLZ 2025 – Modular Edition
echo       (einmalig ca. 60 Sekunden)
echo.

python -m pip install --upgrade pip --quiet
python -m pip install streamlit pillow reportlab pandas --quiet

echo.
echo       App startet im Browser...
start "" http://localhost:8503

python -m streamlit run main.py --server.port=8503

pause