# Coded by @CyberBoyAyush
# For HellBot : https://github.com/HellBoy-OP/HellBot


import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("inflag"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    await event.edit("Hello")
    animation_chars = [
        "Indian Flag",
        "**π§π§π§π§π§π§π§π§π§π§π§π§π§\nπ§π§π§π§π§π§π§π§π§π§π§π§π§\nπ§π§π§π§π§π§π§π§π§π§π§π§π§\nβ¬οΈβ¬οΈβ¬οΈβ¬οΈβ¬οΈπ¦π¦π¦β¬οΈβ¬οΈβ¬οΈβ¬οΈβ¬οΈ\nβ¬οΈβ¬οΈβ¬οΈβ¬οΈβ¬οΈπ¦π¦π¦β¬οΈβ¬οΈβ¬οΈβ¬οΈβ¬οΈ\nβ¬οΈβ¬οΈβ¬οΈβ¬οΈβ¬οΈπ¦π¦π¦β¬οΈβ¬οΈβ¬οΈβ¬οΈβ¬οΈ\nπ©π©π©π©π©π©π©π©π©π©π©π©π©\nπ©π©π©π©π©π©π©π©π©π©π©π©π©\nπ©π©π©π©π©π©π©π©π©π©π©π©π©\n\n                π§‘π€π\n\nProud To Be An Indianβ£οΈ!!**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
