from xrpl.account import get_balance
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet, generate_faucet_wallet
from xrpl.core import keypairs


def _generate_xrpl_wallet_seed() -> str:
    """
    Generate a random seed. Notice that if you create a wallet with this seed, it won't be a working wallet, because you need to fund it before. See https://xrpl.org/docs/concepts/accounts#creating-accounts.
    """
    return keypairs.generate_seed()


def get_wallet(seed: str | None = None) -> Wallet:
    """
    Generate a wallet.
    """
    client = JsonRpcClient("https://s.altnet.rippletest.net:51234")
    if seed:
        wallet = Wallet.from_seed(seed)
    else:
        wallet = generate_faucet_wallet(client, debug=True)
    return wallet


def print_balances(wallets: list, client: JsonRpcClient) -> None:
    """
    Print the balances of wallets.
    """
    print("Balances:")
    for wallet in wallets:
        print(f"{wallet.address}: {get_balance(wallet.address, client)}")
