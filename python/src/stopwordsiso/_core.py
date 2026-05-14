# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2018-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: MIT

"""Core implementation for stopwordsiso.

All language codes follow the ISO 639-1 standard.
"""

import json
from collections.abc import Iterable
from importlib.resources import files

# Mapping from ISO 639-1 language code to list of stopwords.
_data_file = files("stopwordsiso").joinpath("stopwords-iso.json")
_text = _data_file.read_text(encoding="utf-8")
_STOPWORDS_ALL: dict[str, list[str]] = json.loads(_text)
del _data_file, _text

# Frozenset of all supported language codes.
_LANGS: frozenset[str] = frozenset(_STOPWORDS_ALL.keys())


def langs() -> frozenset[str]:
    """Return the set of supported language codes.

    Returns
    -------
    frozenset[str]
        All supported language codes in ISO 639-1 format.
    """
    return _LANGS


def has_lang(lang: str) -> bool:
    """Check whether stopwords are available for a language.

    Parameters
    ----------
    lang : str
        A language code to check, in ISO 639-1 format.

    Returns
    -------
    bool
        ``True`` if stopwords are available for *lang*, ``False`` otherwise.
    """
    return lang.lower() in _LANGS


def stopwords(lang: str | Iterable[str]) -> set[str]:
    """Return combined stopwords for one or more languages.

    Parameters
    ----------
    lang : str | Iterable[str]
        A single ISO 639-1 language code, or an iterable of language codes.
        An empty set is returned for any unknown code.

    Returns
    -------
    set[str]
        Union of stopwords for every requested language.

    Examples
    --------
    >>> from stopwordsiso import stopwords
    >>> isinstance(stopwords("en"), set)
    True
    >>> stopwords("xxx")
    set()
    >>> len(stopwords(["de", "id", "zh"])) > 0
    True
    """
    if isinstance(lang, str):
        lang = lang.lower()
        if has_lang(lang):
            return set(_STOPWORDS_ALL[lang])
        return set()

    words: set[str] = set()
    for code in lang:
        code = code.lower()
        if has_lang(code):
            words.update(_STOPWORDS_ALL[code])

    return words
