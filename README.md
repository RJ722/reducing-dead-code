## Reducing dead code ratio of Python Projects

Maintaining a high level of code quality is important for any serious project. One aspect of this is ensuring that all code is actually used. There are many reasons for dead code ending up in a project.The most common is refactoring, but another is misspellings, which are only detected at runtime for dynamic languages. Finding and removing dead code allows to keep the code base clean and reduces bugs.

This talk is focussed on how we can use Vulture to find dead code. It helps you find unused code in Python programs and it is useful for cleaning up and finding errors in large code bases. If you run Vulture on both your library and test suite you can find untested code. Due to Python's dynamic nature, static code analyzers like Vulture are likely to miss some dead code. Also, code that is only called implicitly may be reported as unused. Nonetheless, Vulture can be a very helpful tool for higher code quality.

One part of this talk is to discuss how to automate testing for dead code with Vulture. There are quite a few options available:

- Adding vulture to your continuous integration testing.
- A script using the Vulture API for custom tests.
- [VultureBear](https://github.com/coala/coala-bears/blob/master/bears/python/VultureBear.py): Integration with [coala](https://coala.io) - a static code analysis tool.


## Download

You may find the most recent version of the presentation here: https://github.com/RJ722/reducing-dead-code/releases

Author: RJ722

PyCon India, 2017
