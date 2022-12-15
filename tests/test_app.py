from unittest.mock import patch
import pytest
from main import get_careers_page, get_home_page, get_login_message

@patch('cruds.login_message')
@pytest.mark.asyncio
async def test_login_page(mock_login_message):
    mock_login_message.return_value = "login page"
    response = await get_login_message()
    assert response == 'login page'