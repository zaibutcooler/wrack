# test_demo.py
import unittest


class TestRequirements(unittest.TestCase):

    def test_read(self):
        with open("./requirements.txt", "r") as f:
            packages = f.readlines()
            assert len(packages) > 0


if __name__ == "__main__":
    unittest.main()
