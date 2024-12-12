#!/bin/bash

# 创建并激活虚拟环境
python3 -m venv btcli_venv
source btcli_venv/bin/activate

# 克隆 btcli 仓库并安装
git clone https://github.com/opentensor/btcli.git
cd btcli
pip3 install .
pip install bittensor

# 返回上级目录
cd ..

# 克隆 WOOFAI_Subnet 仓库并安装
git clone https://github.com/Woof-AI/WOOFAI_Subnet
cd WOOFAI_Subnet
pip install -e .

# 可选：提示脚本完成
echo "Setup completed successfully!"