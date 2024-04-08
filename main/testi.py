import unittest
from unittest.mock import patch
from menu_paligfunkcijas import *
from io import StringIO


class TestIevadesValidacija(unittest.TestCase):

    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')
    def test_valid_input(self, _mock_print, _mock_input):
        """Test that a valid input returns the correct float value."""
        result = ievades_validacija('Ievadiet skaitli: ', lambda x: x > 0, 'Jābūt lielākam par 0')
        self.assertEqual(result, 5.0)

    @patch('builtins.input', side_effect=['-1', '5'])
    @patch('builtins.print')
    def test_retry_on_invalid_condition(self, mock_print, _mock_input):
        result = ievades_validacija('Ievadiet skaitli: ', lambda x: x > 0, 'Jābūt lielākam par 0')
        self.assertEqual(result, 5.0)
        # Expect print to be called exactly once with the error message for the invalid condition
        self.assertEqual(mock_print.call_count, 1)

    @patch('builtins.input', side_effect=['not a number', '5'])
    @patch('builtins.print')
    def test_retry_on_non_numeric_input(self, mock_print, _mock_input):
        """Test that the function retries after a non-numeric input."""
        result = ievades_validacija('Ievadiet skaitli: ', lambda x: x > 0, 'Jābūt lielākam par 0')
        self.assertEqual(result, 5.0)
        # Since the first input is invalid (non-numeric), we expect at least
        # one call to print for the ValueError message, before a valid input is provided.
        self.assertTrue(mock_print.call_count >= 1)

        # Optionally, check that the specific error message for non-numeric input was printed.
        # This is useful if you want to ensure the user is provided with the correct feedback.
        mock_print.assert_any_call("Nederiga ievade. Ludzu, ievadiet derigu skaitlisko vertibu.")


class TestDstiAprekins(unittest.TestCase):
    def test_kk_between_one_and_two_point_five_without_apgadajamie(self):
        self.assertEqual(dsti_aprekins(1400, 0), 0.4)

    def test_kk_between_one_and_two_point_five_with_apgadajamie_and_high_dsti(self):
        self.assertEqual(dsti_aprekins(1400, 1), 0.35)

    def test_kk_between_one_and_two_point_five_with_apgadajamie_and_low_dsti(self):
        self.assertLess(dsti_aprekins(1750, 2), 0.4)

    def test_kk_equal_two_point_five(self):
        self.assertEqual(dsti_aprekins(1750, 0), 0.4)

    def test_kk_greater_than_two_point_five(self):
        self.assertEqual(dsti_aprekins(2100, 1), 0.4)

    def test_kk_in_very_high_range(self):
        self.assertEqual(dsti_aprekins(3500, 0), 0.4)

    def test_kk_less_than_two_point_five_but_close_and_high_dsti(self):
        self.assertEqual(dsti_aprekins(1749, 1), 0.35)
        # edge case def test_non_integer_values(self):
        self.assertEqual(dsti_aprekins(1500.5, 1), 0.35)
        # Assuming the function can handle float inputs


class TestHipotekaraMaksajumaAprekins(unittest.TestCase):
    def test_valid_case(self):
        self.assertEqual(hipotekara_maksajuma_aprekins(2000, 0.35, 150000, 30, 22500, 0.01), True)

    def test_invalid_case(self):
        self.assertEqual(hipotekara_maksajuma_aprekins(850, 0.1, 100000, 20, 10000, 0.01), False)


class TestNullesParbaude(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(nules_parbaude(2, 1, 1, -2, 3), 1)

    def test_case_2(self):
        self.assertEqual(nules_parbaude(1, 2, 1, -3, 2), 1)

    def test_case_3(self):
        self.assertEqual(nules_parbaude(2, 3, 2, 1, -6), 0)

    def test_case_4(self):
        self.assertEqual(nules_parbaude(16, 4, 1, -4, 0), 1)


class TestElastiba(unittest.TestCase):
    def test_vienadots_pieprasijums(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            elastiba(10, 20, 100, 200)
            self.assertEqual(mock_stdout.getvalue(), "Elastiba = |1|, pieprasijums ir vienadots\n")

    def test_neelastigs_pieprasijums(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            elastiba(5, 25, 2, 4)
            self.assertEqual(mock_stdout.getvalue(), "Elastiba = 0.25 , pieprasijums ir neelastigs\n")

    def test_elastigs_pieprasijums(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            elastiba(2, 4, 5, 25)
            self.assertEqual(mock_stdout.getvalue(), "Elastiba = 4.0 , pieprasijums ir elastigs\n")


class TestKoeficientm(unittest.TestCase):
    def test_pozitivivs_slipums(self):
        self.assertEqual(koeficientm(2, 4, 5, 9), (2, 1))

    def test_negativs_slipums(self):
        self.assertEqual(koeficientm(3, 5, 9, 5), (-2, 15))


class TestKrustpunkts(unittest.TestCase):
    def test_paralelas(self):
        self.assertEqual(krustpunkts(2, 3, 2, 5), None)

    def test_neparalelas(self):
        self.assertEqual(krustpunkts(2, 3, 4, 5), (-1.0, 1.0))


class TestPagarinajumsPaKreisi(unittest.TestCase):
    def test_l1_ir_nulle(self):
        self.assertEqual(pagarinajums_pa_kreisi(1, 0, 2), 2)

    def test_l1_nav_nulle(self):
        self.assertEqual(pagarinajums_pa_kreisi(1, 3, 2), -1)


class TestPagarinajumsPaLabi(unittest.TestCase):
    def test_l1_ir_2lim(self):
        self.assertEqual(pagarinajums_pa_labi(1, 4, 3, 2), 3)

    def test_l1_nav_2lim(self):
        self.assertEqual(pagarinajums_pa_labi(1, 8, 3, 2), -1)


class TestSalidzinasana(unittest.TestCase):
    def test_t_smaller_than_zero(self):
        self.assertEqual(salidzinasana(-1, 5), 1)

    def test_t_bigger_than_v(self):
        self.assertEqual(salidzinasana(2, 1), 1)
        self.assertEqual(salidzinasana(2, 0.5), 1)
        self.assertEqual(salidzinasana(2.4, 0.5), 1)
        self.assertEqual(salidzinasana(-1, -2), 1)

    def test_t_equal_zero(self):
        self.assertEqual(salidzinasana(0, 1), 1)

    def test_return_zero(self):
        self.assertEqual(salidzinasana(1, 2), 0)


class TestAugstakaCenaFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=["100"])
    def test_augstaka_cena_valid_input(self, _mock_input):
        # Test case: Valid input
        result = augstaka_cena()
        self.assertEqual(result, 100)

    @patch('builtins.input', side_effect=["abc", "-10", "0", "100"])
    def test_augstaka_cena_invalid_inputs(self, _mock_input):
        # Test case: Invalid inputs
        with patch('builtins.print') as mock_print:
            result = augstaka_cena()
            self.assertEqual(result, 100.0)
            self.assertEqual(mock_print.call_count, 3)
            mock_print.assert_any_call("Ievadita nepareiza vertiba")
            mock_print.assert_any_call("Augstaka cena nevar but vienada vai mazaka par 0")
