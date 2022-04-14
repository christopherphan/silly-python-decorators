# Silly Decorator #1: `@a_hole`

> I’m like a pâtissier, except I decorate functions instead of cakes, and I decorate with U+1F4A9 instead of frosting.

```python console
>>> from aholedecorator import a_hole
>>> @a_hole
... def hello(name: str = "friend") -> str:
...     """Print a greeting."""
...     return f"Hello {name}, I hope you are well."
>>> hello()
'Hello friend, I hope you are well.'
>>> hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/chris/Documents/projects/public_repos/silly-python-decorators/a_hole/aholedecorator.py", line 71, in new_func
    raise AHoleError(choice(_MESSAGES))
aholedecorator.AHoleError: I'm like a pâtissier, except I decorate functions instead of cakes, and I decorate with U+1F4A9 instead of frosting.
```
