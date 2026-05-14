# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2026-present Arthit Suriyawongkul
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for stopwordsiso."""

import unittest

import stopwordsiso
from stopwordsiso import has_lang, langs, stopwords

# pylint: disable=missing-function-docstring


class TestLangs(unittest.TestCase):
    """Tests for langs()."""

    def test_returns_frozenset(self) -> None:
        result = langs()
        self.assertIsInstance(result, frozenset)

    def test_nonempty(self) -> None:
        self.assertGreater(len(langs()), 0)

    def test_contains_known_codes(self) -> None:
        supported = langs()
        for code in ("ar", "en", "de", "ja", "zh"):
            with self.subTest(code=code):
                self.assertIn(code, supported)

    def test_does_not_contain_unknown_code(self) -> None:
        self.assertNotIn("xx", langs())


class TestHasLang(unittest.TestCase):
    """Tests for has_lang()."""

    def test_known_language_returns_true(self) -> None:
        self.assertTrue(has_lang("en"))
        self.assertTrue(has_lang("th"))

    def test_unknown_language_returns_false(self) -> None:
        self.assertFalse(has_lang("xx"))

    def test_empty_string_returns_false(self) -> None:
        self.assertFalse(has_lang(""))

    def test_case_insensitive(self) -> None:
        # ISO 639-1 codes are lowercase,
        # but has_lang() normalizes input to be case-insensitive
        self.assertTrue(has_lang("EN"))


class TestStopwords(unittest.TestCase):
    """Tests for stopwords()."""

    def test_single_language_returns_set(self) -> None:
        result = stopwords("en")
        self.assertIsInstance(result, set)

    def test_single_language_nonempty(self) -> None:
        self.assertGreater(len(stopwords("en")), 0)

    def test_unknown_language_returns_empty_set(self) -> None:
        self.assertEqual(stopwords("xxx"), set())

    def test_empty_list_returns_empty_set(self) -> None:
        self.assertEqual(stopwords([]), set())

    def test_list_of_languages(self) -> None:
        combined = stopwords(["de", "id", "zh"])
        de_only = stopwords("de")
        id_only = stopwords("id")
        zh_only = stopwords("zh")
        self.assertEqual(combined, de_only | id_only | zh_only)

    def test_list_with_unknown_code_ignored(self) -> None:
        result = stopwords(["en", "xxx"])
        self.assertEqual(result, stopwords("en"))

    def test_generator_input(self) -> None:
        # stopwords() accepts any iterable, including a generator
        result = stopwords(code for code in ["en", "de"])
        self.assertEqual(result, stopwords(["en", "de"]))

    def test_returns_new_set_each_call(self) -> None:
        a = stopwords("en")
        b = stopwords("en")
        self.assertIsNot(a, b)

    def test_words_are_strings(self) -> None:
        for word in stopwords("en"):
            with self.subTest(word=word):
                self.assertIsInstance(word, str)


class TestPackageMetadata(unittest.TestCase):
    """Tests for package-level attributes."""

    def test_version_is_string(self) -> None:
        self.assertIsInstance(stopwordsiso.__version__, str)

    def test_version_nonempty(self) -> None:
        self.assertNotEqual(stopwordsiso.__version__, "")

    def test_all_exports_present(self) -> None:
        for name in stopwordsiso.__all__:
            with self.subTest(name=name):
                self.assertTrue(hasattr(stopwordsiso, name))


if __name__ == "__main__":
    unittest.main()
