import click
from pathlib import Path

@click.command()
def cli():
  """README.md generator"""
  click.echo('Generating README.md')
  
  readme_template = Path('C:/Users/benpa/Documents/Projects/readme-generator/readme-template.md')
  readme = Path.cwd().joinpath('README.md')
  
  if readme.is_file():
    click.echo(f'README already exists: {readme}')
    return
  
  readme.write_text(readme_template.read_text())