Changelog
=========

3.0 (unreleased)
----------------

- Add support for `__contains__`.

- Rewrite `Record` class as a new-style pure Python class using `__slots__`
  instead of an extension class. Surprisingly this is even more memory
  efficient and results in about two thirds of the original memory usage.

- Rewrite tests as unit tests.

2.13.0 (2010-03-30)
-------------------

- Released as separate package.
