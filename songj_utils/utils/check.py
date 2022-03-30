import os.path as osp
from typing import Any, List, Optional


def check_file_exist(filename: str, msg_tmpl: str = 'file "{}" does not exist') -> Any:
    if not osp.isfile(filename):
        raise FileNotFoundError(msg_tmpl.format(filename))
