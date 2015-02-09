from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('Application.py', base=base, targetName = 'citizentales')
]

setup(name="Citizen's Tales",
      version = 'SpicyKoala (0.2a)',
      description = 'Rogue-Like en python',
      options = dict(build_exe = buildOptions),
      executables = executables)
