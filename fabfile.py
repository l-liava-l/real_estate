from fabric.api import run, settings, local, prompt
from fabric.context_managers import lcd

def commit():
    """
    Commit change
    """
    local('git status')
    prompt('Press <Enter> to continue or <Ctrl+C> to cancel.')
    local('git add .')
    local('git commit')


def ch(branch):
    """
    Move your branch to current HEAD and checkout
    """
    local('git branch -f %s' % branch)
    local('git checkout %s' % branch)


def rebase(brunch='master'):
    """
    Rebase current branch on other brunch
    """
    current_branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
    local('git checkout %s' % brunch)
    local('git pull origin %s' % brunch)


def merge(brunch='master', push=True, with_commit=True):
    """ Merge with master
    """
    current_branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
    try:
        if with_commit:
            commit()
        rebase(brunch)
        local('git checkout %s' % brunch)
        local('git merge --no-ff %s' % current_branch)
        if push:
            local('git push origin %s' % brunch)
    finally:
        local('git checkout %s' % current_branch)
        local('git rebase master')


def pull():
    current_branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
    rebase()
    local('git checkout %s' % current_branch)
    local('git rebase master')
