import sys
if sys.version_info[0] == 2:
    import Tkinter
    from Tkinter import *
else:
    import tkinter as Tkinter
    from tkinter import *
import random
L1 = random.sample( range( 1, 100 ), 90 )
data = L1
going = True
is_run = False
number = list()
def lottery_roll( var1, var2, var3 ):
    global going, number
    show_member = random.choice( data )
    var1.set( show_member )
    if going:
        window.after( 50, lottery_roll, var1, var2, var3 )
    else:
        var2.set( '恭喜 {} ！！！'.format( show_member ) )
        if not ( len( number ) +1 ) %20:
            number.append( str(show_member)+'\n' )
        else:
            number.append( str(show_member) )
        var3.set( '幸運數字: {}'.format( ' , '.join(number) ) )
        data.remove( show_member )
        going = True
        return

def lottery_start( var1, var2, var3 ):
    global is_run
    if is_run:
        return
    is_run = True
    var2.set( '幸運兒是你嗎。。。' )
    lottery_roll( var1, var2, var3 )

def lottery_end():
    global going, is_run, number
    if is_run:
        going = False
        is_run = False
    

if __name__ == '__main__':
    window = Tkinter.Tk()
    window.geometry('1438x752')
    window.title('賓 果 抽 獎 器')
    bg_label = Label(window,width=70,height=24,bg='#ECf5FF')
    bg_label.place(anchor=NW,x=0,y=0)
    background_img= PhotoImage(file='D:/bingo/img.png')
    background= Label(window, image=background_img, bd=0)
    background.pack()

    var1 = StringVar(value='即將開始')
    show_label1 = Label(window,textvariable=var1,justify='left',anchor=CENTER,width=8,height=2,bg='#FFFFFF',font='楷體 -40 bold',foreground='black')
    show_label1.place(anchor=NW,x=575,y=250)

    var2 = StringVar(value='幸運兒是你嗎。。。')
    show_label2 = Label(window,textvariable=var2,width=15,bg='#E33B3E',font='微軟正黑體 -38 bold',foreground='white')
    show_label2.place(anchor=NW,x=500,y=480 )

    var3 = StringVar(value = '' )
    show_label3 = Label( window, textvariable = var3,justify='center', width = 89, bg = '#FFFFFF', font = '微軟正黑體 -18 bold', foreground = 'black' )
    show_label3.place(anchor=CENTER,x=785,y=650)

    button1 = Button( window, text = '開始', command = lambda: lottery_start(var1, var2, var3), width = 10, bg= '#FFE4B5', font = '微軟正黑體 -18 bold' )
    button1.place( anchor = CENTER, x = 430, y = 425 )
    button2 = Button( window, text = '結束', command = lambda: lottery_end(), width = 10, bg= '#FFE4B5', font= '微軟正黑體 -18 bold' )
    button2.place( anchor = CENTER, x = 900, y = 425 )
    window.mainloop()
