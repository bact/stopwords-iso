# stopwordsiso

[![PyPI - Version](https://img.shields.io/pypi/v/stopwordsiso)](https://pypi.org/project/stopwordsiso/)
![GitHub License](https://img.shields.io/github/license/stopwords-iso/stopwords-iso)

Collection of stopwords for multiple languages, using ISO 639-1 language code.

This Python package is based on [Stopwords ISO][stopwords-iso] project by
Gene Diaz. You can see the full list of stopwords in every language available
there. Contribution to the word lists should also happen there.

Comparable packages also published on
[npm](https://www.npmjs.com/stopwords-iso) and
[bower](https://bower.io).

[stopwords-iso]: https://github.com/stopwords-iso/stopwords-iso

## Installation

```sh
pip install stopwordsiso
```

## Usage

```python
import stopwordsiso

stopwordsiso.has_lang("th")  # True if there are stopwords for Thai
stopwordsiso.langs()  # frozenset of all supported ISO 639-1 language codes
```

```python
from stopwordsiso import stopwords

stopwords("en")  # English stopwords
stopwords(["de", "id", "zh"])  # German, Indonesian, and Chinese stopwords
stopwords("xxx")  # an empty set will be returned for unknown language
```

## Stopwords data

The entire collection is in JSON format and can be found at
[`stopwords-iso.json`][stopwords-iso.json] in your `stopwordsiso/`
Python package directory.
You are free to use this collection any way you like.

[stopwords-iso.json]: https://raw.githubusercontent.com/stopwords-iso/stopwords-iso/master/stopwords-iso.json

Stopwords for each language is a list value with a key of respective language
in ISO 639-1 language code, like this:

```json
{
    "af": [ "aan", "af", "al", "as", ],
    "ar": [ "آض", "آمينَ", "آه", "آهاً", ],
}
```

If you wish to add, remove, or update some of the stopwords,
please go to **Stopwords ISO** project at <https://github.com/stopwords-iso>.

## Credits

- Gene Diaz, stopwords compilation, npm and bower packages
- Arthit Suriyawongkul, Python utility and pip package
  (was originally at <https://github.com/wisesight/stopwords-iso>)
- All stopwords sources are listed at
  <https://github.com/stopwords-iso/stopwords-iso/blob/master/CREDITS.md>.
- Get the latest list of stopwords at
  <https://github.com/stopwords-iso/stopwords-iso>.
