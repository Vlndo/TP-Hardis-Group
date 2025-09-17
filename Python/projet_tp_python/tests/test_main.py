from my_package import http_get

def test_http_get() :
    data = http_get()
    assert 'products' in data
    assert len(data["products"]) > 0