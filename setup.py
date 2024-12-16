from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize("app/tasks/task.pyx", compiler_directives={'language_level': "3"}),
    script_args=["build_ext", f"--build-lib=/app"]
)