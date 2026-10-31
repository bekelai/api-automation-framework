import pytest
import requests

@pytest.fixture(scope="session")
def session():
    """整个测试会话共用一条连接"""
    s = requests.Session()
    yield s
    s.close()
