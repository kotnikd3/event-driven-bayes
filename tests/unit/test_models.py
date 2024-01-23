from unittest import TestCase

import numpy as np

from bayes.domain.models import BinomialModel


class TestBinomialModel(TestCase):
    def setUp(self) -> None:
        prior = np.repeat(1, 10)
        self.model = BinomialModel(prior=prior, w=0, n=0)

    def test_update(self):
        assert 1 == 1
