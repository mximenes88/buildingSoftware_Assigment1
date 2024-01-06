import argparse
import yaml


CONFIG_PATHS = ['system_config.yml', 'user_config.yml']

parser = argparse.ArgumentParser()
parser.add_argument('job_config', type=str)
args = parser.parse_args()

paths_to_load = CONFIG_PATHS + [args.job_config]

# initialize empty dictionary to hold the configuration
config = {}

# load each config file and update the config dictionary
for path in paths_to_load:
    print ('loading ' + path)
    with open(path, 'r') as f:
      this_config = yaml.safe_load(f)
    config.update(this_config)

print(config)




