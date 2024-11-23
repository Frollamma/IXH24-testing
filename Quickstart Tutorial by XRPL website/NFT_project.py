from utils import create_and_transfer_nft

seed_company = "sEd7uhRLEHf7sELoTUiKTcDwgn3zvdA"
seed_receiver = "sEd7vJWGo5cYxju2raWQ1yQSFPgVejN"
product_uri = "https://enzo.com/1234"
taxon = 0
# taxon_string = "VivaEnzo"
# taxon = int.from_bytes(taxon_string.encode())

# def create_and_transfer_nft(seed_company, product_uri, taxon, seed_receiver = None, chain_url = "https://s.altnet.rippletest.net:51234"):
#     try:
#         if seed_receiver is None:
#             seed_receiver = _generate_xrpl_wallet_seed()
        
#         client=JsonRpcClient(chain_url)

#         wallet_company = get_wallet(seed_company)
#         seed_company = wallet_company.seed
        
#         flag = 8
#         transfer_fee = 0
#         response_mint_token = mint_nft_token(
#                 seed_company,
#                 product_uri,
#                 flag,
#                 transfer_fee,
#                 taxon
#             )
#         # print(f"{response_mint_token = }")
#         NFT_token_id = response_mint_token['meta']['nftoken_id'] 

#         wallet_receiver = get_wallet(seed_receiver)
#         seed_receiver = wallet_receiver.seed
#         # print(f"{seed_receiver = }")

#         # Create account by sending funds
#         current_validated_ledger = get_latest_validated_ledger_sequence(client)

#         tx_payment = Payment(
#             account=wallet_company.address,
#             amount=MIN_AMOUNT,
#             destination=wallet_receiver.address,
#             last_ledger_sequence=current_validated_ledger + 20,
#             sequence=get_next_valid_seq_number(wallet_company.address, client),
#             fee=MIN_FEE,
#         )
#         my_tx_payment_signed = sign(tx_payment, wallet_company)
#         tx_response = submit_and_wait(my_tx_payment_signed, client)

#         # print_balances([wallet_company, wallet_receiver], client)

#         # Create Sell Offer for the receiver account with amount 0 and accept it
#         current_time = datetime.now()
#         expiration_time = current_time + timedelta(minutes=60)
#         expiration_time = datetime_to_ripple_time(expiration_time)

#         response_sell_offer = create_sell_offer(seed_company, '0', NFT_token_id, expiration=expiration_time, destination=wallet_receiver.address)
#         # print(f"{response_sell_offer = }")
#         sell_offer_ledger_index = response_sell_offer['meta']['offer_id']

#         # Accept sell offer of company by receiver
#         response_accept_sell_offer = accept_sell_offer(seed_receiver, sell_offer_ledger_index)
#         # print(f"{response_accept_sell_offer = }")

#         if not response_accept_sell_offer['meta']['TransactionResult'] == 'tesSUCCESS':
#             raise Exception(f'Didn\'t work: {e}')
#     except Exception as e:
#         raise Exception(f'Didn\'t work: {e}')

if __name__ == '__main__':
    result = create_and_transfer_nft(seed_company, product_uri, taxon, seed_receiver=seed_receiver)
    print("Everything ok")
    