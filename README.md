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
and owned ISCC-IDs. To become an ISCC-REGISTRAR a contract must offer an `declare` method that
registers ISCC-CODEs by calling the `announce` method of the ISCC-HUB contract.

## The ISCC-HUB contract

The ISCC-HUB contract exposes the `announce` interface for other contracts to declare
ISCC-CODEs and emits `IsccDeclaration`-events.

Call Signature: `announce(_iscc: String[96], _url: String[128], _message: String[128])`

**\_iscc**: The minimal input to the `announce` method is the ISCC-CODE itself (in canonical base32
uppercase encoding with the `ISCC:`-prefix removed).

**\_url**: Optionally you can provide a URL that points to off-chain JSON-LD metadata about the
registered digital content. The schema of the metadata must conform to the ISCC metadata schema 
(see https://schema.iscc.codes) to be interpreted, indexed and resolved by an ISCC MetaRegistry.
Idealy the URL should use content based addressing (e.g. IPFS).

**\_message**: The `message`-field can be empty and is reserved for protocol extensions. If you
want to make sure that an ISCC declartion stays immutable and does not support any future protocol 
extensions (updates, transfers, deletes) you can pass in the processing instruction "frz:"

ISCC-CODE declarations are monitored by external observers that follow a deterministic protocol to
mint unique, short and owned ISCC-IDs.

The resulting ISCC-ID of an ISCC-CODE declaration is owned/controlled by the signee of the original 
transaction (`tx.origin`) and not by the calling contract (`msg.sender`). ISCC-IDs are minted, 
indexed, and resolved off-chain by public ISCC MetaRegistries .

The ISCC-HUB ensures that registration events can be monitored efficiently and always include the 
addreses of the DECLARER (tx.origin) and the REGISTRAR (msg.sender). It is recommended to 
also provide a URL where additional declaration information conforming to the ISCC metadata schema 
can be found (see: https://schema.iscc.codes/)



# Mainnet Live Contracts

ISCC announcement from ISCC-REGISTRARs to these ISCC-HUB contracts will register live ISCC-IDs
on ISCC MetaRegistries:

- ISCC-HUB v1.4 on **Ethereum**: https://etherscan.io/address/0x02F883581225e8eE144E73DfFd17DCbde1A453E7
- ISCC-HUB v1.4 on **Polygon**: https://polygonscan.com/address/0xA03881b52bCC908be7eF56Bf45584Dd4eF38e31D

# EVM Testnet Deployments

ISCC declarations on the latest testnet versions will show up on https://testnet.iscc.id

## Latest Testnet Version
- Demo ISCC-HUB v1.4 on Sepolia (Ethereum) https://sepolia.etherscan.io/address/0xa03881b52bcc908be7ef56bf45584dd4ef38e31d
- Demo ISCC-HUB v1.4 on Mumbai (Polygon) https://mumbai.polygonscan.com/address/0x4301ef777ccd080e3780789e2908bf8a0ae9899e

## Previous Testnet Deployments
- Demo ISCC-HUB v1.4 on Goerli (Ethereum) https://goerli.etherscan.io/address/0xa03881b52bcc908be7ef56bf45584dd4ef38e31d
- Demo ISCC-REGISTRAR v1.3 Solidity on Goerli https://goerli.etherscan.io/address/0x4e016d1f09a182e8981ee19fabc8e45d365e5d22
- Demo ISCC-HUB v1.4 on Rinkeby (Ethereum) https://rinkeby.etherscan.io/address/0xaA7AAD99075da1c2D206fCa08fE991C4611B1b04
- Demo ISCC-HUB v1.3 Vyper on Rinkeby https://rinkeby.etherscan.io/address/0x6E0B3E8a182a812b3cCa3C4F13E848bB389C3277
- Demo ISCC-HUB v1.3 Vyper on Mumbai https://mumbai.polygonscan.com/address/0x70aA323a88A9847231D1CdeE43A84c01f479A5BD
- Demo ISCC-REGISTRAR v1.3 Solidity on Rinkeby https://rinkeby.etherscan.io/address/0xd693ec9cd9850887e18246e12e64aff1a59b4ae6

- Demo ISCC-REGISTRAR v1.2 Vyper on Rinkeby https://rinkeby.etherscan.io/address/0x6cFD889219abc3Dc4FdB441e37C5C0eBAB4EDE59
- Demo ISCC-REGISTRAR v1.2 Solidity on Rinkeby https://rinkeby.etherscan.io/address/0xfde3ec229f47a76ec8b957c2d892aaf2314371d3
- Demo  ISCC-HUB v1.2 Vyper on Rinkeby https://rinkeby.etherscan.io/address/0x7956c3b659776015670277E0A6809Bf8ae5a257F
