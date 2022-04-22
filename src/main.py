"""Main entry point for running wrapping."""

import argparse
from utils import initiateBurn, initiateMint

def sampleFunc() -> None:
    """Sample function to demo tests."""
    print("I am a function that needs to be tested")


def main() -> None:
    """Main entry point for running wrapping."""
    print("AnetaBTC")
    sampleFunc()

    parser = argparse.ArgumentParser(description='Decentralized Wrapping of Bitcoin for Ergo and Cardano')
    parser.add_argument('--option', default='mint', help='whether function should \'mint\' or \'burn\'')
    parser.add_argument('--wallet_id', default=None, help='id of users wallet')
    parser.add_argument('--vault_id', default=None, help='id of clients vault')
    parser.add_argument('--btc_wallet_id', default=None, help='id of users btc wallet')
    parser.add_argument('--btc_vault_id', default=None, help='id of clients btc vault')
    parser.add_argument('--amount', default=0.0, help='amount to mint or burn')
    parser.add_argument('--network', default='mainnet', help='Network to run application on should be \'testnet\' or \'mainnet\'')
    args = parser.parse_args()
    print(args)

    if args.option == 'mint':
        print(initiateMint(amount=args.amount, btc_vault_id=args.btc_vault_id, btc_wallet_id=args.btc_wallet_id, network=args.network, vault_id=args.vault_id, wallet_id=args.wallet_id))
    elif args.option == 'burn':
        print(initiateBurn(amount=args.amount, btc_vault_id=args.btc_vault_id, btc_wallet_id=args.btc_wallet_id, network=args.network, vault_id=args.vault_id, wallet_id=args.wallet_id))
    else:
        raise ValueError(str(args.option) + ' is an undefined option')



if __name__ == "__main__":  # pragma: no cover
    main()
