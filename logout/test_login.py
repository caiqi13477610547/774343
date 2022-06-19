import pytest
class TestLogin:
    def test_hello_001(self):
        print("test_hello_001")
    @pytest.mark.run(order=2)
    def test_hello_003(self):
        print("2")
    @pytest.mark.run(order=1)
    def test_hello_002(self):
        print("1")
if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
