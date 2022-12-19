from unittest.mock import patch
import pytest
from main import get_careers_page, get_home_page, get_login_message

@patch('main.get_home_page')
def test_home_page(mock_login_message):
    mock_login_message.return_value = "home page"
    response = get_home_page()
    assert response == 'home page'