import pytest
class TestLogin:
    @pytest.fixture(params=[1,2,3])
    def befor(self,request):
        print(request.param +5)
    def test_login(self,befor):
        print("login")
if __name__ == '__main__':
    pytest.main(["-s","test_02.py"])
