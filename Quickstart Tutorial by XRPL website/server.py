from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from utils import create_and_transfer_nft, get_wallet
from email_utils import send_email
import uvicorn
from random import choice
from string import ascii_letters

BASE_URL = "http://127.0.0.1:5000"
seed_company = "sEd7uhRLEHf7sELoTUiKTcDwgn3zvdA"
ALPHABET = ascii_letters
COMPANY_EMAIL = "kings@diaden.com"
# COMPANY_EMAIL = "lucamigliaccio2000@gmail.com"

app = FastAPI()

class NFTTransferRequest(BaseModel):
    taxon: int
    email_receiver: str

@app.post("/nft/")
def create_and_transfer_nft_endpoint(request: NFTTransferRequest):
    """
    FastAPI endpoint to create and transfer an NFT.
    """
    chain_url = "https://s.altnet.rippletest.net:51234"
    product_uri = BASE_URL + "/" + "".join([choice(ALPHABET) for _ in range(10)])
    
    try:
        wallet_receiver = create_and_transfer_nft(
            seed_company=seed_company,
            product_uri=product_uri,
            taxon=int(request.taxon),
            chain_url=chain_url,
        )
        # wallet_receiver = get_wallet(seed_company) # TEST
        result = send_email(subject="Thank you for purchase, here is you NFT!", sender_email=COMPANY_EMAIL, recipient_email=request.email_receiver, wallet=wallet_receiver)
        print(f"{result = }")
        
        return {"status": "success", "message": "NFT created and transferred successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("server:app", port=5000, log_level="info")