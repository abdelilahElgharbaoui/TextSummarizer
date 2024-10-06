from textSummarizer.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipline.satge_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"{STAGE_NAME} started.")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"{STAGE_NAME} started.")
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e