from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('renamecfd.py', base=base)
]

setup(name='RenameCFD',
      version = 'v1.0.0-beta',
      description = 'Renombra los archivos xml de los cfdi contenidos en la carpeta actual, colocando en el nombre parte de la informaci\xc3\xb3n contenida en el xml.',
      options = dict(build_exe = buildOptions),
      executables = executables)
