import unittest
import time
from my_package.main import format_url
from my_package.main import ThresholdExceededException

# Exo 4
class Test_format_rul(unittest.TestCase):

    # Test valide et invalide pour la partie protocole de l'url

    def test_valid_protocol(self):
        self.assertEqual(format_url("https","google.com","/fr"), "https://google.com/fr")
    
    def test_invalid_protocol(self):
        with self.assertRaises(Exception):
            format_url("htt","google.com", "/fr")

    # Test valide et invalide pour la partie hostname de l'url

    def test_valid_hostname(self):
        self.assertEqual(format_url("https","google.com","/fr"), "https://google.com/fr")
    
    def test_invalid_hostname(self):
        with self.assertRaises(Exception):
            format_url('https','google .com','/fr')

    # Test valide et invalide pour la partie uri de l'url

    def test_valid_uri(self):
        self.assertEqual(format_url("https","google.com","/fr"), "https://google.com/fr")
    
    def test_invalid_uri(self):
        with self.assertRaises(Exception):
            format_url("https","google.com","fr")

#Exo 6 - Test
class TestThresholdExceededException(unittest.TestCase):
    def test_exception_is_raised(self):
        threshold = 2
        elapsed = 3 

        with self.assertRaises(ThresholdExceededException) as context:
            if elapsed > threshold:
                raise ThresholdExceededException(threshold, elapsed)

        self.assertEqual(
            str(context.exception), 
            "Temps d'exécution de 3.00s dépassé (seuil: 2s)."
            )
    

if __name__ == "__main__":
    unittest.main()