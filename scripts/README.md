# Instructions to sell your tokens

* Open code repo into GitHub Codespaces, using your GitHub account.
* On terminal go to "scripts" folder.
* ``` cd scripts```
* ```cp -v example.env .env```
* Update your private and public key into .env file
* Run "Sell-token-file.py" with script, which will read list of tokens to sell into "USDC".
* Update your "list_of_tokens.csv"
* Make sure you have enough gas to pay the gas fees on selected blockchain
* Run: ```python Sell-token-file.py gnosis list_of_tokens.csv```
* In above commnad:
* Blockchian = gnosis
* list_of_tokens.csv = CSV (comma-separated values) file with list of all tokens to sell [more](https://en.wikipedia.org/wiki/Comma-separated_values)