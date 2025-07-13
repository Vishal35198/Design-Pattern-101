import logging
import json
from threading import Lock
from copy import deepcopy

# Logger for Basic Logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'  # Append mode
)

# Singleton Instances 

class ConfigManager:
    _instance = None
    _lock = Lock()
    
    def __new__(cls, config_path=None):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._config = {}
                if config_path:
                    cls._instance.load_config(config_path)
        return cls._instance
    
    def load_config(self, path: str):
        try:
            with open(path, 'r') as f:
                self._config = json.load(f)
            logging.info(f"Config loaded from {path}")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.exception(f"Config load failed: {str(e)}")
            raise
    # use property for getter/setter type method and deepcopy for no modification
    @property
    def config(self):
        return deepcopy(self._config)  # Prevent external modifications
        
    def read_configs(self):
        for k, v in self._config.items():
            print(f"{k} : {v}")

    def get(self, key, default=None):
        return self._config.get(key, default)
    

