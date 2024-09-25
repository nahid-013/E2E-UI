from logging import getLogger, basicConfig, DEBUG, INFO,FileHandler
logger = getLogger()

FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'

basicConfig(level=INFO , format=FORMAT)