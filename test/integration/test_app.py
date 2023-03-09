import json

import requests


def test_hello_world():
    url = "http://lambda:8080/2015-03-31/functions/function/invocations"

    response = requests.post(url, json={})
    content = json.loads(response.content.decode("utf8"))

    assert response.ok
    assert content["statusCode"] == 200
    assert content["body"] == "Hello World"
