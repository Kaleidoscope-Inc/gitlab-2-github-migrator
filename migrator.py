from github import Github, UnknownObjectException


import click
import gitlab


@click.command()
@click.option('--gitlab-token', required=True, help='GitLab access token.')
@click.option('--gitlab-groupid', required=True, help='GitLab group id.')
@click.option('--github-username', required=True, help='GitHub username.')
@click.option('--github-pat', required=True, help='GitHub private access token.')
@click.option('--github-org', required=True, help='GitHub organization.')
def migrator(gitlab_token, gitlab_groupid, github_username, github_pat, github_org):
    """Script that sets up mirroring from GitLab to GitHub."""
    gl = gitlab.Gitlab(private_token=gitlab_token)
    gh = Github(github_pat)
    group = gl.groups.get(gitlab_groupid)
    for gl_project in group.projects.list(iterator=True):
        try:
            gh.get_repo(gl_project.name)
            print(f'{gl_project.name} already exists on GitHub. Skipping mirroring.')
        except (UnknownObjectException):
            print(
                f'{gl_project.name} does not exist on GitHub. Creating and mirroring.')
            gh.get_organization(github_org).create_repo(
                gl_project.name, private=True)
            project_obj = gl.projects.get(gl_project.id)
            project_obj.remote_mirrors.create({'url': f'https://{github_username}:{github_pat}@github.com/{github_org}/{gl_project.name}.git',
                                               'enabled': True})


if __name__ == '__main__':
    migrator()
