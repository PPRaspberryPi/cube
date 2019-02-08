import asyncio

import evdev

pad1 = evdev.InputDevice('/dev/input/event17')
pad2 = evdev.InputDevice('/dev/input/event18')


async def print_events(device):
    async for event in device.async_read_loop():
        print(device.path, evdev.categorize(event), sep=' >>> ')


for device in pad1, pad2:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()
