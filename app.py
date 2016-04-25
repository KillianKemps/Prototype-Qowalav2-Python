import os, glob, imp

modules = []

for path in glob.glob('plugins/[!_]*/[!_]*.py'):
    name, ext = os.path.splitext(os.path.basename(path))
    dirname = os.path.basename(os.path.dirname(path))
    modules.append(imp.load_source(dirname, path))

for module in modules:
    module.test()
    module.initialize()
