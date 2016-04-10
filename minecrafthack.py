# While Minecraft: Pi Edition is running, run this file on a Raspberry Pi with this command:
# python minecrafthack.sh

# import the block module, which allows for the creation of blocks and the minecraft module, which allows communication with Minecraft
from mcpi import block
from mcpi import minecraft

# First make a connection between python and the game
mc = minecraft.Minecraft.create()

# mc is a object we can call to control the world.  We should say, "Hello!"
mc.postToChat("Hello, Minecraft World!")

# Now add a block.  You could read the coordinates in the top left, and choose numbers near those.
mc.setBlock(-7, 10,0 , block.STONE)

# Try to spell a word in the sky.  It is very easy with copy and paste.
mc.setBlock(-7, 9, 0, block.STONE)
mc.setBlock(-7, 8, 0, block.STONE)
mc.setBlock(-7, 7, 0, block.STONE)
mc.setBlock(-7, 6, 0, block.STONE)
mc.setBlock(-7, 9, 1, block.STONE)
mc.setBlock(-7, 10, 2, block.STONE)
mc.setBlock(-7, 9, 3, block.STONE)
mc.setBlock(-7, 10, 4 , block.STONE)
mc.setBlock(-7, 9, 4, block.STONE)
mc.setBlock(-7, 8, 4, block.STONE)
mc.setBlock(-7, 7, 4, block.STONE)
mc.setBlock(-7, 6, 4, block.STONE)
# I spelled the letter M.  Try to write your name and impress your friends.
