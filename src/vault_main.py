"""Main entry point for running vault for wrapping.
Example Command:

python src/vault_main.py --btc_vault_id="Wallet1-testnet" --network="testnet"

"""

import argparse

from utils import initiateEndpoint


def main() -> None:
    """Main entry point for running vault for wrapping."""
    print("AnetaBTC")

    parser = argparse.ArgumentParser(
        description='Decentralized Wrapping of Bitcoin for Ergo and Cardano')
    parser.add_argument('--option',
                        default='endpoint',
                        help='options for vault')
    parser.add_argument('--vault_id', default=None, help='id of clients vault')
    parser.add_argument('--btc_vault_id',
                        default=None,
                        help='id of clients btc vault')
    parser.add_argument(
        '--network',
        default='mainnet',
        help=
        'Network to run application on should be \'testnet\' or \'mainnet\'')
    args = parser.parse_args()
    print(args)

    if args.option == 'endpoint':
        initiateEndpoint(btc_vault_id=args.btc_vault_id,
                        network=args.network,
                        vault_id=args.vault_id)
    else:
        raise ValueError(str(args.option) + ' is an undefined option')


if __name__ == "__main__":  # pragma: no cover
    main()
