import unittest

from translator import englisth_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englisth_to_french('Hi'), 'Salut') # test when Hi is given as input the output is Salut.
        self.assertEqual(englisth_to_french('None'), ' ') # test when null is given as input the output is null.
        self.assertEqual(englisth_to_french('Bye'), 'Au revoir') # test when Bye is given as input the output is Au revoir.
        self.assertEqual(englisth_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Salut'), {'translations': [{'translation': 'Hi'}], 'word_count': 1, 'character_count': 5}) # test when Salut is given as input the output is Hi.
        self.assertNotEqual(french_to_english('Au revoir'), 'Bye')  # test when Au revoir is given as input the output is not Bye.
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')
             
unittest.main()
