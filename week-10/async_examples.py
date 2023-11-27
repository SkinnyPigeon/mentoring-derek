import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return what


async def take_result(what):
    print(f"Result: {what}")

async def main():
    print(f"started at {time.strftime('%X')}")
    
    await asyncio.gather(
        take_result(await say_after(1, "hello")),
        take_result(await say_after(2, "world")),
    )


    print(f"finished at {time.strftime('%X')}")


async def return_after(delay, what):
    await asyncio.sleep(delay)
    return what


if __name__ == "__main__":
    asyncio.run(main())
