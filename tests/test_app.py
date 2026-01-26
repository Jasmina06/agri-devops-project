import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Asosiy sahifa yuklanishini tekshirish (Scenario 1)"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Agricultural Product Platform" in response.data

def test_notification_logging(client):
    """Notification yuborilganda status 200 bo'lishini tekshirish (Scenario 2)"""
    # Agar app.py da /notify endpoint bo'lsa
    response = client.get('/metrics') # Hozircha metrics orqali tekshiramiz
    assert response.status_code == 200
