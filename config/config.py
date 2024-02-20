import yaml

class AppConfig:
    def __init__(self, config_file):
        with open(config_file, 'r') as stream:
            self.config = yaml.safe_load(stream)

    def get(self, key):
        return self.config[key]

    def get_all(self):
        return self.config

configPath = 'config/local.yaml'

appConfig = AppConfig(configPath)