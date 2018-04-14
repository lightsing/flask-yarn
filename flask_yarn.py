from pathlib import Path
from flask import send_from_directory, abort


class Yarn(object):

    def __init__(self, app):
        self.app = app
        self.setdefault(app)
        self.root = Path(app.config['YARN_DIR'])
        self.static_root = Path(app.config['STATIC_DIR'])
        self.app.add_url_rule(
            '/{prefix}/<name>/<path:file>'.format(prefix=app.config['YARN_PREFIX']),
            view_func=self.serve_static)

    @staticmethod
    def setdefault(app):
        app.config.setdefault('YARN_PREFIX', 'static')
        app.config.setdefault('STATIC_DIR', 'static')
        app.config.setdefault('YARN_DIR', 'node_modules')

    def serve_static(self, name, file):
        for f in [self.root.joinpath(name, 'dist', file),
                  self.root.joinpath(name, file),
                  self.static_root.joinpath(name, file)]:
            if f.exists():
                return send_from_directory(f.parent, f.name)
        return abort(404)

    def url_for(self, name, file):
        return self.root.joinpath(name, 'dist', file)
