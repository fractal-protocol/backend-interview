import json
import requests

from web3 import Web3


USER_ADDRESS = "0x9B974aF13ae64775E7E96fd92d9089b479cB57C5"

# USDC contract                     https://basescan.org/address/0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
# Metamorpho Spark USDC contract    https://basescan.org/address/0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A
USDC_ADDRESS             = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
# Metamorpho Spark USDC vault UI    https://app.morpho.org/base/vault/0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A/spark-usdc-vault
METAMORPHO_VAULT_ADDRESS = "0x7BfA7C4f149E7415b73bdeDfe609237e29CBF34A"


# Provider          https://web3py.readthedocs.io/en/stable/providers.html
# Contracts         https://web3py.readthedocs.io/en/stable/web3.contract.html
# Basic RPC methods https://web3py.readthedocs.io/en/stable/web3.eth.html
w3 = Web3(Web3.HTTPProvider("https://mainnet.base.org"))


with open("ierc20_abi.json", "r") as f:
    erc20_abi = json.load(f)
with open("ierc4626_abi.json", "r") as f:
    erc4626_abi = json.load(f)

# Creating contract instances
usdc_contract = w3.eth.contract(address=USDC_ADDRESS, abi=erc20_abi)
vault_contract = w3.eth.contract(address=METAMORPHO_VAULT_ADDRESS, abi=erc4626_abi)


def main():
    """
    """

    pass


if __name__ == "__main__":
    main()
