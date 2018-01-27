from docutils import nodes
from docutils.parsers.rst import Directive
import requests

URL = 'https://api.github.com/repos/sphinx-doc/sphinx/issues/{}'


def get_issue(issue_id):
    issue = requests.get(URL.format(issue_id)).json()

    title = '%s (#%s)' % (issue['title'], issue_id)
    owner = 'Opened by %s' % issue['user']['login']

    return title, issue['body'], owner


class ShowGitHubIssue(Directive):

    required_arguments = 1

    def run(self):
        issue_id = self.arguments[0]
        issue = get_issue(issue_id)

        section = nodes.section(ids=['github-issue-%s' % issue_id])
        section += nodes.title(text=issue[0])
        section += nodes.paragraph(text=issue[2])
        section += nodes.literal_block(text=issue[1])

        return [section]


def setup(app):
    app.add_directive('github-issue', ShowGitHubIssue)
    return {'version': '1.0', 'parallel_read_safe': True}
