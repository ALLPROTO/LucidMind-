import yaml
import os
from typing import Dict, Any
from .defaults import DEFAULT_CONFIG

def load_config(config_path: str = None) -> Dict[str, Any]:
    """
    Loads configuration from a YAML file and merges it with defaults.
    
    Args:
        config_path: Path to the YAML configuration file
        
    Returns:
        Merged configuration dictionary
    """
    config = DEFAULT_CONFIG.copy()
    
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r') as f:
            user_config = yaml.safe_load(f)
            if user_config:
                config.update(user_config)
                
    return config
