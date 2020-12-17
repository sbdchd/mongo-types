from setuptools import setup  # type: ignore

# This allows for the pip install -e . to work so that mypy can check the types
# of the examples. Since the stubs aren't using valid python package names,
# mypy can't check the types normally.

setup(name="mongo-types")
