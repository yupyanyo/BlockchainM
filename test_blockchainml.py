# test_blockchainml.py
"""
Tests for BlockchainML module.
"""

import unittest
from blockchainml import BlockchainML

class TestBlockchainML(unittest.TestCase):
    """Test cases for BlockchainML class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainML()
        self.assertIsInstance(instance, BlockchainML)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainML()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
