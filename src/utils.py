"""Utils file for wrapping."""
from bitcoinlib.wallets import Wallet, wallet_create_or_open


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


def notPassedPayement(wallet, btc_vault_address) -> bool:
    for transaction in wallet.transactions_full():
        for output in transaction.outputs:
            if output.address == btc_vault_address:
                return False
    return True


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
            runMintingSmartContract(
                amount=0.0,
                btc_vault_address=btc_wallet_address,
                btc_wallet_address=btc_wallet_address,
                network=network,
                erg_vault_address=getERGAddress(vault_id),
                erg_wallet_address=getERGAddress(wallet_id))
            #

            # Return info
            return {"info": w.transactions_full()}
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
    # Send anetaBTC from User Wallet to Smart contract

    # Send Redeem request to Vault which will (Send from Vault BTC Wallet to BTC Wallet)

    # Run smart contract to verify Transaction and keep, return, or slash Collateral

    # Return info
    print("Burn function that needs to be written")
    return {}
