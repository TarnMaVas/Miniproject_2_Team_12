import unittest
from initial_solution import dyvo_insert


class TestDyvoInsert(unittest.TestCase):
    def test_single_word_with_flag(self):
        sentence = "Кицька"
        flag = "ки"
        expected_result = "Дивокицька"
        self.assertEqual(dyvo_insert(sentence, flag), expected_result)

    def test_multiple_words_with_flag(self):
        sentence = "Кицька купила кита."
        flag = "ки"
        expected_result = "Дивокицька купила дивокита."
        self.assertEqual(dyvo_insert(sentence, flag), expected_result)

    def test_multiple_words_without_flag(self):
        sentence = "Собака грається у саду."
        flag = "ки"
        expected_result = "Собака грається у саду."
        self.assertEqual(dyvo_insert(sentence, flag), expected_result)

    def test_empty_sentence(self):
        sentence = ""
        flag = "ки"
        expected_result = ""
        self.assertEqual(dyvo_insert(sentence, flag), expected_result)

    def test_case_insensitive_flag(self):
        sentence = "Кицька купила кита."
        flag = "КИ"
        expected_result = "Дивокицька купила дивокита."
        self.assertEqual(dyvo_insert(sentence, flag), expected_result)

    def test_sentence_with_punctuation(self):
        sentence = "Кит кота по хвилях катав - кит у воді, кіт на киті."
        flag = "ки"
        expected_result = "Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті."
        self.assertEqual(dyvo_insert(sentence, flag), expected_result)

    def test_long_sentence(self):
        sentence = "Кицька купила кита. Собака грається у саду. Кот на дивокиті."
        flag = "ки"
        expected_result = "Дивокицька купила дивокита. Собака грається у саду. Кот на дивокиті."
        self.assertEqual(dyvo_insert(sentence, flag), expected_result)

    def test_sentence_with_non_uppercase_first_letter(self):
        sentence = "кіцька купила кітаків."
        flag = "кі"
        expected_result = "дивокіцька купила дивокітаків."
        self.assertEqual(dyvo_insert(sentence, flag), expected_result)

    def test_non_string_sentence(self):
        self.assertIsNone(dyvo_insert(123, "ки"))

    def test_non_string_flag(self):
        self.assertIsNone(dyvo_insert("Кицька купила кітаків.", 123))

if __name__ == "__main__":
    unittest.main()
