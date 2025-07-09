import os
import sys

import yaml
from pathlib import Path
from string import Template
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from hate_classifier.exception import CustomException
from hate_classifier.logger import LoggerManager


logger = LoggerManager("Utils - main_utils").get_logger()

@ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
  """
  Method Name :   read_yaml
  Description :   This method reads a yaml from local into memory

  Output      :   Returns a dict with the yaml contents
  On Failure  :   Write an exception log and then raise an exception

  Version     :   1.0
  Revisions   :   
  """
  try:
    with open(filepath, "rb") as yaml_file:
      read_yaml = yaml.safe_load(yaml_file)
    
    logger.info(f"Read yaml file : {filepath}")
    return ConfigBox(read_yaml)
  except BoxValueError:
        raise ValueError("yaml file is empty")
  except Exception as e:
    logger.info(f"Could not read yaml file : {filepath}")
    raise CustomException(e, sys) from e
  
  
global_substitutions = {} 
@ensure_annotations
def substitute_var_yaml(template_filepath: Path, output_filepath: Path, variable_substitution: dict):
  """
  Method Name :   substitute_var_yaml
  Description :   This method substitutes a new variable {variable_substitution} into a YAML template {template_filepath} by accumulating all previous ones,
    and writes the final result to `output_path`

  Output      :   Returns a yaml file {output_path} with the substituted contents
  On Failure  :   Write an exception log and then raise an exception

  Version     :   1.0
  Revisions   :   
  """
  try:
    global_substitutions.update(variable_substitution)
    
    with open(template_filepath, "r") as yaml_file:
      template = Template(yaml_file.read())
      rendered_yaml = template.substitute(global_substitutions)
      
    with open(output_filepath, "w") as yaml_file:
      yaml_file.write(rendered_yaml)
  
    logger.info(f"Read yaml file {output_filepath} and inputed value for {variable_substitution.keys()[0]}")
  except Exception as e:
    logger.info(f"Could not read yaml file {output_filepath} and inputed value for {variable_substitution.keys()[0]}")
    raise CustomException(e, sys) from e
  
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")