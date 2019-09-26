# learn-python
learning python3.7 in vscode

# docstring
```python
def power(x, n):
    """Compute the power of a number.

    Arguments:
    * x: a number
    * n: the exponent

    Returns:
    * c: the number x to the power of n

    """
    return x ** n
```

# pytest
```
%%writefile first.py
def first(l):
    return l[0] if l else None

%%writefile -a first.py

# This is appended to the file.
def test_first():
    assert first([1, 2, 3]) == 1
    assert first([]) is None

!pytest first.py
```