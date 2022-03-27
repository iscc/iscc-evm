# @version ^0.3.1
"""
@title ISCC-REGISTRAR Contract v1.0
@notice Registrar conract for declaring ISCC-CODEs to claim unique ISCC-IDs.
@dev For further documentation see https://github.com/iscc/iscc-evm
"""

interface IsccHub:
    def iscc_announce(_iscc: String[96], _url: String[128] = "", _data: Bytes[128] = b"") -> bool: payable

hub: public(address)

@external
def __init__(_hub: address):
    self.hub = _hub

@external
def iscc_declare(_iscc: String[96], _url: String[128] = "", _data: Bytes[128] = b"") -> bool:
    """
    @notice Announces an ISCC declaration to IsccHub to create/mint an ISCC-ID
    @param _iscc ISCC-CODE to be declared in standard base32 encoding (excluding the "ISCC:" prefix)
    @param _url An URL with declaration metadata (conforming to https://schema.iscc.codes/schema/)
    @param _type The type of declaration (0=declare, 1=declare-frozen, 2=update, 3=delete ...)
    """
    IsccHub(self.hub).iscc_announce(_iscc, _url, _data)
    return True
