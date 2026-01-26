import pytest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    """Flask test mijozini yaratish"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """
    Scenario 1: Farm Product Update Board test.
    Asosiy sahifa yuklanishi va mahsulotlar borligini tekshiradi.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Agricultural Product Platform" in response.data
    assert b"Daily product list is available" in response.data

def test_notification_system(client):
    """
    Scenario 2: Order Notification System test.
    Bildirishnoma yuborish endpointi ishlashini tekshiradi.
    """
    response = client.get('/notify')
    assert response.status_code == 200
    assert b"Notification sent" in response.data
    assert b"reliable" in response.data

def test_metrics_endpoint(client):
    """
    Scenario 4 & 5: Monitoring test.
    Prometheus metrikalari to'g'ri generatsiya qilinayotganini tekshiradi.
    """
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b"http_requests_total" in response.data