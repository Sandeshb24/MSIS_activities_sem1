import math
import unittest
from vector import Vector


class TestMean(unittest.TestCase):
    def test_known_value(self):
        self.assertAlmostEqual(Vector([1, 2, 3, 4]).mean(), 2.5)

    def test_constant_vector(self):
        self.assertAlmostEqual(Vector([5, 5, 5]).mean(), 5.0)

    def test_scaling(self):  # mean(c v) = c mean(v)
        v = Vector([1, 4, 9])
        self.assertAlmostEqual(v.scale(3).mean(), 3 * v.mean())

    def test_additivity(self):  # mean(u+v) = mean(u)+mean(v)
        u, v = Vector([1, 2, 3]), Vector([4, -1, 0])
        self.assertAlmostEqual(u.add(v).mean(), u.mean() + v.mean())

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            Vector([]).mean()


class TestDemean(unittest.TestCase):
    def test_known_value(self):
        d = Vector([1, 2, 3]).demean()
        for a, b in zip(d, (-1, 0, 1)):
            self.assertAlmostEqual(a, b)

    def test_mean_is_zero(self):
        self.assertAlmostEqual(Vector([3, -7, 12, 0.5]).demean().mean(), 0.0)

    def test_returns_new_vector(self):
        v = Vector([1, 2, 3])
        d = v.demean()
        self.assertIsNot(d, v)
        self.assertEqual(v.entries, (1.0, 2.0, 3.0))

    def test_constant_gives_zero(self):
        self.assertTrue(all(abs(x) < 1e-12 for x in Vector([4, 4, 4]).demean()))

    def test_idempotent(self):
        d = Vector([1, 5, 9]).demean()
        for a, b in zip(d, d.demean()):
            self.assertAlmostEqual(a, b)

    def test_shift_invariance(self):  # demean(v + c1) = demean(v)
        v = Vector([1, 2, 6])
        shifted = Vector(x + 10 for x in v)
        for a, b in zip(v.demean(), shifted.demean()):
            self.assertAlmostEqual(a, b)


class TestStd(unittest.TestCase):
    def test_known_value(self):
        # [2,4,4,4,5,5,7,9] has population std 2
        self.assertAlmostEqual(Vector([2, 4, 4, 4, 5, 5, 7, 9]).std(), 2.0)

    def test_constant_is_zero(self):
        self.assertAlmostEqual(Vector([3, 3, 3]).std(), 0.0)

    def test_nonnegative(self):
        self.assertGreaterEqual(Vector([-5, 2, 8]).std(), 0)

    def test_shift_invariance(self):
        v = Vector([1, 2, 3, 10])
        self.assertAlmostEqual(Vector(x + 100 for x in v).std(), v.std())

    def test_scale_property(self):  # std(c v) = |c| std(v)
        v = Vector([1, 2, 3, 10])
        self.assertAlmostEqual(v.scale(-3).std(), 3 * v.std())

    def test_norm_relation(self):  # std = ||demean|| / sqrt(n)
        v = Vector([1, 2, 3, 10])
        self.assertAlmostEqual(v.std(), v.demean().norm() / math.sqrt(len(v)))


if __name__ == "__main__":
    unittest.main()
