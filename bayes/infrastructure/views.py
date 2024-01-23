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
        n = self.model.parameters['n']
        w = self.model.parameters['w']

        filename = f'{output_folder}/n_{n}_w_{w}.png'

        self.plt.savefig(filename)
