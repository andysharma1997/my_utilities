from abc import ABC, abstractmethod


class AndyExceptions(Exception, ABC):
    @abstractmethod
    def display_code(self):
        pass

    @abstractmethod
    def display_message(self):
        pass


class SomeCustomException(AndyExceptions):
    code = None
    message = None

    def __init__(self, some_input):
        self.code = 20001
        self.message = "The message attached with the some_input = {}".format(some_input)

    def display_code(self):
        return self.code

    def display_message(self):
        return self.message


class SingletonReinitalizationException(AndyExceptions):
    code = None
    message = None

    def __init__(self):
        self.code = 20002
        self.message = "The singleton is already initialized you are attempting to initialize it again."

    def display_code(self):
        return self.code

    def display_message(self):
        return self.message
