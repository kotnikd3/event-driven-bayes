import numpy as np
import scipy.stats as stats
from abc import ABC, abstractmethod


class StatisticalModel(ABC):
    @abstractmethod
    def __init__(self, prior, **parameters):
        self.prior = prior
        self.parameters = parameters

        self.p_grid = None
        self.posterior = None

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def predict(self, size: int):
        raise NotImplementedError


class BinomialModel(StatisticalModel):
    def __init__(self, prior, w: int, n: int):
        super().__init__(prior, w=w, n=n)

    def update(self) -> None:
        self.p_grid = np.linspace(0, 1, len(self.prior))

        likelihood_pmf = stats.binom.pmf(
            self.parameters['w'],
            self.parameters['n'],
            self.p_grid,
        )

        unstd_posterior = likelihood_pmf * self.prior
        self.posterior = unstd_posterior / unstd_posterior.sum()

    def predict(self, size: int = 10000) -> np.ndarray:
        posterior_samples = np.random.choice(
            self.p_grid,
            p=self.posterior,
            size=size,
            replace=True,
        )

        return stats.binom.rvs(n=self.parameters['n'], p=posterior_samples)

    def __str__(self):
        return f'w: {self.parameters["w"]}, n: {self.parameters["n"]}'
