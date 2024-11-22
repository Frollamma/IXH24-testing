response = {
    "close_time_iso": "2024-11-22T17:37:42Z",
    "ctid": "C0263DD300000001",
    "hash": "71BC5770F16EBE6B6B298929A1D69EEC668F247AE602C65F6381A574E051F3DD",
    "ledger_hash": "889CA6CFC3142B2E94C5F0127668F37BC9BF2734424B15B5AF20E89EAFECBB89",
    "ledger_index": 2506195,
    "meta": {
        "AffectedNodes": [
            {
                "CreatedNode": {
                    "LedgerEntryType": "NFTokenPage",
                    "LedgerIndex": "AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0FFFFFFFFFFFFFFFFFFFFFFFF",
                    "NewFields": {
                        "NFTokens": [
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D082D2F25600263DBB",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            }
                        ]
                    },
                }
            },
            {
                "ModifiedNode": {
                    "FinalFields": {
                        "Account": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
                        "Balance": "99999990",
                        "FirstNFTokenSequence": 2506171,
                        "Flags": 0,
                        "MintedNFTokens": 1,
                        "OwnerCount": 1,
                        "Sequence": 2506172,
                    },
                    "LedgerEntryType": "AccountRoot",
                    "LedgerIndex": "FA401B359E4B4A7BD6EECAE9263498F3F50388487D31932A030AF6F9B78373EC",
                    "PreviousFields": {
                        "Balance": "100000000",
                        "OwnerCount": 0,
                        "Sequence": 2506171,
                    },
                    "PreviousTxnID": "50B6A8FBF0A8BFE03B15F9D5B661F6DC3E679AC693305E199B2B23E8DFA08C50",
                    "PreviousTxnLgrSeq": 2506171,
                }
            },
        ],
        "TransactionIndex": 0,
        "TransactionResult": "tesSUCCESS",
        "nftoken_id": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D082D2F25600263DBB",
    },
    "tx_json": {
        "Account": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
        "Fee": "10",
        "Flags": 8,
        "LastLedgerSequence": 2506213,
        "NFTokenTaxon": 0,
        "Sequence": 2506171,
        "SigningPubKey": "ED545C377B69D9F7F0D64573E9A9B9D0CA0B53EA0A2945DAA52847559092EC0133",
        "TransactionType": "NFTokenMint",
        "TransferFee": 0,
        "TxnSignature": "960272E3ED9AE0F6F64DE1EF095D65AF9D72AD550DBA24360B29E64F1E9E71C13DA189B15320181CADD31A86173D8E30899ACE5DE5834A9A7D3B704D42D8F20C",
        "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
        "date": 785612262,
        "ledger_index": 2506195,
    },
    "validated": True,
}

