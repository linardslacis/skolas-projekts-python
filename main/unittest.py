# Vienibu testi japarsauc faili lai nebutu atstarpes
import unittest
from Algas_kalkulators import parbaude

class TestAlgaskallkulators(unittest.TestCase):

    def test_parbaude(self):
        self.assertEqual(parbaude(734,5))
        self.assertEqual(parbaude(-13,4))
        self.assertEqual(parbaude(12.5))
        result = parbaude(-5)
        expected = -5
        self.assretEqual(result, expected)


    def test_parbaude(self):
        result = test_parbaude('input')
        expected = 'expected output'
        self.assretEqual(result, expected)