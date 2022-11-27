import ConsumerAbi from "../abis/consumer.json" 
import  config  from "../config";
import { ethers } from "ethers";

// create web3 instance to connect to Ethereum RPC interface 
// for both contracts

const provider = new ethers.providers.Web3Provider(window.ethereum);


// consumepi contract
const ConsumerAddress = config.consumerAddress;
const consumerABI = ConsumerAbi.abi;
const Consumer = new ethers.Contract(ConsumerAddress, consumerABI, provider.getSigner());



export { Consumer as Consumer_Contract};


