# new edit
import pprint

text = "merchant_account_resolver_category=&response_signature=78b19d85ac7fd0bd5d8f0ae7a7fe9749e1828bea4382e73665b6894e63feb0d2&group_transaction_id=&provider_status_code_1=&response_signature_v2=SFMyNTYKdHJhbnNhY3Rpb25faWQ9NjkyNWQ1YWEtMzFiZC00YjFmLWFmNzctMzE2NGFmMzIxMDAzCmNvbXBsZXRpb25fdGltZXN0YW1wPTIwMjAxMjE0MTAyMzA5Cm1hc2tlZF9hY2NvdW50X251bWJlcj00MTExMTEqKioqKioxMTExCnRva2VuX2lkPTQ0NTIzMDU2NjkxMTExMTEKYXV0aG9yaXphdGlvbl9jb2RlPQptZXJjaGFudF9hY2NvdW50X2lkPTBiN2ViYWE2LTljNzQtMTFlOS1hMmEzLTJhMmFlMmRiY2NlNAp0cmFuc2FjdGlvbl9zdGF0ZT1mYWlsZWQKaXBfYWRkcmVzcz0xMC4xOTIuMy4xNzkKdHJhbnNhY3Rpb25fdHlwZT1wdXJjaGFzZQpyZXF1ZXN0X2lkPUsxNDMxMjE0MTgyMjM5OTI3NTI0NzMK.QsxOq2N%2BbQQX%2B30iRP134UIMRvA0fKEnhqKWnesBI1A%3D&provider_status_code_2=&provider_status_description_2=&requested_amount=27.90&completion_time_stamp=20201214102309&provider_status_description_1=&token_id=4452305669111111&authorization_code=&merchant_account_id=0b7ebaa6-9c74-11e9-a2a3-2a2ae2dbcce4&provider_transaction_reference_id=&first_name=Transfer&payment_method=creditcard&transaction_id=6925d5aa-31bd-4b1f-af77-3164af321003&provider_transaction_id_1=&provider_transaction_id_2=&status_severity_2=error&status_severity_1=information&last_name=NA&ip_address=10.192.3.179&transaction_type=purchase&status_code_1=200.1084&status_code_2=400.1048&field_name_1=elastic-page-api.3d.original_txn_type&masked_account_number=411111******1111&status_description_1=Proof+of+authentication+attempt+was+generated.&status_description_2=This+Merchant+Account+does+not+have+a+Provider+Account+associated+with+it.++Please+contact+technical+support.&transaction_state=failed&requested_amount_currency=SGD&request_id=K143121418223992752473&field_value_1=purchase"


splitted = text.split("&")

print(len(splitted))

pprint.pprint(splitted)
