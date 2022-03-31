"""ISCC Declaration functions"""
from loguru import logger as log
import iscc_evm


def declare(iscc_code, url, account=0):
    ct = iscc_evm.get_live_contract_registrar(account=account)
    log.debug(f"Calling {ct.address}")
    log.debug(ct)

    tx_hash_digest = ct.functions.iscc_declare(iscc_code, url).transact()
    log.debug(f"ISCC declared (txid: {tx_hash_digest.hex()})")
    return tx_hash_digest.hex()


if __name__ == "__main__":
    declare(
        "KACT4EBWK27737D2AYCJRAL5Z36G76RFRMO4554RU26HZ4ORJGIVHDI",
        "ipfs://bafybeihcck6iocb2steuf4zwq53nfyce34xamke5za7gaq2qqoshmgab6u",
    )
