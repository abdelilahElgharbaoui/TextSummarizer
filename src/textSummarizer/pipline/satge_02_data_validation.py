from typing import Any
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __call__(self):
        pass
    
    def main(self):
        # creating piplines
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            validation_status = data_validation.validate_all_files_exist()
            logger.info(f"Data validation status: {validation_status}")
        except Exception as e:
            logger.exception(e)
            raise e
    