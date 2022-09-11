# GitLab To GitHub Migrator

Python script that sets up GitLab to GitHub mirroring for a GitLab Group.
Given a GitLab Group id, it iterates through the projects in that group and sets up mirroring.
If the repository does not exist on GitHub, it creates it first otherwise it skips mirroring.

# Requirements

```
pip3 install -r requirements.txt
```

# Usage

```
python3 migrator.py --gitlab-token <gitlab_access_token> --gitlab-groupid <gitlab_group_id> --github-username <github_username> --github-pat <github_private_access_token> --github-org <github_organization>
```