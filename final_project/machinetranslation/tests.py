import unittest

from translator import englishToFrench, frenchToEnglish 

class Test_english_to_french (unittest.TestCase):
    def test_englishToFrench (self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)

class Test_french_to_english (unittest.TestCase):
    def test_frenchToEnglish (self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        self.assertNotEqual(frenchToEnglish("None"), '')
        self.assertNotEqual(frenchToEnglish(0), 0)



unittest.main()