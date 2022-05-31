import logging
from  logging import handlers
from datetime import datetime, timedelta
import os
from os.path import join

from datetime import datetime


# --- Logging ---
logging.basicConfig(
    format='%(asctime)s %(filename)s %(lineno)s %(levelname)-8s \n%(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

frmter = logging.Formatter('{lineno}**{message}** at{asctime}|{name}',style='{')
logfh = handlers.RotatingFileHandler("logging.log", mode='a', maxBytes=1024*4, backupCount=0, 
    encoding=None, delay=False, errors=None)
logfh.setFormatter(frmter)

log = logging.getLogger(__name__)
log.addHandler(logfh)

#####################################################################
#                           DIRECTORIES
#####################################################################
# --- root directories ----
GDRIVE_ROOT = os.environ['GDRIVE_ENRICO200165_HOME']
if not os.path.isdir(GDRIVE_ROOT):
    log.error("Not found GDrive home directory: {}". format(GDRIVE_ROOT))
    exit(1)

USERPROFILE_DIR = os.environ['USERPROFILE']
DIR_DOWNLOADS = "d:\\classroom"
# DIR_DOWNLOADS = os.environ['TEMP']
# DIR_DOWNLOADS = join(USERPROFILE_DIR, "gclass_loc_download")
COURSEWORK_LOC_DWLD_ROOT_DIR = join(DIR_DOWNLOADS, "gclassroom")



oauth_token_filedir = join(GDRIVE_ROOT, "08_dev_gdrive", "configs", "google_classroom")
if not os.path.isdir(oauth_token_filedir):
    log.warn("remove if not used")

glcassroom_oauth_token_filepath = join(oauth_token_filedir, "token_gclassroom.json")
credentials_file_dir = oauth_token_filedir
if not os.path.isdir(credentials_file_dir):
    log.warn("remove if not used")

enrico200165_credentials   = ""

config_file_dir = r".\configs"
config_file_name = "scraper_pz_config.yaml"
config_file_path = os.path.join(config_file_dir, config_file_name)
