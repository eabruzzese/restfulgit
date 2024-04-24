import os
import multiprocessing

import gunicorn.app.base

from restfulgit.app import application


class Application(gunicorn.app.base.BaseApplication):

    def __init__(self, application, options=None):
        self.application = application
        self.options = options or {}
        super().__init__()

    @property
    def config(self):
        return {
            k.lower(): v for k, v in self.options.items()
            if k in self.cfg.settings and v is not None
        }

    def load_config(self):
        for key, value in self.config.items():
            self.cfg.set(key, value)

    def load(self):
        return self.application

RESTFULGIT_ADDR = os.getenv("RESTFULGIT_PORT", "0.0.0.0")
RESTFULGIT_PORT = os.getenv("RESTFULGIT_PORT", "8000")
RESTFULGIT_WORKERS = os.getenv("RESTFULGIT_WORKERS")

if __name__ == '__main__':
    Application(
        application=application,
        options={
            "bind": f"{RESTFULGIT_ADDR}:{RESTFULGIT_PORT}",
            "workers": RESTFULGIT_WORKERS or (multiprocessing.cpu_count() * 2) + 1,
        }
    ).run()
