class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CommandInvoker(metaclass=SingletonMeta):
    def __init__(self):
        self.__history = []
        self.__description_history = []

    def execute_command(self, command):
        command.execute()
        self.__history.append(command)
        self.__description_history.append(command.description())

    def undo_command(self):
        if self.__history:
            self.__description_history.append("Undid an action.")
            command = self.__history.pop()
            command.undo()
        else:
            print("No commands to undo")

    def print_history(self):
        print("Command History:")
        for command_description in self.__description_history:
            print(command_description)
