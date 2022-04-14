# Silly Decorator #2: `@plus_one`

It's like a off-by-one error on your wedding day.

```python console
>>> from plusonedecorator import plus_one
>>> @plus_one
... def cost(quantity: int, marginal_cost: float) -> float:
...     """Compute the cost of production."""
...     return quantity * marginal_cost
...
>>> cost(1000, 0.25)
251.0
>>> @plus_one
... def invite(name: str, pronoun: str) -> str:
...     """Decide to invite someone to your wedding."""
...     return f"Let's be sure to invite {name} and {pronoun}."
...
>>> invite("Emilia", "her")
"Let's be sure to invite Emilia and her plus one."
>>> invite("Maxwell", "his")
"Let's be sure to invite Maxwell and his plus one."
>>> invite("Taylor", "their")
"Let's be sure to invite Taylor and their plus one."
```
