import random


class Machine:
    def __init__(self):
        self.commands = {}

    def command(self, cmd, num):
        if cmd not in self.commands:
            self.commands[cmd] = [random.choice(["1", "2", "3", "4"])]
        return self.commands[cmd][-1]

    def response(self, res):
        if res is False:
            # If the action was bad, remove it from the list of possible actions
            for cmd, actions in self.commands.items():
                if len(actions) > 1:
                    actions.pop()

a = [1, 100, 101]
solution = Machine()
print(solution.command(a))