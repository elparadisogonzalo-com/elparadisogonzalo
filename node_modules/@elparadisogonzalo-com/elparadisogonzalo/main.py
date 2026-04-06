from config import Config

def main():
    cfg = Config()
    if not cfg.web3:
        return

    print("RPC URL:", cfg.rpc_url)
    print("Connected:", cfg.web3.is_connected())

    # Get latest block
    block = cfg.web3.eth.block_number
    print("Latest block:", block)

    # Check wallet balance
    address = cfg.get("web3", "wallet_address")
    balance = cfg.web3.eth.get_balance(address)
    print("Wallet balance (wei):", balance)

if __name__ == "__main__":
    main()
