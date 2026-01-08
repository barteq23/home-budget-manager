from src.integration.bank_api_client import BankApiClient

def test_fetch_transactions_returns_list():
    client = BankApiClient()
    assert isinstance(client.fetch_transactions("123"), list)
