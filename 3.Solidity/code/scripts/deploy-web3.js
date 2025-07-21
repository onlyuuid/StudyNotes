const fs = require("fs");
const {Web3} = require("web3");

// 读取编译产物                                  ./ 是相对node的工作目录，不是相对deploy-web3.js所在目录
const contractJson = JSON.parse(fs.readFileSync("./artifacts/contracts/HelloWorld.sol/HelloWorld.json", "utf-8")); 
const abi = contractJson.abi;
const bytecode = contractJson.bytecode;

// 本地节点地址
const providerUrl = "http://127.0.0.1:8545"; // 或 Infura 地址
const privateKey = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"; // ⚠️ 请用 Hardhat/Ganache 提供的测试私钥
const web3 = new Web3(providerUrl);

async function main() {
  const account = web3.eth.accounts.privateKeyToAccount(privateKey);
  web3.eth.accounts.wallet.add(account);

  const contract = new web3.eth.Contract(abi);

  console.log("准备部署合约...");
  const deployTx = contract.deploy({
    data: bytecode,
    // arguments: [] // 如果有构造函数参数，在这里填写
  });

  const gas = await deployTx.estimateGas();

  const result = await deployTx.send({
    from: account.address,
    gas,
  });

  console.log("合约部署成功！");
  console.log("地址：", result.options.address);
}

main().catch((err) => {
  console.error("部署失败：", err);
});
