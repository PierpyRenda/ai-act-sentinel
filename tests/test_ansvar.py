import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import patch
import urllib.error


def _make_mock_response(text: str):
    import json
    from io import BytesIO
    payload = json.dumps({
        "result": {"content": [{"text": text}]}
    }).encode("utf-8")
    mock = type("MockResp", (), {
        "read": lambda self: payload,
        "__enter__": lambda self: self,
        "__exit__": lambda self, *a: False,
    })()
    return mock


def test_lookup_article_success():
    from tools.ansvar import lookup_article
    with patch("urllib.request.urlopen", return_value=_make_mock_response("Article 5 text here")):
        result = lookup_article("5")
    assert "Article 5" in result

def test_lookup_article_network_error():
    from tools.ansvar import lookup_article
    with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("timeout")):
        result = lookup_article("5")
    assert "unavailable" in result.lower() or "[Ansvar" in result

def test_search_act_success():
    from tools.ansvar import search_act
    with patch("urllib.request.urlopen", return_value=_make_mock_response("Prohibited practices results")):
        result = search_act("prohibited practices")
    assert "Prohibited" in result

def test_search_act_network_error():
    from tools.ansvar import search_act
    with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("connection refused")):
        result = search_act("something")
    assert "unavailable" in result.lower() or "[Ansvar" in result

def test_get_obligations_for_role_success():
    from tools.ansvar import get_obligations_for_role
    with patch("urllib.request.urlopen", return_value=_make_mock_response("Provider obligations: Art. 9, Art. 16...")):
        result = get_obligations_for_role("provider")
    assert "provider" in result.lower() or "Art." in result

def test_get_obligations_for_role_network_error():
    from tools.ansvar import get_obligations_for_role
    with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("unreachable")):
        result = get_obligations_for_role("deployer")
    assert "unavailable" in result.lower() or "[Ansvar" in result

def test_get_definition_success():
    from tools.ansvar import get_definition
    with patch("urllib.request.urlopen", return_value=_make_mock_response("AI system means a machine-based system...")):
        result = get_definition("AI system")
    assert "machine" in result.lower() or len(result) > 0

def test_get_definition_network_error():
    from tools.ansvar import get_definition
    with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("dns failure")):
        result = get_definition("provider")
    assert "unavailable" in result.lower() or "[Ansvar" in result

def test_all_functions_return_strings():
    from tools.ansvar import lookup_article, search_act, get_obligations_for_role, get_definition
    with patch("urllib.request.urlopen", side_effect=urllib.error.URLError("offline")):
        assert isinstance(lookup_article("5"), str)
        assert isinstance(search_act("high risk"), str)
        assert isinstance(get_obligations_for_role("provider"), str)
        assert isinstance(get_definition("AI system"), str)
