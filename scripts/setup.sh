#!/bin/bash

echo "Installing dependencies..."
python -m pip install -r requirements.txt

echo "Created and update .env file..."
cp -v example.env .env

echo "Run test program to check if everything is working..."
echo ""
echo ""
echo "python Buy-token.py gnosis USDT LINK 0.000001"
echo ""

