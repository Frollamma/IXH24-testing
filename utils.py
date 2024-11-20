from xrpl.account import get_balance
from xrpl.clients import JsonRpcClient
from xrpl.core import keypairs


def generate_xrpl_wallet_seed() -> str:
    """
    Generate a random seed. Notice that if you create a wallet with this seed, it won't be a working wallet, because you need to fund it before. See https://xrpl.org/docs/concepts/accounts#creating-accounts.
    """
    return keypairs.generate_seed()


def print_balances(wallets: list, client: JsonRpcClient) -> None:
    """
    Print the balances of wallets.
    """
    print("Balances:")
    for wallet in wallets:
        print(f"{wallet.address}: {get_balance(wallet.address, client)}")
