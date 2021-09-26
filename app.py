import click
from pathlib import Path
from string import Template
import re

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
    if lang == 'node' or lang == 'python':
      template_data = template_data | get_data_from_component(lang)
    else:
      print('Language not supported')
  
  readme_template = Path(__file__).parent.joinpath('readme-template.md').read_text() 
  readme_output = Template(readme_template).safe_substitute(template_data)
  
  readme.write_text(readme_output)

def get_data_from_component(component_name):
  component = Path(__file__).parent.joinpath(f'./components/{component_name}.md')
  
  sections = {}

  with component.open() as file:
    current_section = ''
    for line in file:
      if line.startswith('#'):
        current_section = re.search('#+\s*(.+)\n', line).group(1)
        sections[current_section] = ''
      else:
        sections[current_section] += line

  title_mapping = {
    'Prerequisites': 'prereqs',
    'Installation': 'install',
    'Deployment': 'deploy'
  }

  component_data = {}

  for key, value in sections.items():
    template_key = title_mapping[key]
    component_data[template_key] = value.strip()

  return component_data