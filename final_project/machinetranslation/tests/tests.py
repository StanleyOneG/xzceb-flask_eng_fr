
import unittest

from translator import french_to_english, english_to_french

class TestFr2En(unittest.TestCase):
    def test_french(self):
        self.assertIsNotNone(french_to_english())
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        
class TestEn2Fr(unittest.TestCase):
    def test_english(self):
        self.assertIsNotNone(english_to_french())
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        
if __name__ == "__main__":
    unittest.main()
    