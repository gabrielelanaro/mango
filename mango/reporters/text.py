import click
from .utils import render_tree

class TextReporter:

    def log(self, value):
        header = click.style('LOG', fg='green', bold=True)
        print(f"{header}: {value}")

    def add_scalar(self, name, value, iteration):
        header = click.style('SCALAR', fg='green', bold=True)
        print(f"{header}[it={iteration: 6}] {name}: {value: 10}")

    def add_parameters(self, parameters):
        print(click.style("PARAMETERS", fg='green', bold=True))
        print(render_tree(parameters))
