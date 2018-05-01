import click
from pydoc import locate


@click.group()
def cli():
    pass


@cli.command()
@click.argument('experiment')
@click.argument('param', nargs=-1)
def train(experiment, param):
    Experiment = locate(experiment)
    if Experiment is None:
        click.echo(f'Class {experiment} not found')
        return

    exp = Experiment.create(param)
    exp.run()


if __name__ == '__main__':
    cli()
