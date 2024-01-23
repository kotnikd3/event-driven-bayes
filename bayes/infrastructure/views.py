from datetime import datetime

import matplotlib.pyplot as plt

from bayes.application_services.services import AbstractGraph
from bayes.domain.models import StatisticalModel


class MatplotlibGraph(AbstractGraph):
    def __init__(self, model: StatisticalModel):
        super().__init__(model)
        self.plt = plt

    def draw(self) -> None:
        self.plt.plot(
            self.model.p_grid,
            self.model.posterior,
            'o-',
            label='Posterior',
        )
        self.plt.plot(
            self.model.p_grid,
            self.model.prior / self.model.prior.sum(),
            "--",
            label='Prior',
        )

        w = self.model.parameters['w']
        n = self.model.parameters['n']
        points = len(self.model.prior)

        self.plt.xlabel('Proportion of w')
        self.plt.ylabel('Probability')
        self.plt.title(f'w: {w}, n: {n}, grid approx ({points} points)')
        self.plt.legend()

    def save(self, output_folder: str) -> None:
        now = datetime.now()
        date_str = now.strftime("%Y_%m_%d")
        time_str = now.strftime("%H_%M_%S")
        n = self.model.parameters['n']

        filename = f'{output_folder}/{n}_{date_str}_{time_str}.png'

        self.plt.savefig(filename)
