// SPDX-License-Identifier: Apache-2.0
pragma solidity >=0.7.0 <0.9.0;
/// @title ISCC-REGISTRAR v1.2

interface IsccHub {
  function iscc_announce (string calldata _iscc, string calldata _url, string calldata _message) external returns (bool);
}

contract IsccRegistrar {

   address public hub;

   constructor(address _hub) {
      hub = _hub;
   }

   function iscc_declare(string calldata iscc, string calldata url, string calldata message) public returns (bool) {
      return IsccHub(hub).iscc_announce(iscc, url, message);
   }
}
