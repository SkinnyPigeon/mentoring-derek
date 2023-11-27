import pytest
from async_examples import return_after


# Some extra reading: https://tonybaloney.github.io/posts/async-test-patterns-for-pytest-and-unittest.html
@pytest.mark.asyncio
async def test_async_examples():
    assert await return_after(1, "hello") == "hello"
    assert await return_after(2, "world") == "world"