response_sell_offer = {
    "close_time_iso": "2024-11-22T18:54:01Z",
    "ctid": "C02643B700000001",
    "hash": "A9FAE83BDA346D556878A34B7A92EF92ABC780C36C27EED7BD5FEF38ABA61A89",
    "ledger_hash": "2E077198A24FC5E822B57DD9315EB88EC19064DD8C6F93FA086004C6810637F8",
    "ledger_index": 2507703,
    "meta": {
        "AffectedNodes": [
            {
                "ModifiedNode": {
                    "LedgerEntryType": "AccountRoot",
                    "LedgerIndex": "4266B1584F27AD78AA435CD626DC7580204DD0D983A14519D366236E47E938B7",
                    "PreviousTxnID": "357BCF6E48E8C255ECF985768DA3D40526544774CEE4762C8F860F06D38056AC",
                    "PreviousTxnLgrSeq": 2507698,
                }
            },
            {
                "CreatedNode": {
                    "LedgerEntryType": "DirectoryNode",
                    "LedgerIndex": "A44F3B3AE9819E094FAFACC1ACAE2DA611459932E7070475607DB09555EBBBBE",
                    "NewFields": {
                        "Flags": 2,
                        "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0231BA95D00263DC2",
                        "RootIndex": "A44F3B3AE9819E094FAFACC1ACAE2DA611459932E7070475607DB09555EBBBBE",
                    },
                }
            },
            {
                "CreatedNode": {
                    "LedgerEntryType": "NFTokenOffer",
                    "LedgerIndex": "AB8E2AFF59FA024A171D59415B627288BFCBAE4D6DA4478EB1EF0F6DF451C861",
                    "NewFields": {
                        "Destination": "rap34aTVuYT7mvs6ynuffGEHh9egPuteg5",
                        "Expiration": 785620429,
                        "Flags": 1,
                        "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0231BA95D00263DC2",
                        "Owner": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
                    },
                }
            },
            {
                "CreatedNode": {
                    "LedgerEntryType": "DirectoryNode",
                    "LedgerIndex": "CFB521027AACF63F9D1FB7731EA5EC0429575259263B91269B4675B8771C5164",
                    "NewFields": {
                        "Owner": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
                        "RootIndex": "CFB521027AACF63F9D1FB7731EA5EC0429575259263B91269B4675B8771C5164",
                    },
                }
            },
            {
                "ModifiedNode": {
                    "FinalFields": {
                        "Account": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
                        "Balance": "99985770",
                        "FirstNFTokenSequence": 2506171,
                        "Flags": 0,
                        "MintedNFTokens": 8,
                        "OwnerCount": 2,
                        "Sequence": 2506187,
                    },
                    "LedgerEntryType": "AccountRoot",
                    "LedgerIndex": "FA401B359E4B4A7BD6EECAE9263498F3F50388487D31932A030AF6F9B78373EC",
                    "PreviousFields": {
                        "Balance": "99985780",
                        "OwnerCount": 1,
                        "Sequence": 2506186,
                    },
                    "PreviousTxnID": "357BCF6E48E8C255ECF985768DA3D40526544774CEE4762C8F860F06D38056AC",
                    "PreviousTxnLgrSeq": 2507698,
                }
            },
        ],
        "TransactionIndex": 0,
        "TransactionResult": "tesSUCCESS",
        "offer_id": "AB8E2AFF59FA024A171D59415B627288BFCBAE4D6DA4478EB1EF0F6DF451C861",
    },
    "tx_json": {
        "Account": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
        "Amount": "0",
        "Destination": "rap34aTVuYT7mvs6ynuffGEHh9egPuteg5",
        "Expiration": 785620429,
        "Fee": "10",
        "Flags": 1,
        "LastLedgerSequence": 2507721,
        "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0231BA95D00263DC2",
        "Sequence": 2506186,
        "SigningPubKey": "ED545C377B69D9F7F0D64573E9A9B9D0CA0B53EA0A2945DAA52847559092EC0133",
        "TransactionType": "NFTokenCreateOffer",
        "TxnSignature": "B618E1069B9EC4CF63ADBB96565EE8CE088537FE88B87D9C1A0FA7D98137CFB82B0AE9603F073BDBEE59D57E322DB71D17B783AA65B5C0FA25A9A3C7F0BB7F00",
        "date": 785616841,
        "ledger_index": 2507703,
    },
    "validated": True,
}

