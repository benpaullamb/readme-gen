import click
from pathlib import Path
from string import Template

@click.command()
@click.option('--lang', default=None, help='Node or Python')
def cli(lang):
  """README.md generator"""
  click.echo('Generating README.md')

  template_data = {
    'title': '',
    'prereqs': '',
    'install': '',
    'deploy': ''
  }

  readme = Path.cwd().joinpath('README.md')

  if readme.is_file():
    click.echo(f'README already exists: {readme}')
    return
  
  template_data['title'] = readme.parts[-2]
  
  if lang is not None:
    template_data = template_data | get_data_from_component(lang.lower())
  
  readme_template = Path('C:/Users/benpa/Documents/Projects/readme-generator/readme-template.md').read_text()
  readme_output = Template(readme_template).safe_substitute(template_data)
  
  readme.write_text(readme_output)

def get_data_from_component(component):
  return {
    'prereqs': '- Node'
  }