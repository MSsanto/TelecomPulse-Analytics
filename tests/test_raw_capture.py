import pytest

from telecom_pulse.raw_capture import RawCaptureError, _looks_like_block_page, _validate_source_url


def test_official_source_requires_anatel_https():
    _validate_source_url("https://www.anatel.gov.br/dadosabertos/example.csv")

    with pytest.raises(RawCaptureError, match="HTTPS"):
        _validate_source_url("http://www.anatel.gov.br/example.csv")

    with pytest.raises(RawCaptureError, match="unexpected source host"):
        _validate_source_url("https://example.com/example.csv")


def test_waf_block_page_is_detected():
    payload = (
        "Por questões de segurança, esta operação no sistema foi bloqueada. "
        "Código de bloqueio: 123"
    ).encode()
    assert _looks_like_block_page(payload, "text/html; charset=utf-8")


def test_csv_like_payload_is_not_a_block_page():
    payload = b"UF;Grupo;Acessos\nSP;EXEMPLO;10\n"
    assert not _looks_like_block_page(payload, "text/csv")


def test_html_without_block_marker_is_not_misclassified():
    payload = b"<html><body>dataset catalog</body></html>"
    assert not _looks_like_block_page(payload, "text/html")
