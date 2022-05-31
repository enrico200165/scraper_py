

import global_defs as gdf


log = gdf.log


class CfgTask():
    
    def __init__(self, id):
        self._id = id

    def __str__(self):
        return self._id