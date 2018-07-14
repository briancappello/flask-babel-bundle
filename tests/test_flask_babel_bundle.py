from flask import Blueprint
from flask_babel_bundle import FlaskBabelBundle


class TestFlaskBabelBundle:
    def test_add_url_prefix_to_rule(self):
        FlaskBabelBundle.language_code_key = 'lang_code'
        assert FlaskBabelBundle.get_url_rule(None) == '/<lang_code>'
        assert FlaskBabelBundle.get_url_rule('') == '/<lang_code>'
        assert FlaskBabelBundle.get_url_rule('/') == '/<lang_code>/'
        assert FlaskBabelBundle.get_url_rule('/foo') == '/<lang_code>/foo'
        assert FlaskBabelBundle.get_url_rule('/foo/bar') == '/<lang_code>/foo/bar'

    def test_register_blueprint_with_url_lang_code_prefix(self, app):
        bp = Blueprint('bp', 'tests', url_prefix='/bp')
        bp.add_url_rule('/foo', endpoint='foo')

        FlaskBabelBundle.enable_url_lang_code_prefix = True
        FlaskBabelBundle.register_blueprint(app, bp)
        rule = list(app.url_map.iter_rules('bp.foo'))[0]
        assert rule.rule == '/<lang_code>/bp/foo'
        assert bp in list(app.iter_blueprints())

    def test_register_blueprint_without_url_lang_code_prefix(self, app):
        bp = Blueprint('bp', 'tests')
        bp.add_url_rule('/foo', endpoint='foo')

        FlaskBabelBundle.enable_url_lang_code_prefix = False
        FlaskBabelBundle.register_blueprint(app, bp)
        assert bp not in list(app.iter_blueprints())
        assert not list(app.url_map.iter_rules())

    def test_add_url_rule_with_url_lang_code_prefix(self, app):
        FlaskBabelBundle.enable_url_lang_code_prefix = True
        FlaskBabelBundle.add_url_rule(app, '/foo', view_func=lambda: None)

        rule = list(app.url_map.iter_rules())[0]
        assert rule.rule == '/<lang_code>/foo'

    def test_add_url_rule_without_lang_code_prefix(self, app):
        FlaskBabelBundle.enable_url_lang_code_prefix = False
        FlaskBabelBundle.add_url_rule(app, '/foo', view_func=lambda: None)
        assert not list(app.url_map.iter_rules())
