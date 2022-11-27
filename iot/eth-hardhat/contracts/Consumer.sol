// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";


contract Consumer is ChainlinkClient {
    using Chainlink for Chainlink.Request;
  
    uint256 public data;
    
    address public oracle;
    bytes32 public jobId;
    uint256 public fee;

    address public owner;
    address public token;

    string public url;
    string public path;

    uint256 public totalValue;

    // eth rinkeby network (testnet) token address 
    address constant goerli_link = 0x326C977E6efc84E512bB9C30f76E30c160eD06FB;
    
    constructor() {
        // set the variables upon deployment

        // set to the Rinkeby Token Address
        setChainlinkToken(goerli_link);
        // set the contract owner to person deploying contract
        owner = msg.sender;
        // TestOracle Address
        oracle = 0x6884BD96B3DAaD051445d6396D805f6c2d993A7a;
        

        // direct request 
        jobId = "91862ed5536849e6bdd16bc540f2088f";

        // standard fee - .1 link
        fee = 0.1 * 10 ** 18; // (Varies by network and job)
    }


    // set the fee according to the job and network
    // gas fees for network 
    

    mapping(address => bool) public oracleAuth;
    mapping(bytes32 => bool) public jobAuth;
    mapping(string => bool) public urlAuth;
    mapping(string => bool) public pathExists;
    mapping(address => bool) public isOwner;
    // TO ADD : Multiple owners

    bytes32[] public jobs;
    address[] public oracles;
    string[] public urls;
    string[] public paths;
    address[] public owners;
    


    event OracleAdd(address _owner, address indexed _oracleAddress);
    event JobAdd(address _owner, bytes32 indexed _Job);
    event UrlAdd(address _owner, string indexed _url);
    event OwnerAdd(address _owner, address indexed _newOwner);
    event PathAdd(address _owner, string indexed _path);


    function addOwner(address _newOwner) public onlyOwner() {
        require(isOwner[_newOwner] = false, "owner already added");
        owners.push(_newOwner);

        emit OwnerAdd(msg.sender, _newOwner);

    }

    function addOracle(address _oracleAddr) public onlyOwner() {
        require(oracleAuth[_oracleAddr] == false, "Oracle already added");
        oracleAuth[_oracleAddr] = true;
        oracle = _oracleAddr;
        oracles.push(_oracleAddr);

        emit OracleAdd(msg.sender, _oracleAddr);

    }
    
    function addJob(bytes32 _jobId) public onlyOwner() {
        require(jobAuth[_jobId] == false, "Job already added");
        jobAuth[_jobId] = true;
        jobId = _jobId;
        jobs.push(_jobId);

        emit JobAdd(msg.sender, _jobId);
    }

    function addUrl(string memory _url) public onlyOwner() {
        require(urlAuth[_url] = false, "url already added");
        urlAuth[_url] = true;
        url = _url;
        urls.push(_url);

        emit UrlAdd(msg.sender, _url);
    }

    function addPath(string memory _path) public onlyOwner() {
        require(pathExists[_path] = false, "path already exists");
        pathExists[_path] = true;
        path = _path;
        paths.push(_path);

        emit PathAdd(msg.sender, _path);
    }


    function setOracle(address _oracleAddr) public onlyOwner() {
        require(oracleAuth[_oracleAddr] == true, "You have not added this oracle");
        oracle = _oracleAddr;
    }

    function setJob(bytes32 _jobId) public onlyOwner() {
        require(jobAuth[_jobId] == true, "You have not added this job");
        jobId = _jobId;
    }

    function setFee(uint256 _rate) public onlyOwner() {
        fee = _rate * 10 ** 18;
    }

    function getFee() public view returns(uint256) {
        return fee;
    }

    function getJob() public view returns(bytes32) {
        return jobId;
    }

    function getOracle() public view returns(address) {
        return oracle;
    }

    function getData() public view returns(uint) {
        return data;
    }

    function getOracles() public view returns (address[] memory) {
        return oracles;
    }

    function getjobs() public view returns (bytes32[] memory) {
        return jobs;
    }

    function getOwners() public view returns (address[] memory) {
        return owners;
    }

    function getPaths() public view returns (string[] memory) {
        return paths;
    }

    function getUrls() public view returns (string[] memory) {
        return urls;
    }

    

    function requestData() public returns (bytes32 requestId) 
    {
        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        
        // Set the URL to perform the GET request on
        request.add("weatherMetric", "temperature");

        int timesAmount = 10**18;
        request.addInt("times", timesAmount);
        
        // Sends the request
        return sendChainlinkRequestTo(oracle, request, fee);
    }


    function fulfill(bytes32 _requestId, uint256 _data) public recordChainlinkFulfillment(_requestId) {
        data = _data;
    }

    
    function withdrawLink(address payable _to, uint _amount) external onlyOwner() {
        require(_amount < totalValue, "amount exceeds");
        (bool sent, ) = _to.call{value: _amount}("");
        require(sent, "transaction failed");
    } 

    function depositLink() external payable {
        totalValue += msg.value;
    }
    

    modifier onlyOwner() {
        require(isOwner[msg.sender], "unauthorized");
        _;
    }

}