# Basics of using `pytest`

A project to show how the basics for pytest (and setup.py) work!

### How It Works Notes

- Both `tests/` and `gitallica/` are python packages with `__init__.py` files.
- Must have a `pytest.ini` file to set the `pythonpath` config.
- `pythonpath` is set to the root of the project(ie: `.`).
- **Optional:** `setup.py` is used to install the package in editable mode.

**marks:**
- Pay attention to `test_core.py` marks.
- Running both marks together: `pytest -m "basic or advanced"`
- Running one but not other: `pytest -m "basic and not advanced"`
- Running union of levels: `pytest -m "basic and red"`

**`pytest.ini`:**
- You must set the `pythonpath` config to find the gitallica package.
- `verbosity_test_cases` is same as having `pytest -v` option

**pip:**
- To pip install gitallica: `pip install -e .`

**TODO::**
- Look into `twine` to upload this package to pypi


# Useful and Commonly Used pytest Features

## Fixtures
Used to provide a fixed baseline upon which tests can reliably and repeatedly execute.
```python
@pytest.fixture
def sample_fixture():
    return "sample data"

def test_using_fixture(sample_fixture):
    assert sample_fixture == "sample data"
```

## Parametrize
Allows you to run a test with different sets of parameters.
```python
@pytest.mark.parametrize("input,expected", [(1, 2), (3, 4), (5, 6)])
def test_parametrize(input, expected):
    assert input + 1 == expected
```

## Xfail
Marks a test as expected to fail.
```python
@pytest.mark.xfail
def test_expected_to_fail():
    assert False
```

## Skip
Skips a test.
```python
@pytest.mark.skip(reason="not implemented yet")
def test_skip():
    assert False
```

## Skipif
Conditionally skips a test.
```python
@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
def test_skipif():
    assert False
```

## Raises
Asserts that an exception is raised.
```python
def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## Tempdir
Provides a temporary directory unique to the test invocation.
```python
def test_tempdir(tmpdir):
    temp_file = tmpdir.join("temp_file.txt")
    temp_file.write("content")
    assert temp_file.read() == "content"
```

## Monkeypatch
Allows you to modify objects, dictionaries, or environment variables.
```python
def test_monkeypatch(monkeypatch):
    monkeypatch.setattr("os.getcwd", lambda: "/tmp")
    assert os.getcwd() == "/tmp"
```

## Capture
Captures output during tests.
```python
def test_capture(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
```

## Custom markers
Define your own markers for categorizing tests.
```python
@pytest.mark.custom_marker
def test_custom_marker():
    assert True
```
