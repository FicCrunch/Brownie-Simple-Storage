# Interacting with deployed contracts

from brownie import SimpleStorage, accounts, config


def read_contract():
    #  accessing the latest deployment
    simple_storage = SimpleStorage[-1]
    # abi
    # address
    print(simple_storage.retrieve())


def main():
    read_contract()
