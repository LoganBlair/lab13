#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class

enemy1 = drawpad.create_rectangle(50,50,125,95,fill = "Blue")
enemy2 = drawpad.create_rectangle(300,400,375,445,fill = "green")
enemy3 = drawpad.create_rectangle(400,275,475,325,fill = "purple")


direction = 5

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="Up", background= "red")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    
       	    self.button2 = Button(self.myContainer1)
	    self.button2.configure(text="Right", background= "red")
	    self.button2.grid(row=1,column=2)
	    self.button2.bind("<Button-1>",self.button2clicked)
	    
	    self.button3 = Button(self.myContainer1)
	    self.button3.configure(text="Down", background= "red")
	    self.button3.grid(row=2,column=1)
	    self.button3.bind("<Button-1>",self.button3clicked)
	    
	    self.button4 = Button(self.myContainer1)
	    self.button4.configure(text="Left", background= "red")
	    self.button4.grid(row=1,column=0)
       	    self.button4.bind("<Button-1>",self.button4clicked)
    
           	  
           	    # No need to edit this - just includes the drawpad into our frame
            drawpad.pack(side=RIGHT)
           	    # call the animate function to start our recursion
            self.animate()
            self.animate2()
            self.animate3()
	
	def animate(self):
	    global drawpad
	    global direction
	    global enemy1
	    x1, y1, x2, y2 = drawpad.coords(enemy1)
	    if x2 > drawpad.winfo_width():
	        drawpad.move(enemy1,-800,0)
	    else:
	        direction = 5
	    drawpad.move(enemy1,5,0)
	    drawpad.after(10,self.animate)
	 
	def animate2(self):
	    global drawpad
	    global direction
	    global enemy2  	    
	    x1, y1, x2, y2 = drawpad.coords(enemy2)
	    if x2 > drawpad.winfo_width():
	        drawpad.move(enemy2,-800,0)
	    else:
	        drawpad.move(enemy3,0,0)
	    drawpad.move(enemy2,8,0)    
	    drawpad.after(10,self.animate2) 

	def animate3(self):
	    global drawpad
	    global direction
	    global enemy3
	    x1, y1, x2, y2 = drawpad.coords(enemy3)	    
	    if x2 > drawpad.winfo_width():
	        drawpad.move(enemy3,-800,0)
	    else:
	        drawpad.move(enemy3,0,0)
	    drawpad.move(enemy3,10,0)   
	    drawpad.after(10,self.animate3)  
	    
	    
	    
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def button2clicked(self, event):
	   global oval
	   global player
	   drawpad.move(player,10,0)
	   
	def button3clicked(self, event):
	    global oval
	    global player
	    drawpad.move(player,0,10)
	    
	def button4clicked(self, event):
	   global oval
	   global player
	   drawpad.move(player,-10,0)

app = MyApp(root)
root.mainloop()