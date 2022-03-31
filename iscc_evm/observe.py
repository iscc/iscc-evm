# -*- coding: utf-8 -*-
from loguru import logger as log
import iscc_evm
from pprint import pp


def observe_hub():
    co = iscc_evm.get_live_contract_hub()
    event_filter = co.events.IsccDeclaration.createFilter(fromBlock=0)
    log.info("observe historic registration events")
    for event in event_filter.get_all_entries():
        log.info("event:")
        pp(dict(event))


if __name__ == "__main__":
    observe_hub()
