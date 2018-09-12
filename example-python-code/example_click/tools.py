# coding: utf-8
"""
Usage: tools.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  cmd1
  command2
"""
import click

@click.group()
def cli():
    pass

@click.command('cmd1')
@click.option('-f','--file',default=None)
def command1(file):
    pass


@click.command()
@click.option('-f','--file',default=None)
@click.argument('date')
def command2(file,date):
    pass

cli.add_command(command1)
cli.add_command(command2)

def main():
    cli()

if __name__ == '__main__':
    main()