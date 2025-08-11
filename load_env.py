import os
import environ


_GLOBAL_ENV = None


def loadEnv(env_path: str = "./", env_file: str = ".env"):
    global _GLOBAL_ENV

    if _GLOBAL_ENV is not None:
        return _GLOBAL_ENV
    _GLOBAL_ENV = environ.Env()
    _GLOBAL_ENV.read_env(os.path.join(env_path, env_file))
    return _GLOBAL_ENV
