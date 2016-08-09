import ugfx
import buttons
import pyb
 
ugfx.init()
buttons.init()
ugfx.clear(ugfx.YELLOW)
 
ugfx.text(5, 5, "Hello World", ugfx.RED)
ugfx.fill_circle(100, 100, 30, ugfx.GREEN)
ugfx.fill_circle(200, 100, 30, ugfx.GREEN)
ugfx.area(80, 150, 140, 20, ugfx.GREEN)
ugfx.area(120, 170, 60, 20, ugfx.GREEN)
