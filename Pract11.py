from tkinter import *
import random
W=800
H=600
SEG=20
IN_GAME=True
root=Tk()

class Segment(object):
    def __init__(self,x,y):
        self.instance=c.create_rectangle(x,y,x+SEG,y+SEG,fill='lightgreen')

class Snake(object):
    def __init__(self,segments):
        self.segments=segments
        self.mapping={'Down':(0,1),'Up':(0,-1),'Left':(-1,0),'Right':(1,0)}
        self.vector=self.mapping['Right']
    def move(self):
        for i in range(len(self.segments)-1):
            segment=self.segments[i].instance
            x1,y1,x2,y2=c.coords(self.segments[i+1].instance)
            c.coords(segment,x1,y1,x2,y2)
        x1,y1,x2,y2=c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,x1+self.vector[0]*SEG,y1+self.vector[1]*SEG,x2+self.vector[0]*SEG,y2+self.vector[1]*SEG)
    def change_direction(self,event):
        if event.keysym in self.mapping:
            self.vector=self.mapping[event.keysym]
    def add_segment(self):
        last_seg=c.coords(self.segments[0].instance)
        x=last_seg[2]-SEG
        y=last_seg[3]-SEG
        self.segments.insert(0,Segment(x,y))
    def reset_snake(self):
        for segment in self.segments:
            c.delete(segment.instance)



def create_block():
    global BLOCK
    posx=SEG*(random.randint(1,(W-SEG)/SEG))
    posy=SEG*(random.randint(1,(H-SEG)/SEG))
    BLOCK=c.create_oval(posx,posy,posx+SEG,posy+SEG,fill='red')

def main():
    global IN_GAME
    if IN_GAME:
        s.move()
        head_coords=c.coords(s.segments[-1].instance)
        x1,y1,x2,y2=head_coords
        if x2>W or x1<0 or y1<0 or y2>H:
            IN_GAME=False
        elif head_coords==c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()
        else:
            for i in range(len(s.segments)-1):
                if head_coords==c.coords(s.segments[i].instance):
                    IN_GAME=False
        root.after(100,main)
    else:
        set_state(restart_text,'normal')
        set_state(game_over_text,'normal')

def clicked(event):
    global IN_GAME
    s.reset_snake()
    IN_GAME=True
    c.delete(BLOCK)
    c.itemconfigure(restart_text,state='hidden')
    c.itemconfigure(game_over_text,state='hidden')
    start_game()
def set_state(item,state):
    c.itemconfigure(item,state=state)
def start_game():
    global s
    create_block()
    s=create_snake()
    c.bind('<KeyPress>',s.change_direction)
    main()
def create_snake():
    segments=[Segment(SEG,SEG),Segment(SEG*2,SEG),Segment(SEG*3,SEG)]
    return Snake(segments)



root.title('Змейка')
c=Canvas(width=W,height=H,bg='lightblue')
c.pack()
c.focus_set()
game_over_text=c.create_text(W/2,H/2,text='GAME OVER...',font='Arial 20',fill='red',state='hidden')
restart_text=c.create_text(W/2,H-H/3,text='Click to restart',font='Arial 30',fill='white',state='hidden')
c.tag_bind(restart_text,'<Button-1>',clicked)
start_game()

root.mainloop()



























        
            
            
