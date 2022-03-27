# -*- coding: utf-8 -*-
import sys
from loguru import logger as log
import ipfshttpclient
from web3 import Web3
import iscc_evm


__all__ = [
    "w3_client",
    "get_live_contract_hub",
    "get_live_contract_registrar",
    "chain_name",
]

IPFS_CLIENT = None
W3_CLIENT = None
DB_CIENT = None
CHAINS = {
    1: "Ethereum mainnet",
    2: "Morden (disused), Expanse mainnet",
    3: "Ropsten",
    4: "Rinkeby",
    5: "Goerli",
    42: "Kovan",
    1337: "Geth private chains (default)",
}


def w3_client():
    """Return cached web3 connection."""
    global W3_CLIENT
    if not W3_CLIENT:
        W3_CLIENT = Web3(Web3.HTTPProvider(iscc_evm.settings.web3_address))
        if W3_CLIENT.isConnected():
            log.debug(
                f"Connected to {chain_name(W3_CLIENT)} via {iscc_evm.settings.web3_address}"
            )
        else:
            log.error("Connection failed")
            log.info(f"Connection failed to {iscc_evm.settings.web3_address}.")
            log.info("Make sure your ethereum node is running.")
            log.info("Set custom connection address via env var WEB3_ADDRESS.")
            sys.exit()
    return W3_CLIENT


def get_live_contract_registrar(addr=iscc_evm.settings.registrar_address, account=0):
    w3 = w3_client()
    w3.eth.defaultAccount = w3.eth.accounts[account]
    return w3.eth.contract(address=addr, abi=iscc_evm.compile_contract(iscc_evm.SOURCE_FILE_REGISTRAR)["abi"])


def get_live_contract_hub(addr=iscc_evm.settings.hub_address, account=0):
    w3 = w3_client()
    w3.eth.defaultAccount = w3.eth.accounts[account]
    return w3.eth.contract(address=addr, abi=iscc_evm.compile_contract(iscc_evm.SOURCE_FILE_HUB)["abi"])


def ipfs_client():
    """Return cached ipfs connection."""
    global IPFS_CLIENT
    if IPFS_CLIENT is None:
        ipfs_addr = iscc_evm.settings.ipfs_address
        try:
            IPFS_CLIENT = ipfshttpclient.connect(ipfs_addr)
        except Exception:
            log.error(f"IPFS connection to {ipfs_addr}")
            log.info(f"Connection failed to {ipfs_addr}.")
            log.info("Make sure IPFS is running.")
            log.info("Set custom connection address via env var IPFS_ADDRESS.")
            sys.exit()
    return IPFS_CLIENT


def chain_name(w3_client):
    """Return chain name"""
    return CHAINS[w3_client.eth.chainId]
