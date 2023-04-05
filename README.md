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
    <a href="https://pypi.org/project/moralis/"><img alt="pypi" src="https://img.shields.io/pypi/v/moralis?label=version"></a>
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

If you're new to Moralis, check the [quickstart guide in the official docs](https://docs.moralis.io/docs/quickstart) on how to get started.

If you're already familiar with Moralis and have your account registered. Then follow along to connect your SDK:

## 1. Install Moralis

```shell
pip install moralis
```

## 2. Call your methods

Import the correct module from the SDK and call the method you need. For a full reference of all the methods available, check the [references](#-references) section.

<!-- Start: generated:example-evm_api -->

```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x057Ec652A4F150f7FF94f089A38008f49a0DF88e", 
    "chain": "eth", 
    "to_block": 1.2, 
}

result = evm_api.balance.get_native_balance(
    api_key=api_key,
    params=params,
)

print(result)
```

<!-- End: generated:example-evm_api -->

# 🧭 Table of Contents

- [🚀 Quick start](#-quick-start)
  - [1. Install Moralis](#1-install-moralis)
  - [2. Call your methods](#2-call-your-methods)
- [🧭 Table of Contents](#-table-of-contents)
- [⭐️ Star us](#️-star-us)
- [🤝 Need help](#-need-help)
- [👀 Examples](#-examples)
- [📚 References](#-references)
  - [evm_api](#evm_api)
  - [sol_api](#sol_api)
  - [auth](#auth)
  - [streams](#streams)
- [🧙‍♂️ Community](#️-community)

# ⭐️ Star us

If this JS SDK helps you build your dapps faster - please star this project, every star makes us very happy!

# 🤝 Need help

If you need help with setting up the boilerplate or have other questions - don't hesitate to write in our community forum and we will check asap. [Forum link](https://forum.moralis.io). The best thing about this SDK is the super active community ready to help at any time! We help each other.

# 👀 Examples

**_Example getting native balance of an address via the EVM balance API_**

<!-- Start: generated:example-evm_api -->

```python
from moralis import evm_api

api_key = "YOUR_API_KEY"
params = {
    "address": "0x057Ec652A4F150f7FF94f089A38008f49a0DF88e", 
    "chain": "eth", 
    "to_block": 1.2, 
}

result = evm_api.balance.get_native_balance(
    api_key=api_key,
    params=params,
)

print(result)
```

<!-- End: generated:example-evm_api -->

**_Example getting native balance of an address via the SOL account API_**

<!-- Start: generated:example-sol_api -->

```python
from moralis import sol_api

api_key = "YOUR_API_KEY"
params = {
    "network": "", 
    "address": "", 
}

result = sol_api.account.balance(
    api_key=api_key,
    params=params,
)

print(result)
```

<!-- End: generated:example-sol_api -->

**_Example getting authentication message via the Auth API_**

<!-- Start: generated:example-auth -->

```python
from moralis import auth

api_key = "YOUR_API_KEY"
body = {
    "domain": "defi.finance", 
    "chainId": "1", 
    "address": "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B", 
    "statement": "Please confirm", 
    "uri": "https://defi.finance/", 
    "expirationTime": "2020-01-01T00:00:00.000Z", 
    "notBefore": "2020-01-01T00:00:00.000Z", 
    "resources": ['https://docs.moralis.io/'], 
    "timeout": 15, 
}

result = auth.challenge.request_challenge_evm(
    api_key=api_key,
    body=body,
)

print(result)
```

<!-- End: generated:example-auth -->

**_Example getting stream via the Streams API_**

<!-- Start: generated:example-streams -->

```python
from moralis import streams

api_key = "YOUR_API_KEY"
params = {
    "limit": 1.2, 
    "cursor": "", 
}

result = streams.evm_streams.get_streams(
    api_key=api_key,
    params=params,
)

print(result)
```

<!-- End: generated:example-streams -->

# 📚 References

For more info see [the live docs](https://moralisweb3.github.io/Moralis-Python-SDK/), or the [docs pages](./docs)

<!-- Start: generated:references -->

## evm_api

- [balance](./docs/evm_api/balance.md)
- [block](./docs/evm_api/block.md)
- [defi](./docs/evm_api/defi.md)
- [events](./docs/evm_api/events.md)
- [ipfs](./docs/evm_api/ipfs.md)
- [nft](./docs/evm_api/nft.md)
- [resolve](./docs/evm_api/resolve.md)
- [token](./docs/evm_api/token.md)
- [transaction](./docs/evm_api/transaction.md)
- [utils](./docs/evm_api/utils.md)

## sol_api

- [account](./docs/sol_api/account.md)
- [nft](./docs/sol_api/nft.md)
- [token](./docs/sol_api/token.md)

## auth

- [challenge](./docs/auth/challenge.md)

## streams

- [evm_streams](./docs/streams/evm_streams.md)
- [history](./docs/streams/history.md)
- [project](./docs/streams/project.md)
- [stats](./docs/streams/stats.md)



<!-- End: generated:references -->

# 🧙‍♂️ Community

- [Discord](https://discord.gg/moralis)
- [Forum](https://forum.moralis.io)
