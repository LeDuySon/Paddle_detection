import yaml
import argparse
import os

parser = argparse.ArgumentParser(description='Change config for evaluation')
parser.add_argument('--config_path', type=str, required=True,
                    help='path to config file')

parser.add_argument('--data_path', type=str, required=True, help='path to your own dataset')
args = parser.parse_args()

config_path = args.config_path.split("/")
def read_yaml_file(files):
    config = None
    with open(files, 'r') as stream:
        try:
           # config = yaml.load(stream, Loader=yaml.BaseLoader)
            config = yaml.load(stream)
            print("READ YAML")
        except yaml.YAMLError as exc:
            print(exc)
    return config

def write_yaml_file(files, data):
    with open(files, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

def change_dataset_dir(base_list):
    for idx in range(len(base_list)):
        if("datasets" in base_list[idx]):
            base_list[idx] = args.data_path
    return base_list 

config = read_yaml_file(args.config_path)
print(config)
base_config = config['_BASE_']

if(len(base_config)==1):
    root_config_name = base_config[0]
    config_path[-1] = root_config_name
    root_config_path = "/".join(config_path)
    print("Root: ", root_config_path)
    root_config = read_yaml_file(root_config_path)
    root_config_base = root_config['_BASE_']
    root_config_base = change_dataset_dir(root_config_base)
    root_config['_BASE_'] = root_config_base
    write_yaml_file(root_config_path, root_config)
else:
    base_config = change_dataset_dir(base_config)
    config['_BASE_'] = base_config
    print("New config file saved: ", args.config_path)
    write_yaml_file(args.config_path, config)

    
