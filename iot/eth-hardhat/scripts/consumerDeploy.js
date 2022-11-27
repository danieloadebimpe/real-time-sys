const hre = require("hardhat");

async function main() {

  const Consumer = await hre.ethers.getContractFactory("Consumer");
  const consumer = await Consumer.deploy();

  await consumer.deployed();

  console.log("consumer contract deployed to:", consumer.address);

  saveFrontendFiles();
}

function saveFrontendFiles() {
  const fs = require("fs");

  const abiDir = __dirname + "/../rubix/src/abis";

  if(!fs.existsSync(abiDir)) {
    fs.mkdirSync(abiDir);
  }

  const artifact = artifacts.readArtifactSync("Consumer");


  fs.writeFileSync(
    abiDir + "/consumer.json",
    JSON.stringify(artifact, null, 2)
  );
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });