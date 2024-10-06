from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig,DataValidationConfig)

from textSummarizer.logging import logger
class ConfigurationManager:
    def  __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        
        try:
            
            self.config = read_yaml(Path("config/config.yaml"))
        except FileNotFoundError as e:
            logger.error(f"Configuration file not found: {config_filepath}")
            raise e
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config
    def get_data_validation_config(self):
        config = self.config.data_validation
        
        create_directories([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )
        
        return data_validation_config
    
    