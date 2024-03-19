from cnnClassifier import logger
from cnnClassifier.pipeline.stage01 import DataIngestionTrainingPipeline


Stage_Name ="Data Ingestion Stage"
try:
        logger.info(f'>>>>>> Stage {Stage_Name} Started <<<<<<<')
        obj =DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>> Stage {Stage_Name} Completed <<<<<<<\n \n x=======x')
except Exception as e:
        logger.exception(e)
        raise e
