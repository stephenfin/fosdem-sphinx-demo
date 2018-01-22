from docutils import nodes

BASE_URL = 'https://github.com/sphinx-doc/sphinx/issues/{}'


def github_issue(name, rawtext, text, lineno, inliner, options={},
                 content=[]):
    refuri = BASE_URL.format(text)
    node = nodes.reference(rawtext, text, refuri=refuri, **options)
    return [node], []


def setup(app):
    app.add_role('ghissue', github_issue)
    return {'version': '1.0', 'parallel_read_safe': True}
