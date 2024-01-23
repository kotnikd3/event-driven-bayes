import json

import numpy as np

from bayes.application_services.repositories import MemoryRepository
from bayes.domain.models import BinomialModel


class IncrementalLearner:
    def __init__(self, repository: MemoryRepository):
        # prior = np.repeat(1, points)
        # We can assume, that there is more than 10% of water
        prior = (np.linspace(0, 1, 120) > 0.1).astype(int)
        self.model = BinomialModel(prior=prior, w=0, n=0)
        self.repository = repository

    def update(self, trial: str) -> None:
        prior, w, n = self._get_previous_knowledge()

        if trial == 'w':
            w += 1
        n += 1

        self.model = BinomialModel(prior=prior, w=w, n=n)
        self.model.update()

        print(self.model)

        self._save_current_knowledge()

    def _get_previous_knowledge(self) -> tuple:
        # Get data from Redis
        if data := self.repository.get_data():
            deserialized_posterior = np.array(json.loads(data[b'posterior']))
            return deserialized_posterior, int(data[b'w']), int(data[b'n'])

        return (
            self.model.prior,
            self.model.parameters['w'],
            self.model.parameters['n'],
        )

    def _save_current_knowledge(self) -> None:
        # Save data to Redis
        serialized_posterior = json.dumps(self.model.posterior.tolist())

        data = {
            'posterior': serialized_posterior,
            'w': self.model.parameters['w'],
            'n': self.model.parameters['n'],
        }

        self.repository.save_data(data)
