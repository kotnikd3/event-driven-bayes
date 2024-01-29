from unittest import TestCase

import numpy as np

from bayes.domain.models import BinomialModel
from bayes.infrastructure.views import MatplotlibGraph


class TestMatplotlibGraph(TestCase):
    def setUp(self):
        prior = (np.linspace(0, 1, 120) > 0.1).astype(int)
        self.model = BinomialModel(prior=prior, w=0, n=0)
        self.model.update()

    def test_draw(self):
        graph = MatplotlibGraph(model=self.model)
        graph.draw()
        self.assertTrue(graph.plt)
