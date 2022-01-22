import time
import asyncio


async def cook_pasta():
    print("Filled port with water. Pasta will now cook.")
    await asyncio.sleep(10)
    print("Paste ready.")


async def heat_meatloaf():
    print("Took meatloaf out of the fridge. Into the microwave it goes")
    await asyncio.sleep(3)
    print("Meatloaf heated.")


async def peel_avocado():
    print("Grabbed avocado. Now peeling and slicing")
    await asyncio.sleep(2)
    print("Avocado sliced.")


async def lunch():
    print("Preparing lunch.")
    start = time.time()
    await asyncio.gather(
        cook_pasta(),
        heat_meatloaf(),
        peel_avocado(),
    )
    end = time.time()
    print(f"Eating after {round(end - start)} min of prep time")


asyncio.run(lunch())
