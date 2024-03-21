import os
import shutil as sht

import src.main.PATH as path


TMP_FOLD = path.TMP_FOLD


def clean_dir(dir_to_clean=TMP_FOLD):
    if os.path.isdir(dir_to_clean):
        sht.rmtree(dir_to_clean)
