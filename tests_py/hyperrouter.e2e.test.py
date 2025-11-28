from types import ModuleType


def test_hyperrouter():
    """The package must successfully import.

    Mostly useful as a "hello world" e2e test that ensures the CI/CD
    setup runs without issue.
    """
    import hyperrouter  # noqa: PLC0415, RUF100
    assert isinstance(hyperrouter, ModuleType)
