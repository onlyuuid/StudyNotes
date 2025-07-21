const fs = require("fs");
const { Web3 } = require("web3");

// 合约信息
const contractAddress = "0x5FbDB2315678afecb367f032d93F642f64180aa3";

const json = JSON.parse(fs.readFileSync("./artifacts/contracts/HelloWorld.sol/HelloWorld.json", "utf8"));
const abi = json.abi;

// 区块链连接
const providerUrl = "http://127.0.0.1:8545";
const privateKey = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"; // ⚠️ 替换成你之前部署用的私钥
const web3 = new Web3(providerUrl);

// 初始化
const account = web3.eth.accounts.privateKeyToAccount(privateKey);
web3.eth.accounts.wallet.add(account);

// 创建合约实例
const contract = new web3.eth.Contract(abi, contractAddress);

async function main() {
  // 1. 调用 view 函数（读取 message）
  const message = await contract.methods.getGreeting().call();
  console.log("读取到的 message：", message);

  // 2. 调用 setMessage 修改状态（发起交易）
  console.log("开始调用 setMessage() 修改 message...");
  const tx = await contract.methods.setGreeting("大魔王").send({
    from: account.address,
    gas: 100000,
  });

  console.log("交易哈希：", tx.transactionHash);

  // 3. 再次读取
  const newMessage = await contract.methods.getGreeting().call();
  console.log("修改后的 message：", newMessage);
}

main().catch(console.error);
