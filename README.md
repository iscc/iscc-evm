# iscc-evm - EVM Smart Contracts for ISCC declarations

## Introduction

The purpose of decentralized [ISCC-CODE](https://core.iscc.codes/iscc_code/) declarations is to 
mint unique and short [ISCC-IDs](https://core.iscc.codes/iscc_id/) that are owned and controled 
by its declarers. ISCC-IDs connect **Actors** to **Digital Content** in a decentralized environment.

Actors are identified by their wallet addresses which they use to sign ISCC-CODE declarations
(ledger transactions). Digital Content is identified by ISCC-CODES. The ISCC-ID is derived from an
ISCC-CODE, a wallet address and the history of previous declarations. ISCC-IDs are globally unique,
short, persistent, authenticated, and resolve to at least exactly one ISCC-CODE and wallet address.
Optionaly ISCC-IDs can also be resolved to off-chain [ISCC metadata](https://schema.iscc.codes).
The ISCC-IDs are not required to be generated or stored on the participating ledgers themselves but
are the result of processing the history of transactions according to a **Minting Protocol**.

This repository implements the decentralized ISCC registry for Ethereum Virtual Machin (EVM) based
blockchains.

## The ISCC-REGISTRAR contract

An ISCC-REGISTRAR contract offers ISCC-CODE declarations to its users for claimig unique, short
and owned ISCC-IDs. To become an ISCC-REGISTRAR a contract must offer an `iscc_declare` method that
registers ISCC-CODEs by calling the `iscc_announce` method of the ISCC-HUB contract.

## The ISCC-HUB contract

The ISCC-HUB contract exposes the "iscc_announce" interface for other contracts to declare
ISCC-CODEs and emits `IsccDeclaration`-events.

The minimal input for an ISCC-CODE declaration is the ISCC-CODE itself. ISCC-CODE declarations 
are monitored by external observers that follow a deterministic protocol to mint unique, short 
and owned ISCC-IDs.

The resulting ISCC-ID of an ISCC-CODE declaration is owned by the signee of the original 
transaction (`tx.origin`) and not by the calling contract (`msg.sender`). ISCC-IDs are minted, 
indexed, and resolved off-chain by public ISCC-RESOLVERS.

The ISCC-HUB ensures that registration events can be monitored efficiently and always include the 
addreses of the DECLARER (tx.origin) and the REGISTRAR (msg.sender). It is recommended to 
also provide a URL where additional declaration information conforming to the ISCC metadata schema 
can be found (see: https://schema.iscc.codes/)

The `message`-field is reserved for protocol extensions.

# EVM Deployments

- ISCC-REGISTRAR v1.0 on [Rinkeby](https://rinkeby.etherscan.io/address/0x232BE91F5c4D8aAfe00557A1108c27D51db567B3)
- ISCC-HUB v1.0 on [Rinkeby](https://rinkeby.etherscan.io/address/0x485f167fb70dd73bc494ff76bb992d1ec8d6d2e4)

