# Sell all token from your wallets

* Install python and pip on your system
  ```
  brew install python3 pip
  # OR
  sudo yum install python3 pip 
  ```

* Install all required packages 
  ```
  python -m pip install -r requirements.txt
  # Or
  pip3 install -r requirements.txt
  ```
  
* Copy "example.env" into ".env" and update your private and public keys
  ```
  cp -v example.env .env
  ls -lha .env
  ```
* Check whether you can buy using buy script (and your wallet details)
  ```
  python Buy-token.py gnosis USDT LINK 0.000001
  ```