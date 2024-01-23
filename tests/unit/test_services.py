from unittest import TestCase

from bayes.application_services.services import IncrementalLearner
from tests.conftest import FakeMemoryRepository


class TestIncrementalLearner(TestCase):
    def setUp(self):
        self.learner = IncrementalLearner(FakeMemoryRepository())

    def test_update(self):
        self.learner.update('w')
        self.learner.update('w')

        self.assertEqual(2, self.learner.model.parameters['w'])
        self.assertEqual(2, self.learner.model.parameters['n'])

        self.learner.update('l')
        self.learner.update('SOMETHING')

        self.assertEqual(2, self.learner.model.parameters['w'])
        self.assertEqual(4, self.learner.model.parameters['n'])