response_accept_sell_offer = {
    "close_time_iso": "2024-11-22T19:09:50Z",
    "ctid": "C02644EC00000001",
    "hash": "D9C422B1721FD6AC8DA9AB9CCFF632D49B1BF692E9A4A7181152DA253A3BA588",
    "ledger_hash": "A7DDC26F9EA89485C129338AA3B357353C4FBC2EA2108C77D40E82A64CDB82BE",
    "ledger_index": 2508012,
    "meta": {
        "AffectedNodes": [
            {
                "DeletedNode": {
                    "FinalFields": {
                        "Amount": "0",
                        "Destination": "rap34aTVuYT7mvs6ynuffGEHh9egPuteg5",
                        "Expiration": 785621362,
                        "Flags": 1,
                        "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D050E74B5F00263DC4",
                        "NFTokenOfferNode": "0",
                        "Owner": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
                        "OwnerNode": "0",
                        "PreviousTxnID": "3D88EA28E39E4416F9F3A365A62BF851A2A5A7F41ECE362E10F3D5C82CA4D0D4",
                        "PreviousTxnLgrSeq": 2508009,
                    },
                    "LedgerEntryType": "NFTokenOffer",
                    "LedgerIndex": "072FDE1DECC1FB3D73D5F5FADA63F2E0D4939A86D659EA1002AF2FBA4AA5223E",
                }
            },
            {
                "DeletedNode": {
                    "FinalFields": {
                        "Flags": 2,
                        "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D050E74B5F00263DC4",
                        "PreviousTxnID": "3D88EA28E39E4416F9F3A365A62BF851A2A5A7F41ECE362E10F3D5C82CA4D0D4",
                        "PreviousTxnLgrSeq": 2508009,
                        "RootIndex": "2EFBB748326C6C3E481B24C36FAF2E50DC2461CDB64642B3134C4397A58C3170",
                    },
                    "LedgerEntryType": "DirectoryNode",
                    "LedgerIndex": "2EFBB748326C6C3E481B24C36FAF2E50DC2461CDB64642B3134C4397A58C3170",
                }
            },
            {
                "CreatedNode": {
                    "LedgerEntryType": "NFTokenPage",
                    "LedgerIndex": "370F31188619D33A535983A710956BAF3D8E6683FFFFFFFFFFFFFFFFFFFFFFFF",
                    "NewFields": {
                        "NFTokens": [
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D050E74B5F00263DC4",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            }
                        ]
                    },
                }
            },
            {
                "ModifiedNode": {
                    "FinalFields": {
                        "Account": "rap34aTVuYT7mvs6ynuffGEHh9egPuteg5",
                        "Balance": "100015990",
                        "Flags": 0,
                        "OwnerCount": 1,
                        "Sequence": 2507471,
                    },
                    "LedgerEntryType": "AccountRoot",
                    "LedgerIndex": "4266B1584F27AD78AA435CD626DC7580204DD0D983A14519D366236E47E938B7",
                    "PreviousFields": {
                        "Balance": "100016000",
                        "OwnerCount": 0,
                        "Sequence": 2507470,
                    },
                    "PreviousTxnID": "3D88EA28E39E4416F9F3A365A62BF851A2A5A7F41ECE362E10F3D5C82CA4D0D4",
                    "PreviousTxnLgrSeq": 2508009,
                }
            },
            {
                "ModifiedNode": {
                    "FinalFields": {
                        "Flags": 0,
                        "NFTokens": [
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D00C35D85C00263DC1",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0231BA95D00263DC2",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D03A017A5E00263DC3",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D082D2F25600263DBB",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D099B8C35700263DBC",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0B09E945800263DBD",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0C784655900263DBE",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0DE6A365A00263DBF",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0F550075B00263DC0",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                        ],
                    },
                    "LedgerEntryType": "NFTokenPage",
                    "LedgerIndex": "AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0FFFFFFFFFFFFFFFFFFFFFFFF",
                    "PreviousFields": {
                        "NFTokens": [
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D00C35D85C00263DC1",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0231BA95D00263DC2",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D03A017A5E00263DC3",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D050E74B5F00263DC4",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D082D2F25600263DBB",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D099B8C35700263DBC",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0B09E945800263DBD",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0C784655900263DBE",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0DE6A365A00263DBF",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                            {
                                "NFToken": {
                                    "NFTokenID": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D0F550075B00263DC0",
                                    "URI": "68747470733A2F2F656E7A6F2E636F6D2F31323334",
                                }
                            },
                        ]
                    },
                    "PreviousTxnID": "95DD0E29AE7CDE0A4FE667C6335D95A2FD0E1F7AB51F4BAF9C1F0B368FB2C8C4",
                    "PreviousTxnLgrSeq": 2508000,
                }
            },
            {
                "ModifiedNode": {
                    "FinalFields": {
                        "Flags": 0,
                        "Owner": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
                        "RootIndex": "CFB521027AACF63F9D1FB7731EA5EC0429575259263B91269B4675B8771C5164",
                    },
                    "LedgerEntryType": "DirectoryNode",
                    "LedgerIndex": "CFB521027AACF63F9D1FB7731EA5EC0429575259263B91269B4675B8771C5164",
                    "PreviousTxnID": "3D88EA28E39E4416F9F3A365A62BF851A2A5A7F41ECE362E10F3D5C82CA4D0D4",
                    "PreviousTxnLgrSeq": 2508009,
                }
            },
            {
                "ModifiedNode": {
                    "FinalFields": {
                        "Account": "rGeQMqAnoZdn4xh4j8dw2j9bkrJgSZ2ZQB",
                        "Balance": "99981690",
                        "FirstNFTokenSequence": 2506171,
                        "Flags": 0,
                        "MintedNFTokens": 10,
                        "OwnerCount": 3,
                        "Sequence": 2506193,
                    },
                    "LedgerEntryType": "AccountRoot",
                    "LedgerIndex": "FA401B359E4B4A7BD6EECAE9263498F3F50388487D31932A030AF6F9B78373EC",
                    "PreviousFields": {"OwnerCount": 4},
                    "PreviousTxnID": "3D88EA28E39E4416F9F3A365A62BF851A2A5A7F41ECE362E10F3D5C82CA4D0D4",
                    "PreviousTxnLgrSeq": 2508009,
                }
            },
        ],
        "TransactionIndex": 0,
        "TransactionResult": "tesSUCCESS",
        "nftoken_id": "00080000AB9CC6DA21003E7F43F31A3F242FF1C0CCE0E2D050E74B5F00263DC4",
    },
    "tx_json": {
        "Account": "rap34aTVuYT7mvs6ynuffGEHh9egPuteg5",
        "Fee": "10",
        "Flags": 0,
        "LastLedgerSequence": 2508030,
        "NFTokenSellOffer": "072FDE1DECC1FB3D73D5F5FADA63F2E0D4939A86D659EA1002AF2FBA4AA5223E",
        "Sequence": 2507470,
        "SigningPubKey": "EDFF2461FE923C65FB0B5481179DF6AA84B0DCFF211D7E28E9ACB3E7887940B1F9",
        "TransactionType": "NFTokenAcceptOffer",
        "TxnSignature": "B680F1B6086FFA34627F7DB00627D84F2427F286F8053550F309D9E8F1E647C4723893AABF2E13AF2BF7B39F3BCB0403E2EC4E0243F49618B3CFC66383819901",
        "date": 785617790,
        "ledger_index": 2508012,
    },
    "validated": True,
}
