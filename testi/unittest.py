# Vienibu testi japarsauc faili lai nebutu atstarpes
import unittest
from Algaskalkulators import parbaude

class TestAlgaskallkulators(unittest.TestCase):

    def test_parbaude(self):
        self.assertEqual(parbaude(734,5))
        self.assertEqual(parbaude(-13,4))
        self.assertEqual(parbaude(12.5))

    def test_parbaude1(self):
        result = test_parbaude1('input')
        expected = 'expected output'
        self.assretEqual(result, expected)