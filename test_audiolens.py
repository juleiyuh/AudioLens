# test_audiolens.py
"""
Tests for AudioLens module.
"""

import unittest
from audiolens import AudioLens

class TestAudioLens(unittest.TestCase):
    """Test cases for AudioLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AudioLens()
        self.assertIsInstance(instance, AudioLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AudioLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
