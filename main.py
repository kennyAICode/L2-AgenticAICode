import unittest

def normalize(text): return " ".join(text.lower().split())
class Tests(unittest.TestCase):
    def test_normalize(self): self.assertEqual(normalize("  Hello   AGENT "), "hello agent")
    def test_empty(self): self.assertEqual(normalize(""), "")

if __name__ == "__main__": unittest.main()
