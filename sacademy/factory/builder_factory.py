
class FactoryBuilder:
    def __init__(self, options: dict):
        self.module = options['training-module']
        self.players = options['factory']['applications']['players']
        self.coach = options['factory']['applications']['coaches']
        self.window = options['factory']['window']
        self.simulator = options['factory']['simulator']
