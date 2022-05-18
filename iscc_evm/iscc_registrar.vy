# @version ^0.3.3
"""
@title ISCC-REGISTRAR Contract v1.3
@notice Registrar contract for declaring ISCC-CODEs to claim unique ISCC-IDs.
@dev For further documentation see https://github.com/iscc/iscc-evm
"""

interface IsccHub:
    def announce(_iscc: String[96], _url: String[128], _message: String[128]): nonpayable

hub: public(address)
operator: public(address)

@external
def __init__(_hub: address):
    self.hub = _hub
    self.operator = msg.sender

@external
@payable
def declare(_iscc: String[96], _url: String[128], _message: String[128]):
    """
    @notice Announces an ISCC declaration to IsccHub to create/mint an ISCC-ID
    @param _iscc ISCC-CODE to be declared in standard base32 encoding (excluding the "ISCC:" prefix)
    @param _url Optional URL of declaration metadata (see: https://schema.iscc.codes)
    @param _message Optional protocol messaage (see: https://github.com/iscc/iscc-evm)
    """
    IsccHub(self.hub).announce(_iscc, _url, _message)

@external
def transfer(_to: address, _amount: uint256):
    """
    @notice Allow to transfer any income the contract may receive
    """
    assert msg.sender == self.operator
    assert self.balance >= _amount
    send(_to, _amount)
