# test_demo.py
import unittest
from wrack.data_prep import load_data


class TestDataset(unittest.TestCase):

    def test_download(self):
        result = load_data()
        assert len(result) > 0


if __name__ == "__main__":
    unittest.main()
