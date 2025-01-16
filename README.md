# Basics of using `pytest`

A project to show how the basics for pytest (and setup.py) work!

### Notes

- Project has a primary python package called `gitallica`.

**marks:**
- Pay attention to `test_core.py` marks.
- Running both marks together: `pytest -m "basics or advanced`
- Running one but not other: `pytest -m "basics and not advanced`

**`pytest.ini`:**
- You must set the `pythonpath` config to find the gitallica package.
- `verbosity_test_cases` is same as having `pytest -v` option

**pip:**
- To pip install gitallica: `pip install -e .`

**TODO::**
- Look into `twine` to upload this package to pypi
