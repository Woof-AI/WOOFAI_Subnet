#!/bin/bash

# creat venv 
python3 -m venv btcli_venv
source btcli_venv/bin/activate

# setuo bittensor sdk
pip install bittensor
pip install -e .

# finished!!!
echo "Setup completed successfully!"
