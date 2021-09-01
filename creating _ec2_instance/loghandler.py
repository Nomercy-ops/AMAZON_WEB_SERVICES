import logging

logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='aws_ec2.log', level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='aws_ecs.log', level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')
