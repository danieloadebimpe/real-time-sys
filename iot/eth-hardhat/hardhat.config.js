require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  defaultNetwork: 'goerli',
  networks: {
  goerli: {
    url: "wss://eth-goerli.g.alchemy.com/v2/eXe73McIzmxiVOaCe_dqK3Sf1XA7u9nc",
    accounts: ["3ad06e8f47109a8c0ec9b9ba8545a0150535c252bd41f2b6d367777009646df0"], 
  }
},
  solidity: {
    compilers: [
      {
        version: "0.8.10"
      },
      {
        version: "0.8.17"
      },
      {
        version: "0.6.0"
      }
    ]
  }

};
