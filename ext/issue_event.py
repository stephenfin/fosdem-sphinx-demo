from __future__ import print_function
from __future__ import unicode_literals

import io
import os.path
import requests

URL = 'https://api.github.com/repos/sphinx-doc/sphinx/issues'


def get_issues():
    issues = requests.get(URL).json()

    for issue in issues:
        title = '%s (#%s)' % (issue['title'], issue['number'])
        owner = 'Opened by %s' % issue['user']['login']
        yield issue['number'], title, issue['body'], owner


def generate_issue_docs(app):
    for num, title, body, owner in get_issues():
        filename = os.path.join(app.srcdir, 'issues', '%s.rst' % num)

        with io.open(filename, 'w') as issue_doc:
            print(title, file=issue_doc)
            print('=' * len(title), file=issue_doc)
            print('', file=issue_doc)
            print('%s ::' % owner, file=issue_doc)
            print('', file=issue_doc)

            for line in body.splitlines():
                if line:
                    print('    %s' % line if line else '', file=issue_doc)
                else:
                    print('', file=issue_doc)


def setup(app):
    app.connect('builder-inited', generate_issue_docs)
    return {'version': '1.0', 'parallel_read_safe': True}
