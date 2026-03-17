from util.environment_config import EnvironmentConfig
from datetime import datetime

CONST_DEBUG_ENVIRONMENTS = ["LOCAL", "DEV"]

class Logger:
    config: EnvironmentConfig
    scope: list[str] | None

    def __init__(self, config: EnvironmentConfig, scope = None):
        self.config = config
        self.scope = scope

    def print_log(self, prefix: str, message: str):
        print(f"{prefix}[{datetime.now().strftime("%H:%M:%S")}]{"" if self.scope == None else f"[{"/".join(self.scope)}]"}: {message}")

    def info(self, message: str):
        self.print_log("Info", message)
    
    def warning(self, message: str):
        ANSI_YELLOW = '\033[93m'
        self.print_log(ANSI_YELLOW + "Warning", message)

    def error(self, message: str):
        ANSI_RED = '\033[91m'
        self.print_log(ANSI_RED + "Error", message)

    def debug(self, message: str):
        if(self.config.environment in CONST_DEBUG_ENVIRONMENTS):
            self.print_log("Debug", message)
    
    def get_scope(self, scope: str):
        return Logger(self.config, [scope] if self.scope == None else [*self.scope, scope])