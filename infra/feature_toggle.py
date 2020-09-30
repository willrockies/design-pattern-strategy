import yaml

def get_toggle(name):
  with open('feature-toggles.yml', 'r') as file:
    configs = yaml.load(file)
    return configs[name]