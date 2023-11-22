import asyncio
import time

async def function1():
    await asyncio.sleep(1)
    print("function1")
    return("priya")

async def function2():
    await asyncio.sleep(1)
    print("function2")
    return("patel")

async def function3():
    await asyncio.sleep(4)
    print("function3")

async def function4():
    await asyncio.sleep(2)
    print("function4")
async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
        function4()
    )
    print(L)

asyncio.run(main())