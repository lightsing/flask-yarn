from pathlib import Path
from flask import current_app, send_from_directory

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class Yarn(object):

    def __init__(self, app):
        self.app = app
        self.setdefault(app)
        self.root = Path(app.config['YARN_DIR'])
        self.app.add_url_rule(
            '/{prefix}/<name>/<path:file>'.format(prefix=app.config['YARN_PREFIX']),
            view_func=self.serve_static)

    def setdefault(self, app):
        app.config.setdefault('YARN_PREFIX', 'static')
        app.config.setdefault('YARN_DIR', 'node_modules')

    def serve_static(self, name, file):
        f = self.root.joinpath(name, 'dist', file)
        return send_from_directory(f.parent, f.name)