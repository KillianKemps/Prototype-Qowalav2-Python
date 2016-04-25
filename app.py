import os, glob, imp

import core_api

modules = []

# Search all modules in plugins/
for path in glob.glob('plugins/[!_]*/main.py'):
    name, ext = os.path.splitext(os.path.basename(path))
    dirname = os.path.basename(os.path.dirname(path))
    modules.append(imp.load_source(dirname, path))

# Start all plugins found
for module in modules:
    module.test()
    module.initialize(core_api.QowalaAPI)
