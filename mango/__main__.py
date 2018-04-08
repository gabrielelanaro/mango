import click
from pydoc import locate


@click.group()
def cli():
    pass

@cli.command()
@click.argument('experiment')
def train(experiment):
    Experiment = locate(experiment)
    if Experiment is None:
        click.echo(f'Class {experiment} not found')
        return

    exp = Experiment()
    exp.dataset.load()
    exp.model.initialize()
    exp.trainer.train()

if __name__ == '__main__':
    cli()
