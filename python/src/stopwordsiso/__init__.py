# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2018-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Collection of stopwords for multiple languages.

Stopwords are retrieved by ISO 639-1 language code::

    import stopwordsiso

    stopwordsiso.has_lang("th")      # True - Thai is supported
    stopwordsiso.langs()             # frozenset of all supported codes
    stopwordsiso.stopwords("en")     # set of English stopwords
    stopwordsiso.stopwords(["de", "id", "zh"])  # combined stopwords

Source data and contribution:
    https://github.com/stopwords-iso/stopwords-iso

The MIT License (MIT)
Copyright (c) 2019 Arthit Suriyawongkul and Gene Diaz
"""

from importlib.metadata import PackageNotFoundError, version

from ._core import has_lang, langs, stopwords

try:
    __version__: str = version("stopwordsiso")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__ = [
    "__version__",
    "has_lang",
    "langs",
    "stopwords",
]
