
<div align="center">

# **WOOF AI** <!-- omit in toc -->

### Bridging Pet Tech and Blockchain Innovation <!-- omit in toc -->
![hero](./asset/offline.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

#  Introduction

“WOOF” is the expression of a dog’s bark. We are developing an AI project designed to analyze and mimic canine behavior. By collecting dog barks uploaded by users, we aim to build a large-scale model to analyze dogs emotions and predict their behaviors, fostering a closer emotional bond between humans and dogs. We hope to encourage people around the world to form deeper connections with dogs. In the future, we look forward to expanding Woof AI's capabilities to provide more personalized interactions, enhance pet care, and revolutionize how we communicate with our furry companions. Woof woof!

# Core Algorithm
- Audio Feature Extraction: VGGish + STFT - Initially, the VGGish model is used to extract features from audio data.
- Audio Classification: Audio Spectrogram Transformer (AST) - AST is a Transformer model specifically designed for audio data, utilizing self-attention mechanisms to process spectrograms.
- Sound Event Classification: Our method to differentiate “non-dog bark” sounds uses a dual contrastive learning strategy. This involves a “negative sample provisioning” approach where we select and strengthen learning on sounds that could be mistaken for dog barks, thus improving the model’s ability to discriminate between different sounds.

# Model Performance Comparison

<img width="416" alt="image" src="https://github.com/user-attachments/assets/a25d4cc0-bbca-4f74-b587-852a706e800e">

# Miner and Validator Functionality

This tutorial shows how to  run incentives on it using the our testnet.
**important**.
- Do not expose your private key.
- Use only your testnet wallet.
- Do not reuse your mainnet wallet password.
- Make sure your incentives are resistant to abuse.

## Prerequisites

Before proceeding, make sure you have Bittensor installed. see the following instructions:

- [Install `bittensor`](https://github.com/opentensor/bittensor#install).

After installing `bittensor`, proceed as follows:

## 1. Install the Bittensor subnet template

**Note: Skip this step if** you have already performed it for local testing and development.

``cd`'' Go to your project directory and clone the bittensor-subnet-template repository:

``bash
git clone https://github.com/Woof-AI/WOOFAI_Subnet.git
```

Next, `cd` into the WOOFAI_Subnet

``bash

```bash
python -m pip install -e . 
```

## 2. Create wallets

Create wallets for subnet owners, subnet verifiers, and subnet miners.

This step creates local cold and hot key pairs for three identities: subnet owner, subnet verifier, and subnet miner.

The owner will create and control the subnet. The owner must have at least 100 testnet TAOs to run the subsequent steps.

Validators and miners will be registered to the subnet created by the owner. This ensures that validators and miners can run their respective validator and miner scripts.

Create a cold key for your owner's wallet:

```bash
btcli wallet new_coldkey --wallet.name owner
```

Create a cold key for your miner wallet:

```bash
btcli wallet new_coldkey --wallet.name miner
```

and

```bash
btcli wallet new_hotkey --wallet.name miner --wallet.hotkey default
```

Create a cold key for your authenticator wallet:

```bash
btcli wallet new_coldkey --wallet.name validator
```

and

```bash
btcli wallet new_hotkey --wallet.name validator --wallet.hotkey default
```

## 3. Getting Subnet Creation Fees

Creating subnets on the test network is competitive. The fee is determined by the rate at which new subnets are registered to the chain.

By default, you must have at least 100 testnet TAOs in the owner's wallet to create a subnet. However, the exact amount will fluctuate based on demand. The following command shows how to get the current cost of creating a subnet.

```bash
btcli subnet lock_cost --subtensor.network test
```

The above command will show:

```bash
>> Subnet lock cost: τ100.000000000
```

## 4. (Optional) Getting Tap Tokens

Taps have been disabled on the test network. Therefore, if you do not have enough tap tokens, request tap tokens at [Bittensor Discord Community](https://discord.com/channels/799672011265015819/830068283314929684).

## 5. Purchase a slot

Using the test TAO obtained in the previous step, you can register your subnet on the test network. This will create a new subnet and grant you owner rights.

The following commands show how to purchase a slot.

**Note:** Slots require a TAO lock. You will return these TAOs when you unregister the subnet.

```bash
btcli subnet create --subtensor.network test 
```

Enter the name of the owner's wallet that will be given cold key access:

```bash
>> Enter wallet name (default): owner # Enter the name of your owner's wallet.
>> Enter the password to unlock the key: # Enter your wallet password.
>> Register subnet? [y/n]: <y/n> # Select yes (y)
>> ⠇ 📡 Registering subnet...
✅ Subnet registered, netuid: 1 # Your subnet netuid will be displayed here, save it for later.
```

## 6. Registering Keys

This step registers your subnet verifier and subnet miner keys to the subnet, giving them **the first two slots**.

Register your miner key to the subnet:

```bash
btcli subnet register --netuid 13 --subtensor.network test --wallet.name miner --wallet.hotkey default
```

Follow the prompts below:

```bash
>> Enter netuid [1] (1): # Enter netuid 1 to specify the subnet you just created.
>> Continue to register ?
  Hot key: ...
  Cold key: ...
  Network: finney [y/n]: # Select yes (y)
>> ✅ Registered
```

Next, register your authenticator key to the subnet:

```bash
btcli subnet register --netuid 13 --subtensor.network test --wallet.name validator --wallet.hotkey default
```

Follow the prompt:

```bash
>> Enter netuid [1] (1): # Enter netuid 1 to specify the subnet you just created.
>> Continue to register ?
  Hot key: ...
  Cold key: ...
  Network: finney [y/n]: # Select yes (y)
>> ✅ Registered
```

## 7.Check whether your key is registered or not

This step returns information about your registered key.

Check if your authenticator key is registered:

```bash
btcli wallet overview --wallet.name validator --subtensor.network test
```

The above command will display the following:

``bash
Subnet: 1                                                                                                                                                                
Cold key Hot key UID Active Collateral(τ) Ranking Trust Consensus Incentive Dividend Emission(ρ) V Trust V Privilege Update AXON Hot key_SS58                    
miner default 0 True 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0 0.00000 14 none 5GTFrsEQfvTsh3WjiEVFeKzFTc2xcf...
1 1 2 τ0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 ρ0 0.00000                                                         
                                                                          Wallet balance: τ0.0         


##  8.running WOOF-recognition


 git clone https://github.com/Woof-AI/WOOF-recognition

 cd WOOF-recognition

 python -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
 python app.py 



## 9.running subnet miners and subnet validators

start webnet
python app.py

Run the subnet miner:

```bash
python neurons/miner.py --netuid 1 --subtensor.network test --wallet.name miner --wallet.hotkey default --logging.debug
```

You will see the following terminal output

```bash
>> 2023-08-08 16:58:11.223 | info | Running miner: subnet: 1 network: ws://127.0.0.1:9946 configuration: ...
```

Next, run the subnet verifier:

```bash
python neurons/validator.py --netuid 1 --subtensor.network test --wallet.name validator --wallet.hotkey default --logging.debug
```

You will see the following terminal output

```bash
>> 2023-08-08 16:58:11.223 | info | running validator: subnet: 1 network: ws://127.0.0.1:9946 configuration: ...
```

## 10. Getting Emissions Traffic

Register the root network with ``btcli``:

``bash
btcli root register --subtensor.network test
```

Then set the weights of the sub-network:

``bash
btcli root weights --subtensor.network test
```

## 11. Stopping the node

To stop the node, press CTRL + C at the terminal where the node is running.



# Notice
The model always stays on your machine and is yours!
The data provided by our community friends and the benefits and efficiency brought by running in the subnet will better help us train the dog model

