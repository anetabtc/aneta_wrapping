"""Utils file for wrapping."""
import bitcoinlib
from bitcoinlib.wallets import Wallet, wallet_create_or_open
import time
from datetime import datetime
from bitcoinlib.services.services import Service

def verifyVault(amount=0.0, vault_id=None) -> bool:
    return True

def getBTCAddress(btc_id=None) -> str:
    return 'mqG7j93x8Yu47Niq15rtotmxVTG3Jc8LcH'

def getERGAddress(erg_id=None) -> str:
    return None

def runMintingSmartContract(amount, btc_vault_address, btc_wallet_address,
                            network, erg_vault_address,
                            erg_wallet_address) -> dict:
    print("MAGIC HAPPENS HERE")
    return {}

def runRedeemingSmartContract(amount, btc_vault_address, btc_wallet_address,
                            network, erg_vault_address,
                            erg_wallet_address) -> dict:
    print("MAGIC HAPPENS HERE Also")
    return {}

def sendRedeemRequest(amount, btc_vault_id, btc_wallet_address,
                            network, erg_vault_address,
                            erg_wallet_address) -> dict:
    print(f"Sending Redeem Request vault_id {btc_vault_id}")
    # Temporary!!! Onlf for local test
    try:
        initiateEndpoint(btc_vault_id=btc_vault_id,
                        network=network,
                        btc_user_address=btc_wallet_address)
    except bitcoinlib.wallets.WalletError:
        pass

    #
    return {}

def checkTransaction(amount, btc_vault_address, btc_wallet_address,
                            network, erg_vault_address,
                            erg_wallet_address, start_time) -> dict:
    print(f"Checking whether {btc_vault_address} sent {amount}BTC to {btc_wallet_address} on {network} after {start_time}")
    srv = Service()
    for transaction in srv.gettransactions(btc_vault_address):
        for output in transaction.outputs:
            if output.address == btc_wallet_address \
                and transaction.as_dict()['date'] > start_time \
                and transaction.as_dict()['status'] == 'confirmed':
                # TODO NEED TO Check Amount
                import ipdb; ipdb.set_trace()
                print("Transaction was successful")
                return {"status": True}
    return {"status": False}

def notPassedPayement(wallet, btc_vault_address) -> bool:
    for transaction in wallet.transactions_full():
        for output in transaction.outputs:
            if output.address == btc_vault_address:
                # TODO need to check if transaction was already confirmed
                return False
    return True

def sendBTC(amount, wallet, send_address, network='testnet'):
    return wallet.send_to(send_address,
                          f'{amount} TBTC',
                          offline=False,
                          network=network)
            

def initiateMint(amount=0.0,
                 btc_vault_id=None,
                 btc_wallet_id=None,
                 network='testnet',
                 vault_id=None,
                 wallet_id=None) -> dict:
    """Loads btc_wallet_id sends money to vault with btc_vault_id and verifies
    then mints anetaBTC to wallet_id."""
    # Load BTC Wallet
    w = wallet_create_or_open(btc_wallet_id, network=network)
    btc_wallet_address = w.get_key().address
    print(btc_wallet_address)

    # Verify Vault for your amount and Check if payment already posted
    btc_vault_address = getBTCAddress(btc_vault_id)
    if verifyVault(amount=amount, vault_id=vault_id):
        if notPassedPayement(wallet=w, btc_vault_address=btc_vault_address):
            # Send Money from BTC Wallet to Verified Vault BTC Wallet
            t = w.send_to(btc_vault_address,
                          f'{amount} TBTC',
                          offline=False,
                          network=network)

            # Run smart contract to verify Transaction and Collateral, and Mint
            # TODO
            smart_contract_info = runMintingSmartContract(
                amount=amount,
                btc_vault_address=btc_vault_address,
                btc_wallet_address=btc_wallet_address,
                network=network,
                erg_vault_address=getERGAddress(vault_id),
                erg_wallet_address=getERGAddress(wallet_id))
            #

            # Return info
            return {"info": w.transactions_full(), "sc_info": smart_contract_info}
        else:
            error_msg = f"Payment to {btc_vault_address} is already posted"
            return {"info": error_msg}
    else:
        error_msg = f"Vault {vault_id} is not a verified vault"
        return {"info": error_msg}

def initiateBurn(amount=0.0,
                 btc_vault_id=None,
                 btc_wallet_id=None,
                 network='testnet',
                 vault_id=None,
                 wallet_id=None) -> dict:
    """Send Burn request to vault."""
    # Load BTC Wallet
    w = wallet_create_or_open(btc_wallet_id, network=network)
    btc_wallet_address = w.get_key().address
    print(btc_wallet_address)

    # Send anetaBTC from User Wallet to Smart contract
    btc_vault_address = getBTCAddress(btc_vault_id)
    start_time = datetime.now()

    smart_contract_info = runRedeemingSmartContract(
        amount=amount,
        btc_vault_address=btc_vault_address,
        btc_wallet_address=btc_wallet_address,
        network=network,
        erg_vault_address=getERGAddress(vault_id),
        erg_wallet_address=getERGAddress(wallet_id))

    # Send Redeem request to Vault which will (Send from Vault BTC Wallet to BTC Wallet)
    request_info = sendRedeemRequest(
        amount=amount,
        btc_vault_id=btc_vault_id,
        btc_wallet_address=btc_wallet_address,
        network=network,
        erg_vault_address=getERGAddress(vault_id),
        erg_wallet_address=getERGAddress(wallet_id))

    # Wait for transaction to post, smart contract to verify Transaction, and the contract to keep, return, or slash Collateral
    transaction_succeeded = False
    max_timesteps = 10 #1000
    t = 0
    while not transaction_succeeded and t < max_timesteps:
        check_info = checkTransaction(
            amount=amount,
            btc_vault_address=btc_vault_address,
            btc_wallet_address=btc_wallet_address,
            network=network,
            erg_vault_address=getERGAddress(vault_id),
            erg_wallet_address=getERGAddress(wallet_id),
            start_time=start_time)

        if check_info["status"]:
            transaction_succeeded = True
        else:
            t += 1
        
        time.sleep(1)

    # Return info
    return {"info": check_info, "sc_info": smart_contract_info, "request_info": request_info}

def initiateEndpoint(btc_vault_id=None,
                 network='testnet',
                 vault_id=None,
                 btc_user_address = 'mqG7j93x8Yu47Niq15rtotmxVTG3Jc8LcH') -> dict:
    # btc_user_address is used only for testing
    # Run Endpoint to wait for Redeem request then run sendBTC()
    # Example
    w = wallet_create_or_open(btc_vault_id, network=network)
    btc_vault_address = w.get_key().address
    print(btc_vault_address)
    amount = 0.0001
    info = sendBTC(amount=amount, wallet=w, send_address=btc_user_address, network=network)
    print(f"Sent from {btc_vault_address} sent {amount}BTC to {btc_user_address} on {network} at {datetime.now().time()}")

    # Return info
    return {"info": info}
