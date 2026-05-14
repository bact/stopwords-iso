#!/usr/bin/env python3
"""Generates a table of ISO 639-1:2002 languages and appends it to README.md."""

import json
import time
import urllib.request
from functools import cached_property
from html.parser import HTMLParser
from pathlib import Path

_HERE = Path(__file__).parent
_STOPWORDS_JSON = _HERE / "src" / "stopwordsiso" / "stopwords-iso.json"
_README = _HERE / "README.md"
_ISO_639_URL = "https://www.loc.gov/standards/iso639-2/php/code_list.php"


class ISO6391TableParser(HTMLParser):
    """Parse the ISO 639-1 code table from the Library of Congress HTML page."""

    def __init__(self) -> None:
        super().__init__()
        self._in_tr: bool = False
        self._in_td: bool = False
        self._code_flag: bool = False
        self._country_flag: bool = False
        self._tdc: int = 0
        self._codes: list[str] = []
        self._names: list[str] = []

    @cached_property
    def code_to_name(self) -> dict[str, str]:
        """Return a mapping of ISO 639-1 code to language name."""
        return {
            code: name
            for code, name in zip(self._codes, self._names)
            if code.isalpha() and code.islower()
        }

    def _reset_tdc(self) -> None:
        self._tdc = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "tr":
            self._in_tr = True
            self._code_flag = self._country_flag = False
        elif self._in_tr and tag == "td":
            self._in_td = True
            self._code_flag = self._tdc == 1
            self._country_flag = self._tdc == 2
            self._tdc += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "tr":
            self._in_tr = False
            self._reset_tdc()
        elif tag == "td":
            self._in_td = False

    def handle_data(self, data: str) -> None:
        if self._in_td:
            if self._code_flag:
                self._codes.append(data)
            elif self._country_flag:
                self._names.append(data)


def tabulate() -> int:
    """Fetch the ISO 639-1 table and append a language coverage table to README.md."""
    headers = {"User-Agent": "stopwords-iso/stopwords-iso"}
    req = urllib.request.Request(_ISO_639_URL, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("latin-1")

    parser = ISO6391TableParser()
    parser.feed(html)

    sw: dict[str, list[str]] = json.loads(_STOPWORDS_JSON.read_text(encoding="utf-8"))

    check = "\u2713"
    rows = [
        "| ISO 639-1 Code | Language | Included Here |",
        "| -------------- | -------- | ------------- |",
        *(
            f"| {code} | {name} | {check if code in sw else ''} |"
            for code, name in parser.code_to_name.items()
        ),
    ]
    table = "\n".join(rows)

    readme = _README.read_text(encoding="utf-8")
    readme += f"""
### List of Included Languages

_Last updated: {time.ctime()}_

This table lists the entire set of ISO 639-1:2002 codes, with a check
mark indicating those language codes that are found in `stopwords-iso.json`.

The list of codes itself is from [www.loc.gov]({_ISO_639_URL}), which is
the official "language codes list" and is linked to from
[www.iso.org](https://www.iso.org/iso-639-language-codes.html).

{table}
"""
    return _README.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    tabulate()
