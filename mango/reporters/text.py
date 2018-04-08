import click


class TextReporter:

    def log(self, value):
        header = click.style('LOG', fg='green', bold=True)
        click.echo(f"{header}: {value}")

    def add_scalar(self, name, value, iteration):
        header = click.style('SCALAR', fg='green', bold=True)
        click.echo(f"{header}[it={iteration: 9}] {name}: {value: 10}")
