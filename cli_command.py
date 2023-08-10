#!/usr/bin/env python
import plugins
import os
import json

class Plugin(plugins.BasePlugin):
    __name__ = 'cli_command'

    def run(self, config):

        command = config.get(__name__, 'command')

        if not command:
            return "The mandatory config parameter 'command' is not set or empty."

        stream = os.popen(command)
        output = stream.read()

        try:
            results = json.loads(output)
        except Exception:
            return "The command did not return a valid json string."
        return results

if __name__ == '__main__':
    Plugin().execute()
