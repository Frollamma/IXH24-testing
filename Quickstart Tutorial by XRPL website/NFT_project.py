import xrpl
import json

from mod1 import get_account, get_account_info, send_xrp
from mod2 import (
    create_trust_line,
    send_currency,
    get_balance,
    configure_account,
)
from mod3 import (
    mint_token,
    get_tokens,
    burn_token,
)
from mod4 import (
    create_sell_offer,
    create_buy_offer,
    get_offers,
    cancel_offer,
    accept_sell_offer,
    accept_buy_offer,
)
from utils import get_wallet, print_balances
from xrpl.account import get_next_valid_seq_number, get_balance
from xrpl.models import Payment, Tx
from xrpl.transaction import sign, submit_and_wait
from xrpl.wallet import Wallet, generate_faucet_wallet
from xrpl.ledger import get_latest_validated_ledger_sequence
from xrpl.clients import JsonRpcClient
from datetime import datetime, timedelta
from xrpl.utils import datetime_to_ripple_time


seed_company = "sEd7uhRLEHf7sELoTUiKTcDwgn3zvdA"
seed_receiver = "sEd7vJWGo5cYxju2raWQ1yQSFPgVejN"
product_uri = "https://enzo.com/1234"
taxon = 0
# taxon_string = "VivaEnzo"
# taxon = int.from_bytes(taxon_string.encode())
MIN_AMOUNT = "2000"
MIN_FEE = "20"

def create_and_transfer_nft(seed_company, seed_receiver, product_uri, taxon, chain_url = "https://s.altnet.rippletest.net:51234"):
    try:
        client=JsonRpcClient(chain_url)

        wallet_company = get_wallet(seed_company)
        seed_company = wallet_company.seed
        
        flag = 8
        transfer_fee = 0
        response_mint_token = mint_token(
                seed_company,
                product_uri,
                flag,
                transfer_fee,
                taxon
            )
        # print(f"{response_mint_token = }")
        NFT_token_id = response_mint_token['meta']['nftoken_id'] 

        wallet_receiver = get_wallet(seed_receiver)
        seed_receiver = wallet_receiver.seed
        # print(f"{seed_receiver = }")

        # Create account by sending funds
        current_validated_ledger = get_latest_validated_ledger_sequence(client)

        tx_payment = Payment(
            account=wallet_company.address,
            amount=MIN_AMOUNT,
            destination=wallet_receiver.address,
            last_ledger_sequence=current_validated_ledger + 20,
            sequence=get_next_valid_seq_number(wallet_company.address, client),
            fee=MIN_FEE,
        )
        my_tx_payment_signed = sign(tx_payment, wallet_company)
        tx_response = submit_and_wait(my_tx_payment_signed, client)

        # print_balances([wallet_company, wallet_receiver], client)

        # Create Sell Offer for the receiver account with amount 0 and accept it
        current_time = datetime.now()
        expiration_time = current_time + timedelta(minutes=60)
        expiration_time = datetime_to_ripple_time(expiration_time)

        response_sell_offer = create_sell_offer(seed_company, '0', NFT_token_id, expiration=expiration_time, destination=wallet_receiver.address)
        # print(f"{response_sell_offer = }")
        sell_offer_ledger_index = response_sell_offer['meta']['offer_id']

        # Accept sell offer of company by receiver
        response_accept_sell_offer = accept_sell_offer(seed_receiver, sell_offer_ledger_index)
        # print(f"{response_accept_sell_offer = }")

        if response_accept_sell_offer['meta']['TransactionResult'] == 'tesSUCCESS':
            return True
    except Exception as e:
        raise Exception(f'Didn\'t work: {e}')

if __name__ == '__main__':
    result = create_and_transfer_nft(seed_company, seed_receiver, product_uri, taxon)
    
    if result == True:
        print("Everything ok")