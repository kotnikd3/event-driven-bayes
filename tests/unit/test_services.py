from unittest import TestCase

from bayes.application_services.services import IncrementalLearner


class TestIncrementalLearner(TestCase):
    def setUp(self) -> None:
        self.model = IncrementalLearner()
