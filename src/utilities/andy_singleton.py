from src.utilities import andy_logger,andy_exceptions

logger = andy_logger.get_logger("andy_singleton")


class Singletons:
    __instance = None
    some_param = None

    @staticmethod
    def get_instance():
        """Static access method"""
        if Singletons.__instance is None:
            logger.info("Calling private constructor for embedder initialization ")
            Singletons()
        return Singletons.__instance

    def __init__(self):
        if Singletons.__instance is not None:
            raise andy_exceptions.SingletonReinitalizationException
        else:
            self.some_param = "Set some Singleton parameters here "
            Singletons.__instance = self

    def get_some_param(self):
        return self.some_param
