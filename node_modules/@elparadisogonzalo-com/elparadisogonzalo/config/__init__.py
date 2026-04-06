import os
from dotenv import load_dotenv
from web3 import Web3

# Force load from project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

class Config:
    def __init__(self):
        self.rpc_url = os.getenv("RPC_URL")
        self.wallet_address = os.getenv("WALLET_ADDRESS")
        self.web3 = Web3(Web3.HTTPProvider(self.rpc_url))
        if not self.web3.is_connected():
            print("❌ Failed to connect to blockchain")
            self.web3 = None

    def get(self, section, key):
        if key == "wallet_address":
            return self.wallet_address
        return None
