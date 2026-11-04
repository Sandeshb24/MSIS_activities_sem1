import unittest
import numpy as np
from vector import Vector
import semantic_tagging as st


class TestTagging(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = st.load_model()
        cls.names, cls.T = st.build_tag_matrix(cls.model, st.TAGS)
        cls.tokens = ["research", "students", "zzqxvv", "innovation", "research"]
        cls.in_vocab, cls.oov, cls.W = st.build_text_matrix(cls.model, cls.tokens)
        cls.S_vec = st.similarity_matrix_vector_class(cls.W, cls.T)
        cls.S_np = st.similarity_matrix_numpy(cls.W, cls.T)

    def test_T_shape(self):
        self.assertEqual(self.T.shape, (20, 50))

    def test_W_shape(self):
        self.assertEqual(self.W.shape, (len(self.in_vocab), 50))

    def test_S_shape(self):
        self.assertEqual(self.S_np.shape, (len(self.in_vocab), 20))

    def test_pair_matches(self):
        i, j = 1, self.names.index("education")
        v = Vector(self.W[i]).cosine_similarity(Vector(self.T[j]))
        self.assertAlmostEqual(v, self.S_np[i, j], places=6)

    def test_allclose(self):
        self.assertTrue(np.allclose(self.S_vec, self.S_np))

    def test_oov_excluded(self):
        self.assertIn("zzqxvv", self.oov)
        self.assertNotIn("zzqxvv", self.in_vocab)
        self.assertEqual(self.W.shape[0], 4)

    def test_repeats_preserved(self):
        self.assertEqual(self.in_vocab.count("research"), 2)

    def test_bad_tag_raises(self):
        bad = st.TAGS[:19] + ["zzqxvv"]
        with self.assertRaises(ValueError):
            st.build_tag_matrix(self.model, bad)

    def test_identical_word_scores_one(self):
        ranking = st.rank_tags(self.names, self.S_np, self.in_vocab)
        top = dict((t, s) for t, s, _ in ranking)
        self.assertAlmostEqual(top["research"], 1.0, places=5)


if __name__ == "__main__":
    unittest.main()
