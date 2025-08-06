# test_inquirerprompts.py
"""
Tests for InquirerPrompts module.
"""

import unittest
from inquirerprompts import InquirerPrompts

class TestInquirerPrompts(unittest.TestCase):
    """Test cases for InquirerPrompts class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InquirerPrompts()
        self.assertIsInstance(instance, InquirerPrompts)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InquirerPrompts()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
