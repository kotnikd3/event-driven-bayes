from unittest import TestCase

import numpy as np

from bayes.domain.models import BinomialModel


class TestBinomialModel(TestCase):
    def setUp(self) -> None:
        prior = np.repeat(1, 10)
        self.model = BinomialModel(prior=prior, w=0, n=0)

    def test_update(self):
        self.model.update()

        self.assertEqual(10, len(self.model.p_grid))
        self.assertEqual(10, len(self.model.posterior))

    def test_predict(self):
        self.model.update()  # First we need to .update()
        size = 30
        result = self.model.predict(size=size)

        self.assertTrue(isinstance(result, np.ndarray))
        self.assertEqual(size, len(result))
