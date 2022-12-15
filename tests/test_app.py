from unittest.mock import patch
import pytest
from main import get_careers_page, get_home_page, get_login_message

@patch('main.login_message')
def test_login_page(mock_login_message):
    mock_login_message.return_value = "login page"
    response = get_login_message()
    assert response == 'login page'