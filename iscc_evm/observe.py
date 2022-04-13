# -*- coding: utf-8 -*-
import json

from loguru import logger as log
import iscc_evm
from pprint import pp


def observe_hub():
    w3 = iscc_evm.w3_client()
    co = iscc_evm.get_live_contract_hub()
    event_filter = co.events.IsccDeclaration.createFilter(fromBlock=0)
    log.info("observe historic registration events")
    for event in event_filter.get_all_entries():
        log.info("event:")
        block = w3.eth.getBlock(event.blockNumber)
        # block = json.loads(w3.toJSON(block))
        # event = json.loads(w3.toJSON(event))
        pp(dict(block))
        pp(dict(event.args))
        pp(dict(event))
        # print(w3.eth.getBlock(event.blockNumber)["timestamp"])


if __name__ == "__main__":
    observe_hub()
