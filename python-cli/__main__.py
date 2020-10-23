import sys
import click

@click.group()
@click.version_option("1.0.0")
def main():
    pass

@main.command()
@click.argument('arg', type=click.Path(exists=True))
@click.option('-o', '--option', default="")
def funct(**kwargs):
    """

    """
    print(kwargs.get('arg'))
    print(kwargs.get('option'))


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("$ flask-cli funct -o=[option] [arg]")
    main()
