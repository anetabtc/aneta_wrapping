"""Utils file for wrapping."""

def initiateMint(amount=0.0, btc_vault_id=None, btc_wallet_id=None, network='testnet', vault_id=None, wallet_id=None) -> dict:
    """Loads btc_wallet_id sends money to vault with btc_vault_id and verifies then mints anetaBTC to wallet_id"""
    # Load BTC Wallet

    # Verify Vault for your amount

    # Send Money from BTC Wallet to Verified Vault BTC Wallet

    # Run smart contract to verify Transaction and Collateral, and Mint

    # Return info
    print("Mint function that needs to be written")
    return {}

def initiateBurn(amount=0.0, btc_vault_id=None, btc_wallet_id=None, network='testnet', vault_id=None, wallet_id=None) -> dict:
    """Send Burn request to vault"""
    # Send anetaBTC from User Wallet to Smart contract

    # Send Redeem request to Vault which will (Send from Vault BTC Wallet to BTC Wallet)

    # Run smart contract to verify Transaction and keep, return, or slash Collateral

    # Return info
    print("Burn function that needs to be written")
    return {}
    