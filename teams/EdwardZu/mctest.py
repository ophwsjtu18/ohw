import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
while True:
    events = mc.events.pollBlockHits()
    for e in events:
        print(e.pos.x,e.pos.y,e.pos.z)
