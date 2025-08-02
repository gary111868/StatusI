# test_statusim.py
"""
Tests for StatusIM module.
"""

import unittest
from statusim import StatusIM

class TestStatusIM(unittest.TestCase):
    """Test cases for StatusIM class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StatusIM()
        self.assertIsInstance(instance, StatusIM)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StatusIM()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
