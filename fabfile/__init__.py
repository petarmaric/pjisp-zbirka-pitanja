"""\
Pregled korisnih komandi:

* 'fab build'                         kompajlira celokupnu knjigu (u svim podrzanim formatima)
"""

from fabric.api import task

import build
import publish


@task(default=True)
def help():
    from fabric.main import show_commands
    show_commands(__doc__, 'normal')
