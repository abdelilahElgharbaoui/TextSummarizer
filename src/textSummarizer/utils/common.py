# create frequent modules that can be reused

import os 
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# ensure that we passed the same type we demand
@ensure_annotations
# configBox d['key'] => d.key
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
    path_to_yaml (str): path like input 
    
    Raises:
    ValueError: if yaml file is empty
    e:empty file
    
    Retuens:
    ConfigBox: ConfigBox type
    
    """
    
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """Create list of directories
    
    Args:
        path_to directories (list) : list of path of directories
        ignor_log(bool,optional): ignore if multiple dirs is to be created. Defaults to Flase
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")
     
            
@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB 
    Args:
        path (Path): path of file
    Returns:
         str: size inKB
    """
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb}KB"