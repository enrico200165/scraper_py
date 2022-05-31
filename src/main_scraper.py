from yaml import parse

import global_defs as gdf
import config_parser


log = gdf.log


def main():
    cfg_task_list = config_parser.parse_config(gdf.config_file_path)
    print(cfg_task_list)

main()