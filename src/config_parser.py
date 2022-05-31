
import yaml # pip install pyyaml
from datetime import datetime


import global_defs as gdf

from cfg_task_list import CfgTaskList
from cfg_task import CfgTask

TASK_LIST_KEY = 'task_list'
ID_KEY = 'ID'

# simply reads the yaml and produces a dictionary
def parse_config_yaml(config_file_path):

    with open(config_file_path, 'r') as file:
        yaml_loaded = yaml.safe_load(file)

    return yaml_loaded



def parse_config(config_file_path):

    cfg_dict = parse_config_yaml(config_file_path)

    task_list_de = cfg_dict[TASK_LIST_KEY]
    if task_list_de is None:
        exit(1)

    task_list = parse_task_list(task_list_de)
    return task_list


def parse_task_list(task_list_de):
    
    task_list_cfg = CfgTaskList("dummy, ID rimosso")
    
    for task_de in task_list_de:
        task_cfg = parse_task_de(task_de)
        task_list_cfg.add_task(task_cfg)

    return task_list_cfg


def parse_task_de(task_de):

    task_cfg = CfgTask("dummy ID "+str(datetime.now()))

    return task_cfg

