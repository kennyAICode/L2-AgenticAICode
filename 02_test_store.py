import unittest
from tfidf_store import VectorStore


class StoreTests(unittest.TestCase):
    def test_python_query_ranks_python_document_first(self):
        docs = ["Python has functions", "Agents use tools"]
        result = VectorStore(docs).search("Python function", top_k=1)
        self.assertEqual(result[0][1], docs[0])


if __name__ == "__main__":
    unittest.main()

