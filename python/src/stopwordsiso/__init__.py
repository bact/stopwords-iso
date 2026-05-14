# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2018-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: MIT

"""Collection of stopwords for multiple languages.

Stopwords are retrieved by ISO 639-1 language code::

    import stopwordsiso

    stopwordsiso.has_lang("th")                 # True - Thai is supported
    stopwordsiso.langs()                        # set of all supported codes
    stopwordsiso.stopwords("en")                # set of English stopwords
    stopwordsiso.stopwords(["de", "id", "zh"])  # combined stopwords

Source data and contribution:
    https://github.com/stopwords-iso/stopwords-iso
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
