import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

    
if __name__ == '__main__':
    unittest.main()
