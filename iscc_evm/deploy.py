from pathlib import Path
from loguru import logger as log
import vyper
from iscc_evm.connection import w3_client


__all__ = [
    "compile_contract",
    "get_contract_hub",
    "get_contract_registrar",
    "deploy_hub",
    "deploy_registrar",
    "deploy",
    "SOURCE_FILE_HUB",
    "SOURCE_FILE_REGISTRAR",
]


HERE = Path(__file__)
SOURCE_FILE_HUB = HERE.parent / "iscc_hub.vy"
SOURCE_FILE_REGISTRAR = HERE.parent / "iscc_registrar.vy"
ENV = HERE.parent.parent / ".env"


def compile_contract(fp) -> dict:
    """Compile hub contract."""
    with open(fp, "rt") as infile:
        compiled = vyper.compile_code(infile.read(), ["abi", "bytecode"])
        log.debug(f"Compiled {fp}")
        return compiled


def get_contract_hub():
    """Build hub contract object."""
    return w3_client().eth.contract(**compile_contract(SOURCE_FILE_HUB))


def get_contract_registrar():
    """Build registrar contract object."""
    return w3_client().eth.contract(**compile_contract(SOURCE_FILE_REGISTRAR))


def deploy_hub(account=0):
    w3 = w3_client()
    w3.eth.defaultAccount = w3.eth.accounts[account]
    contract_obj = get_contract_hub()
    tx_hash = contract_obj.constructor().transact()
    address = w3.eth.getTransactionReceipt(tx_hash)["contractAddress"]
    log.debug(f"Hub contract deployed to {address}")
    return address


def deploy_registrar(hub=None, account=0):
    w3 = w3_client()
    w3.eth.defaultAccount = w3.eth.accounts[account]
    contract_obj = get_contract_registrar()
    tx_hash = contract_obj.constructor(hub).transact()
    address = w3.eth.getTransactionReceipt(tx_hash)["contractAddress"]
    log.debug(f"Registrar contract deployed to {address}")
    return address


def deploy(account=0):
    addr_hub = deploy_hub()
    addr_reg = deploy_registrar(hub=addr_hub)
    return addr_hub, addr_reg


if __name__ == "__main__":
    hub_addr = deploy_hub()
    reg_addr = deploy_registrar(hub=hub_addr)

    ENV.write_text(f'REGISTRAR_ADDRESS="{reg_addr}"\n' f'HUB_ADDRESS="{hub_addr}"')
