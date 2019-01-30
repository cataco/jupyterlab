c.ServerProxy.servers = {
    'lab-dev': {
        'command': [
            'jupyter',
            'lab',
            '--debug',
            '--no-browser',
            '--port={port}',
            '--NotebookApp.token=""',
            '--NotebookApp.base_url={base_url}lab-dev',
            # Disable dns rebinding protection here, since our 'Host' header
            # is not going to be localhost when coming from hub.mybinder.org
            '--NotebookApp.allow_remote_access=True'
        ],
        'absolute_url': True
    }
}

c.NotebookApp.default_url = '/lab-dev'

import logging
c.NotebookApp.log_level = logging.DEBUG
