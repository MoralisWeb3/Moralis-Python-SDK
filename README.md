<div align="center">
    <a align="center" href="https://moralis.io" target="_blank">
      <img src="https://raw.githubusercontent.com/MoralisWeb3/Moralis-Python-SDK/main/assets/moralis-logo.svg" alt="Moralis JS SDK" height=200/>
    </a>
    <h1 align="center">Moralis Python SDK</h1>
    <a href="https://discord.gg/moralis" target="_blank">
      <img alt="Join the Moralis DAO on Discord" src="https://img.shields.io/discord/819584798443569182?color=7289DA&label=Discord&logo=discord&logoColor=ffffff">
    </a>
    <a href="https://docs.moralis.io" target="_blank">
      <img alt="Check the docs" src="https://img.shields.io/badge/Docs-Full Documentation-21BF96?style=flat&logo=gitbook&logoColor=ffffff">
    </a>
    <a href="https://forum.moralis.io" target="_blank">
      <img alt="Discourse posts" src="https://img.shields.io/discourse/posts?color=B7E803&label=Forum&logo=discourse&server=https%3A%2F%2Fforum.moralis.io">
    </a><br/>
    <img alt="npm" src="https://img.shields.io/pypi/v/moralis?label=version">
    <img src="https://img.shields.io/github/last-commit/MoralisWeb3/Moralis-Python-SDK">
  <p>
  </p>
  <p>
    A library that gives you access to the powerful Moralis Server backend from your Python app.
  </p>
  <br/>
</div>

**Features**:

- Web3 **authentication**
- Make **Evm api** and **Solana api** calls
- **Stream** realtime blockchain data

... and much more. Check the [official Moralis docs](https://docs.moralis.io/) for more details.

# 🚀 Quick start

If you're new to Moralis, check the [quickstart guide in the official docs](https://docs.moralis.io/moralis-dapp/getting-started) on how to get started.

If you're already familiar with Moralis and have your account registered. Then follow along to connect your SDK:

## 1. Install Moralis

```shell
pip install moralis
```

## 2. Call your methods

```python
from moralis import evm_api, auth

api_key = "YOUR_API_KEY"

path_params = {
  'address': '0xd8da6bf26964af9d7eed9e03e53415d37aa96045'
}

result = evm_api.balance.get_native_balance(
  api_key=api_key,
  path_params=path_params
)

print(result)
```

```python
from moralis import  auth

api_key = "YOUR_API_KEY"

body = {
  "timeout": 15,
  "domain": "moralis.io",
  "uri": "https://moralis.io",
  "chainId": "1",
  "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
}

result = auth.challenge.request_challenge_evm(
  api_key=api_key,
  body=body
)

print(result)
```

# ⭐️ Star us

If this JS SDK helps you build your dapps faster - please star this project, every star makes us very happy!

# 🤝 Need help

If you need help with setting up the boilerplate or have other questions - don't hesitate to write in our community forum and we will check asap. [Forum link](https://forum.moralis.io). The best thing about this SDK is the super active community ready to help at any time! We help each other.
