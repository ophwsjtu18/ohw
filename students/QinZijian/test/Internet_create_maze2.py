from gifmaze.algorithms import prim
import gifmaze as gm
surface = gm.GIFSurface(width=600, height=400, bg_color=0)
surface.set_palette([0, 0, 0, 255, 255, 255, 255, 0, 255, 0, 0, 0])
anim = gm.Animation(surface)
#anim.set_control(speeds=20, delay=5, trans_index=3)
maze = anim.create_maze_in_region(cell_size=5, region=8, mask=None)
anim.pad_delay_frame(200)
prim(maze, start=(0, 0))
anim.pad_delay_frame(500)
surface.save('prim.gif')
surface.close()
