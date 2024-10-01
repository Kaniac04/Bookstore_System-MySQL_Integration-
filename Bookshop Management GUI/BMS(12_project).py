import tkinter as tkg
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox as msgbox
import mysql.connector as mysql
import random
import datetime

#--------------------------------------------------------------------------ADMIN USER PAGE---------------------------------------------------------------------------------
#function for admin page
def adminlog():
    
        adminuser=tkg.Toplevel(parent)
        adminuser.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
        adminuser.title('Admin Login')
        username_text=tkg.Label(adminuser,text='Username: ')
        username_text.grid(row=0,column=0,padx=20,pady=10)
        userentry=tkg.Entry(adminuser)
        userentry.grid(row=0,column=1,padx=20,pady=10)
        password_text=tkg.Label(adminuser,text='Password: ')
        password_text.grid(row=1,column=0,padx=20,pady=10)
        passwordentry=tkg.Entry(adminuser,show='*')
        passwordentry.grid(row=1,column=1,padx=20,pady=10)

        submit_button=tkg.Button(adminuser,text='SUBMIT',command=lambda: check(userentry.get(),passwordentry.get(),adminuser))
        submit_button.grid(row=2,column=0,columnspan=2,pady=10)

# function for checking the password
def check(a,b,c):
    if a=='Aayush_code' and b=='ABCD100':
        c.destroy()
        adminscreen()
    else:
        c.destroy()
        adminlog()

#admin screen
def adminscreen():
    admin_scr=tkg.Toplevel(parent)
    admin_scr.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
    admin_scr.title('Admin Screen')
    admin_screen_img=tkg.Label(admin_scr,image=mainscreen_img,height=200,width=500)
    admin_screen_img.grid(row=0,column=0,columnspan=2)
    add_book_button=tkg.Button(admin_scr,text='Add/Update Book Info',width=70,height=5,command=add_book_screen)
    add_book_button.grid(row=1,column=0,columnspan=2)
    order_button=tkg.Button(admin_scr,text='Order',width=35,height=5,command=order_screen)
    order_button.grid(row=2,column=0)
    history_button=tkg.Button(admin_scr,text='Order History',width=35,height=5,command=ord_his)
    history_button.grid(row=2,column=1)
    new_cust_button=tkg.Button(admin_scr,text='New Customer',width=35,height=5,command=new_customer).grid(row=3,column=0)
    cust_details_button=tkg.Button(admin_scr,text='View Customer Info',width=35,height=5,command=customer_log).grid(row=3,column=1)

#add book screen
def add_book_screen():
        addbook_scr=tkg.Toplevel(parent)
        addbook_scr.title('Add book(Admin interface)')
        addbook_scr.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
        add_scr_img=tkg.Label(addbook_scr,image=mainscreen_img,height=100,width=900)
        add_scr_img.grid(row=0,column=0,columnspan=2)
        add_rbutton=tkg.Radiobutton(addbook_scr,text='Add New Book',value=1,command= lambda: adding_book(addbook_scr)).grid(row=1,column=0)
        quan_rbutton=tkg.Radiobutton(addbook_scr,text='Update Info',value=2,command= lambda: update_info(addbook_scr)).grid(row=1,column=1)
        
def adding_book(c):

    adding_frame=tkg.LabelFrame(c)
    new_b=tkg.Label(adding_frame,text='Name of the book: ')
    new_b.grid(row=0,column=0)
    new_entry=tkg.Entry(adding_frame)
    new_entry.grid(row=0,column=1)
    b_code=tkg.Label(adding_frame,text='Book Code: ')
    b_code.grid(row=1,column=0)
    b_code_entry=tkg.Entry(adding_frame)
    b_code_entry.grid(row=1,column=1)
    genre_b=tkg.Label(adding_frame,text='Book Genre: ').grid(row=2,column=0)
    genre_b_entry=tkg.Entry(adding_frame)
    genre_b_entry.grid(row=2,column=1)
    author_name=tkg.Label(adding_frame,text='Name of Author: ').grid(row=3,column=0)
    author_name_entry=tkg.Entry(adding_frame)
    author_name_entry.grid(row=3,column=1)
    price_lab=tkg.Label(adding_frame,text='Price: ').grid(row=4,column=0)
    price_entry=tkg.Entry(adding_frame)
    price_entry.grid(row=4,column=1)
    no_copies_lab=tkg.Label(adding_frame,text='Number of Copies: ').grid(row=5,column=0)
    no_copies_entry=tkg.Entry(adding_frame)
    no_copies_entry.grid(row=5,column=1)
    done_button=tkg.Button(adding_frame,text='Add',command=lambda: dbentry(new_entry.get(),b_code_entry.get(),genre_b_entry.get(),author_name_entry.get(),price_entry.get(),no_copies_entry.get(),c)).grid(row=6,column=1,pady=20)
    adding_frame.grid(row=2,column=0,padx=20,pady=20)
    
def dbentry(a,b,c,d,e,f,g):
        book_log= mysql.connect(host='localhost',user='root',password='cbytes',database="bookshop_log")
        add_cursor=book_log.cursor()
        add_cursor.execute("select Bookid from book_log")
        existing_bcodes=add_cursor.fetchall()
        if int(b) in existing_bcodes[0]:
                msgbox.showinfo("Warning","Book Id already exists!")
        else:        
                add_cursor.execute("insert into book_log values('"+a+"',"+b+",'"+c+"','"+d+"',"+e+","+f+");")
                book_log.commit()
                book_log.close()
                msgbox.showinfo("DONE","Book Added")
                g.destroy()
        
def update_info(c):
        update_frame=tkg.LabelFrame(c)
        new_b=tkg.Label(update_frame,text='Name of the book: ')
        new_b.grid(row=0,column=0)
        new_entry=tkg.Entry(update_frame)
        new_entry.grid(row=0,column=1)
        b_code=tkg.Label(update_frame,text='Book Code: ')
        b_code.grid(row=1,column=0)
        b_code_entry=tkg.Entry(update_frame)
        b_code_entry.grid(row=1,column=1)
        genre_b=tkg.Label(update_frame,text='Book Genre: ').grid(row=2,column=0)
        genre_b_entry=tkg.Entry(update_frame)
        genre_b_entry.grid(row=2,column=1)
        author_name=tkg.Label(update_frame,text='Name of Author: ').grid(row=3,column=0)
        author_name_entry=tkg.Entry(update_frame)
        author_name_entry.grid(row=3,column=1)
        price_lab=tkg.Label(update_frame,text='Price: ').grid(row=4,column=0)
        price_entry=tkg.Entry(update_frame)
        price_entry.grid(row=4,column=1)
        no_copies_lab=tkg.Label(update_frame,text='Number of Copies: ').grid(row=5,column=0)
        no_copies_entry=tkg.Entry(update_frame)
        no_copies_entry.grid(row=5,column=1)
        get_info_button=tkg.Button(update_frame,text='Get Info',command=lambda: getting_upinfo(new_entry,b_code_entry.get(),genre_b_entry,author_name_entry,price_entry,no_copies_entry)).grid(row=7,column=0,pady=20)
        changed_button=tkg.Button(update_frame,text='Change',command=lambda: changing_info(new_entry.get(),b_code_entry.get(),genre_b_entry.get(),author_name_entry.get(),price_entry.get(),no_copies_entry.get(),c)).grid(row=7,column=1,pady=20)
        remove_button=tkg.Button(update_frame,text='Remove',command=lambda: remove_book(b_code_entry.get(),c)).grid(row=8,column=0,columnspan=2)
        update_frame.grid(row=2,column=1,padx=20,pady=20)

def changing_info(a,b,c,d,e,f,g):
        book_log= mysql.connect(host='localhost',user='root',password='cbytes',database="bookshop_log")
        change_cursor=book_log.cursor()
        if a=='' or b=='' or c=='' or d=='' or e=='' or f=='':
                msgbox.showinfo('Warning','All Fields are Compulsory!!')
                book_log.close()
        else:
                change_cursor.execute("update book_log set Name='"+a+"',Genre='"+c+"',Author='"+d+"',Price="+str(e)+",NOC="+str(f)+" where Bookid="+str(b))
                book_log.commit()
                book_log.close()
                msgbox.showinfo("DONE","Info Changed!")
                g.destroy()

def getting_upinfo(a,b,c,d,e,f):
        a.delete(0,20)
        c.delete(0,20)
        d.delete(0,20)
        e.delete(0,20)
        f.delete(0,20)
        try:
                book_log= mysql.connect(host='localhost',user='root',password='cbytes',database="bookshop_log")
                update_cursor=book_log.cursor()
                update_cursor.execute("select * from book_log where Bookid="+b+";")
                got_info=update_cursor.fetchall()
                a.insert(0,got_info[0][0])
                c.insert(0,got_info[0][2])                
                d.insert(0,got_info[0][3])
                e.insert(0,got_info[0][4])
                f.insert(0,got_info[0][5])
                book_log.close()
        except IndexError:
                msgbox.showinfo('Warning','Book Id does not exist!!')
                                 
def remove_book(a,b):
        book_log=mysql.connect(host='localhost',user='root',password='cbytes',database="bookshop_log")
        remove_cursor=book_log.cursor()
        remove_cursor.execute("delete from book_log where Bookid="+a+";")
        book_log.commit()
        msgbox.showinfo("DONE","Book removed")
        book_log.close()
        b.destroy()

#-----------------------------------------------------------------------ORDER_HISTORY_SCREEN-----------------------------------------------------------------------------

def ord_his():
        order_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        disp_cur=order_log.cursor()
        disp_cur.execute("select * from order_log")
        disp_data=disp_cur.fetchall()
        order_log.close()
        
        ord_history=tkg.Toplevel(parent)
        ord_history.iconbitmap('5faaf8e369d95204cf8848e495a983af.ico')
        ord_history.title('Order History')
        tkg.Label(ord_history,image=mainscreen_img,height=300).pack()
        tkg.Label(ord_history,text='Order History',font=('Courier',20)).pack()

        tkg.Label(ord_history,text='SEARCH ORDERS',font=('Courier',36)).place(x=560,y=40)
        srh_cri=tkg.Spinbox(ord_history,values=('Orderid','Custid','Name','Phone','Email','Bookid','DOP'))
        srh_cri.place(x=500,y=100)
        search_box=tkg.Entry(ord_history,width=40)
        search_box.place(x=645,y=99)
        search_button=tkg.Button(ord_history,text='SEARCH',command=lambda: search_result(srh_cri.get(),search_box.get())).place(x=900,y=98)

        bill_entry=tkg.Entry(ord_history,width=65)
        bill_entry.place(x=500,y=130)
        bill_pbutton=tkg.Button(ord_history,text='Print Bill',command=lambda: print_bill(0,0,0,0,bill_entry.get(),0,'h')).place(x=900,y=130)

        table_his=ttk.Treeview(ord_history)
        table_his.pack(pady=20)
        table_his['columns']=('1','2','3','4','5','6','7','8','9','10','11','12')
        table_his['show']='headings'

        table_his.column('1',width=120,anchor='c')
        table_his.column('2',width=120,anchor='c')
        table_his.column('3',width=120,anchor='c')
        table_his.column('4',width=120,anchor='c')
        table_his.column('5',width=120,anchor='c')
        table_his.column('6',width=120,anchor='c')
        table_his.column('7',width=120,anchor='c')
        table_his.column('8',width=120,anchor='c')
        table_his.column('9',width=120,anchor='c')
        table_his.column('10',width=120,anchor='c')
        table_his.column('11',width=120,anchor='c')
        table_his.column('12',width=120,anchor='c')

        table_his.heading('1',text='Order ID')
        table_his.heading('2',text='Cust ID')
        table_his.heading('3',text='Name')
        table_his.heading('4',text='Phone')
        table_his.heading('5',text='Email')
        table_his.heading('6',text='Book ID')
        table_his.heading('7',text='Price')
        table_his.heading('8',text='Price per Book')
        table_his.heading('9',text='NOC')
        table_his.heading('10',text='DOP')
        table_his.heading('11',text='Discount')
        table_his.heading('12',text='Discounted Price')

        for i in range(len(disp_data)):
                table_his.insert('','end',text='L1',values=(str(disp_data[i][0]),str(disp_data[i][1]),str(disp_data[i][8]),str(disp_data[i][2]),str(disp_data[i][3]),str(disp_data[i][4]),str(disp_data[i][6]),str(int(disp_data[i][6])/int(disp_data[i][5])),str(disp_data[i][5]),str(disp_data[i][7]),str(disp_data[i][9]),str(disp_data[i][10])))

def search_result(typ,sr):
        sr_result=tkg.Toplevel(parent)
        tkg.Label(sr_result,text='SEARCH RESULT',font=('Courier',24)).pack()

        order_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        disp_cur=order_log.cursor()
        if typ in ['Phone','Bookid']:
                disp_cur.execute("select * from order_log where "+typ+"="+sr+";")
        else:
                disp_cur.execute("select * from order_log where "+typ+"='"+sr+"';")
        disp_data=disp_cur.fetchall()
        order_log.close()
        sr_tab=ttk.Treeview(sr_result)
        sr_tab.pack()
        sr_tab['columns']=('1','2','3','4','5','6','7','8','9','10','11','12')
        sr_tab['show']='headings'

        sr_tab.column('1',width=120,anchor='c')
        sr_tab.column('2',width=120,anchor='c')
        sr_tab.column('3',width=120,anchor='c')
        sr_tab.column('4',width=120,anchor='c')
        sr_tab.column('5',width=120,anchor='c')
        sr_tab.column('6',width=120,anchor='c')
        sr_tab.column('7',width=120,anchor='c')
        sr_tab.column('8',width=120,anchor='c')
        sr_tab.column('9',width=120,anchor='c')
        sr_tab.column('10',width=120,anchor='c')
        sr_tab.column('11',width=120,anchor='c')
        sr_tab.column('12',width=120,anchor='c')

        sr_tab.heading('1',text='Order ID')
        sr_tab.heading('2',text='Cust ID')
        sr_tab.heading('3',text='Name')
        sr_tab.heading('4',text='Phone')
        sr_tab.heading('5',text='Email')
        sr_tab.heading('6',text='Book ID')
        sr_tab.heading('7',text='Price')
        sr_tab.heading('8',text='Price per Book')
        sr_tab.heading('9',text='NOC')
        sr_tab.heading('10',text='DOP')
        sr_tab.heading('11',text='Discount')
        sr_tab.heading('12',text='Discounted Price')

        for i in range(len(disp_data)):
                sr_tab.insert('','end',text='L1',values=(str(disp_data[i][0]),str(disp_data[i][1]),str(disp_data[i][8]),str(disp_data[i][2]),str(disp_data[i][3]),str(disp_data[i][4]),str(disp_data[i][6]),str(int(disp_data[i][6])/int(disp_data[i][5])),str(disp_data[i][5]),str(disp_data[i][7]),str(disp_data[i][9]),str(disp_data[i][10])))


#------------------------------------------------------------------------------ORDER_SCR---------------------------------------------------------------------------------
        
def order_screen():
        global book_data,quan_data,price_data
        book_data=[]
        quan_data=[]
        price_data=[]
        ord_scr=tkg.Toplevel(parent)
        ord_scr.iconbitmap('5faaf8e369d95204cf8848e495a983af.ico')
        ord_scr_image=tkg.Label(ord_scr,image=mainscreen_img,height=200,width=600).pack()

        tkg.Label(ord_scr,text='Billing Screen',font=('Courier',24)).place(x=175,y=80)

        cust_det_frame=tkg.Frame(ord_scr)
        cust_det_frame.pack(padx=70,pady=30)
        cust_code=tkg.Label(cust_det_frame,text='''Customer Code:
(type "None" if it is a non existing customer)''').grid(row=0,column=0)
        cust_code_entry=tkg.Entry(cust_det_frame)
        cust_code_entry.grid(row=0,column=1)
        ck_button=tkg.Button(cust_det_frame,text='Check',command=lambda: supplement2(ord_scr,cust_det_frame,cust_code_entry.get())).grid(row=1,column=0,columnspan=2)

def book_fr(main_scr,custfr,cust_code,name,phone,email):
        cust_data=[cust_code,name,phone,email]
        custfr.destroy()
        book_frame=tkg.Frame(main_scr)
        book_frame.pack(padx=70,pady=30)
        b_code_ord=tkg.Label(book_frame,text="Book Code: ").grid(row=0,column=0)
        b_code_entry=tkg.Entry(book_frame)
        b_code_entry.grid(row=0,column=1)

        display_table=ttk.Treeview(main_scr)
        display_table.pack(pady=30)
        display_table['columns']=('1','2','3')
        display_table['show']='headings'

        display_table.column('1',width=120,anchor='c')
        display_table.column('2',width=120,anchor='c')
        display_table.column('3',width=120,anchor='c')

        display_table.heading('1',text='Book Id')
        display_table.heading('2',text='Quantity')
        display_table.heading('3',text='Price')

        chk_button=tkg.Button(book_frame,text='Check',command=lambda: supplement1(book_frame,b_code_entry.get(),display_table,b_code_entry,cust_data,main_scr)).grid(row=1,column=0,columnspan=2)
def supplement1(a,b,c,d,cust_data,main_scr):
        info_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        info_cur=info_log.cursor()
        info_cur.execute("select Bookid from book_log;")
        data=info_cur.fetchall()
        for i in data:                        
                if int(b) in i:
                        info_cur.execute("select * from book_log where Bookid='"+str(b)+"';")
                        data=info_cur.fetchall()
                        lab1=tkg.Label(a,text='Name: '+str(data[0][0]))
                        lab1.grid(row=2,column=0,columnspan=2)
                        lab2=tkg.Label(a,text='Genre: '+str(data[0][2]))
                        lab2.grid(row=3,column=0,columnspan=2)
                        lab3=tkg.Label(a,text='Author: '+str(data[0][3]))
                        lab3.grid(row=4,column=0,columnspan=2)
                        lab4=tkg.Label(a,text='Price: '+str(data[0][4]))
                        lab4.grid(row=5,column=0,columnspan=2)
                        quan_b=tkg.Label(a,text='''Quantity:
Number of copies available:'''+str(data[0][5]))
                        quan_b.grid(row=6,column=0)
                        quan_entry=tkg.Entry(a,text=str(data[0][5]))
                        quan_entry.grid(row=6,column=1)
                        remove_button=tkg.Button(a,text='REMOVE',command=lambda: remove_bbill(lab1,lab2,lab3,lab4,quan_b,quan_entry,add_button))
                        remove_button.grid(row=7,column=1)
                        add_button=tkg.Button(a,text='ADD',command=lambda: add_tobill(int(data[0][5])-int(quan_entry.get()),a,b,str(data[0][4]),str(quan_entry.get()),c,d,lab1,lab2,lab3,lab4,quan_b,quan_entry,add_button))
                        add_button.grid(row=7,column=0)
                        info_log.close()
                        return
                make_bill_button=tkg.Button(a,text='Make Bill',command=lambda: make_bill(cust_data,book_data,quan_data,price_data,main_scr)).grid(row=8,column=0,columnspan=2,pady=5)
        msgbox.showinfo('Warning','This Book ID does not exist!')
        return

def remove_bbill(ph1,ph2,ph3,ph4,ph5,ph6,button):
        ph1.grid_forget()
        ph2.grid_forget()
        ph3.grid_forget()
        ph4.grid_forget()
        ph5.grid_forget()
        ph6.destroy()
        button.destroy()

def ord_code_gen():
        order_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        code_gen_cur=order_log.cursor()
        code_gen_cur.execute("select Orderid from order_log")
        temp=code_gen_cur.fetchall()
        existingcodes=[]
        ordcode='BSOL'+str(random.randint(1,100000000000))
        for i in temp:
                existingcodes.append(i[0])
        while str(ordcode) in existingcodes:
                ordcode='BSOL'+random.randint(1,100000000000)
        order_log.close()
        return ordcode
                                    
def add_tobill(remain,mainfr,code,price,quan,table,scrdes,ph1,ph2,ph3,ph4,ph5,ph6,button):
        temp_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        temp_cur=temp_log.cursor()
        temp_cur.execute("update book_log set NOC="+str(remain)+" where Bookid='"+str(code)+"';")
        temp_log.commit()
        temp_log.close()
        table.insert('','end',text='L1',values=(str(code),str(quan),str(int(price)*int(quan))))
        scrdes.delete(0,20)
        ph1.grid_forget()
        ph2.grid_forget()
        ph3.grid_forget()
        ph4.grid_forget()
        ph5.grid_forget()
        ph6.destroy()
        button.destroy()
        book_data.append(str(code))
        quan_data.append(str(quan))
        price_data.append(str(price))

def make_bill(cust_data,book_codes,quan_data,price_data,main_scr):
        order_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        order_cur=order_log.cursor()
        new_ord_code=ord_code_gen()
        today=str(datetime.date.today())
        
        for i in range(len(book_codes)):
                order_cur.execute("insert into order_log values('"+new_ord_code+"','"+cust_data[0]+"',"+str(cust_data[2])+",'"+cust_data[3]+"',"+str(book_codes[i])+","+str(quan_data[i])+","+str(int(price_data[i])*int(quan_data[i]))+",'"+today+"','"+cust_data[1]+"',"+'0'+","+str(int(price_data[i])*int(quan_data[i]))+");")
                order_log.commit()
        order_log.close()
        main_scr.destroy()
        print_bill(cust_data,book_codes,quan_data,price_data,new_ord_code,today,'o')

def print_bill(a,b,c,d,cd,date,typ):
        bill=tkg.Toplevel(parent)
        bill.iconbitmap('5faaf8e369d95204cf8848e495a983af.ico')
        
        if typ=='o':
                tkg.Label(bill,text='BOOKSOUL BOOKSTORE',font=('Courier',24)).grid(row=0,column=0,columnspan=3)
                tkg.Label(bill,text='Order ID '+str(cd),font=('Courier',20)).grid(row=1,column=0,columnspan=3)
                tkg.Label(bill,text='Customer ID: '+str(a[0])).grid(row=2,column=0)
                tkg.Label(bill,text='Name: '+str(a[1])).grid(row=3,column=0)
                tkg.Label(bill,text='Phone: '+str(a[2])).grid(row=4,column=0)
                tkg.Label(bill,text='Email: '+str(a[3])).grid(row=5,column=0)
                tkg.Label(bill,text='DOP: '+str(date)).grid(row=3,column=1,columnspan=2,rowspan=3)
                
                booklist=ttk.Treeview(bill)
                booklist.grid(row=6,column=0,columnspan=3,pady=30,padx=10)
                booklist['columns']=('1','2','3','4')
                booklist['show']='headings'

                booklist.column('1',width=120,anchor='c')
                booklist.column('2',width=120,anchor='c')
                booklist.column('3',width=120,anchor='c')
                booklist.column('4',width=120,anchor='c')
                
                booklist.heading('1',text='Book Id')
                booklist.heading('2',text='Quantity')
                booklist.heading('3',text='Price per Book')
                booklist.heading('4',text='Price')

                sum_l=[]
                
                for i in range(len(b)):
                        booklist.insert('','end',text='L1',values=(str(b[i]),str(c[i]),str(d[i]),str(int(d[i])*int(c[i]))))
                        sum_l.append(int(d[i])*int(c[i]))
                tkg.Label(bill,text='TOTAL:  '+str(sum(sum_l))).grid(row=7,column=0,columnspan=3,pady=20,padx=20,sticky='E')
                disc_button=msgbox.askquestion('Discount','Do you want to apply discount?')
                if disc_button=='yes':
                        discount(sum_l,str(a[0]),bill)
                else:
                        pass
                tkg.Label(bill,text='''Bill Invoice - BookSoul Bookstore
Ther are no other branches of this bookstore.
Items once sold will not be returned or changed.''').grid(row=10,column=0,columnspan=3,pady=40)
                tkg.Label(bill,text='THANK YOU',font=('Courier',16)).grid(row=11,column=0,columnspan=3)

        elif typ=='h':
                order_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
                disp_cur=order_log.cursor()
                disp_cur.execute("select * from order_log where Orderid='"+cd+"';")
                fetch_data=disp_cur.fetchall()

                tkg.Label(bill,text='BOOKSOUL BOOKSTORE',font=('Courier',24)).grid(row=0,column=0,columnspan=3)
                tkg.Label(bill,text='Order ID '+str(cd),font=('Courier',20)).grid(row=1,column=0,columnspan=3)
                tkg.Label(bill,text='Customer ID: '+str(fetch_data[0][1])).grid(row=2,column=0)
                tkg.Label(bill,text='Name: '+str(fetch_data[0][8])).grid(row=3,column=0)
                tkg.Label(bill,text='Phone: '+str(fetch_data[0][2])).grid(row=4,column=0)
                tkg.Label(bill,text='Email: '+str(fetch_data[0][3])).grid(row=5,column=0)
                tkg.Label(bill,text='DOP: '+str(fetch_data[0][7])).grid(row=3,column=1,columnspan=2,rowspan=3)
                                
                booklist=ttk.Treeview(bill)
                booklist.grid(row=6,column=0,columnspan=3,pady=30,padx=10)
                booklist['columns']=('1','2','3','4')
                booklist['show']='headings'

                booklist.column('1',width=120,anchor='c')
                booklist.column('2',width=120,anchor='c')
                booklist.column('3',width=120,anchor='c')
                booklist.column('4',width=120,anchor='c')
                
                booklist.heading('1',text='Book Id')
                booklist.heading('2',text='Quantity')
                booklist.heading('3',text='Price per Book')
                booklist.heading('4',text='Price')

                sum_l=[]
                for i in range(len(fetch_data)):
                        booklist.insert('','end',text='L1',values=(str(fetch_data[i][4]),str(fetch_data[i][5]),str(int(fetch_data[i][6])/int(fetch_data[i][5])),str(fetch_data[i][6])))
                        sum_l.append(int(fetch_data[i][6]))

                tkg.Label(bill,text='TOTAL:  '+str(sum(sum_l))).grid(row=7,column=0,columnspan=3,pady=20,padx=20,sticky='E')
                tkg.Label(bill,text='Discount: '+str(fetch_data[0][9])+'%').grid(row=8,column=0,columnspan=3,sticky='E')
                tkg.Label(bill,text='Discounted Rate: '+str(fetch_data[0][10])).grid(row=9,column=0,columnspan=3,sticky='E')
                tkg.Label(bill,text='''Bill Invoice - BookSoul Bookstore
Ther are no other branches of this bookstore.
Items once sold will not be returned or changed.
Subject to State Jurisdiction.''').grid(row=10,column=0,columnspan=3,pady=40)
                tkg.Label(bill,text='THANK YOU',font=('Courier',16)).grid(row=11,column=0,columnspan=3)
                        
def supplement2(main,a,b):
        if b.title()=='None':
                name_lab=tkg.Label(a,text='Name').grid(row=2,column=0)
                nameentry=tkg.Entry(a)
                nameentry.grid(row=2,column=1)
                phone_lab=tkg.Label(a,text='Phone No').grid(row=3,column=0)
                phone_entry=tkg.Entry(a)
                phone_entry.grid(row=3,column=1)
                email_lab=tkg.Label(a,text='Email').grid(row=4,column=0)
                email_entry=tkg.Entry(a)
                email_entry.grid(row=4,column=1)
                next_button=tkg.Button(a,text='Proceed',command=lambda: book_fr(main,a,b,nameentry.get(),phone_entry.get(),email_entry.get())).grid(row=6,column=0,columnspan=2)

        else:
                name_lab=tkg.Label(a,text='Name').grid(row=2,column=0)
                nameentry=tkg.Entry(a)
                nameentry.grid(row=2,column=1)
                phone_lab=tkg.Label(a,text='Phone No').grid(row=3,column=0)
                phone_entry=tkg.Entry(a)
                phone_entry.grid(row=3,column=1)
                email_lab=tkg.Label(a,text='Email').grid(row=4,column=0)
                email_entry=tkg.Entry(a)
                email_entry.grid(row=4,column=1)
                global cust_log,passing_cur
                cust_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
                passing_cur=cust_log.cursor()
                passing_cur.execute('select Custid from cust_log')
                list_id=passing_cur.fetchall()
                for i in list_id:
                        if str(i[0])==str(b):
                                passing_cur.execute("select * from Cust_log where Custid='"+str(b)+"';")
                                cust_info=passing_cur.fetchall()
                                nameentry.insert(0,cust_info[0][0])
                                phone_entry.insert(0,cust_info[0][2])
                                email_entry.insert(0,cust_info[0][3])
                                cust_log.close()
                                next_button=tkg.Button(a,text='Proceed',command=lambda: book_fr(main,a,b,nameentry.get(),phone_entry.get(),email_entry.get())).grid(row=6,column=0,columnspan=2)
                                return
                msgbox.showinfo('Warning','Id does not exist!!')
                cust_log.close()
                return

def discount(sum_l,code,invoice_scr):
        order_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        order_cur=order_log.cursor()
        disc=sum(sum_l)-(sum(sum_l)/10)
        order_cur.execute("update order_log set Discount=10 where Custid='"+code+"';")
        order_log.commit()
        order_cur.execute("update order_log set Discount_Price="+str(disc)+" where Custid='"+code+"';")
        order_log.commit()
        order_log.close()
        tkg.Label(invoice_scr,text='Discount: 10%').grid(row=8,column=0,columnspan=3,sticky='E')
        tkg.Label(invoice_scr,text='Discounted Rate: '+str(disc)).grid(row=9,column=0,columnspan=3,sticky='E')
       
#---------------------------------------------------------------------------CUSTOMER ID PAGE-------------------------------------------------------------------------------
#functions for customer id page
def customer_log():
    cust_log=tkg.Toplevel(parent)
    cust_log.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
    cust_log.title('Customer Login')
    cust_username=tkg.Label(cust_log,text='Customer Id: ')
    cust_username.grid(row=0,column=0,pady=10,padx=20)
    cust_pass=tkg.Label(cust_log,text='Customer Password: ')
    cust_pass.grid(row=1,column=0,pady=10,padx=20)
    cust_id=tkg.Entry(cust_log)
    cust_id.grid(row=0,column=1,pady=10,padx=20)
    pass_entry=tkg.Entry(cust_log,show='*')
    pass_entry.grid(row=1,column=1,pady=10,padx=20)

    submit_button=tkg.Button(cust_log,text='SUBMIT',command=lambda: check1(cust_id.get(),pass_entry.get(),cust_log))
    submit_button.grid(row=2,column=0,columnspan=2,pady=10)

def check1(a,b,c):
    cust_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
    check_cursor=cust_log.cursor()
    check_cursor.execute("select Custid from cust_log;")
    store_codes=check_cursor.fetchall()
    d=1
    for record in store_codes:
            if (str(a)) in record and b=='ABCD100':
                c.destroy()
                cust_log.close()
                cust_screen(a)
                d+=1
                break                
    if d==1:
        c.destroy()
        customer_log()

def cust_screen(a):
    cust_scr=tkg.Toplevel(parent)
    cust_scr.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
    cust_scr.title('Customer Screen')
    cust_img=tkg.Label(cust_scr,image=mainscreen_img,height=200,width=500)
    cust_img.grid(row=0,column=0,columnspan=2)
    prev_order_button=tkg.Button(cust_scr,text='Previous Order',width=35,height=5,command=lambda: prev_ord(a))
    prev_order_button.grid(row=1,column=0)
    change_info_button=tkg.Button(cust_scr,text='Change Info',width=35,height=5,command=lambda: change_info(a))
    change_info_button.grid(row=1,column=1)
    cust_info=tkg.Button(cust_scr,text='Customer Info',width=72,height=5,command= lambda: display_info(a))
    cust_info.grid(row=2,column=0,columnspan=2)

def change_info(a):
        cust_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        change_cur=cust_log.cursor()
        change_cur.execute("select * from cust_log where Custid='"+a+"';")
        data=change_cur.fetchall()
        cust_log.close()
                
        change_scr=tkg.Toplevel(parent)
        change_scr.iconbitmap('5faaf8e369d95204cf8848e495a983af.ico')
        tkg.Label(change_scr,image=mainscreen_img,width=400,height=200).grid(row=0,column=0,columnspan=2)
        tkg.Label(change_scr,text='Name ').grid(row=1,column=0,pady=10)
        name_entry=tkg.Entry(change_scr)
        name_entry.grid(row=1,column=1,pady=10)
        tkg.Label(change_scr,text='Phone ').grid(row=2,column=0,pady=10)
        phone_entry=tkg.Entry(change_scr)
        phone_entry.grid(row=2,column=1,pady=10)
        tkg.Label(change_scr,text='Email ').grid(row=3,column=0,pady=10)
        email_entry=tkg.Entry(change_scr)
        email_entry.grid(row=3,column=1,pady=10)

        name_entry.insert(0,str(data[0][0]))
        phone_entry.insert(0,str(data[0][2]))
        email_entry.insert(0,str(data[0][3]))

        update_button=tkg.Button(change_scr,text='Update',command=lambda: update(a,name_entry.get(),phone_entry.get(),email_entry.get(),change_scr))
        update_button.grid(row=4,column=0,columnspan=2,pady=10)
        
def update(ID,a,b,c,scr):
        cust_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        update_cur=cust_log.cursor()
        update_cur.execute("update cust_log set Name='"+a+"', Phone="+b+", Email='"+c+"' where Custid='"+ID+"';")
        cust_log.commit()
        cust_log.close()
        msgbox.showinfo('Update Status','Updated Successfully')
        scr.destroy()

def prev_ord(a):
        prev_scr=tkg.Toplevel(parent)
        prev_scr.iconbitmap('5faaf8e369d95204cf8848e495a983af.ico')
        tkg.Label(prev_scr,text='Previous Orders',font=('Courier',24)).pack()

        order_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        disp_cur=order_log.cursor()
        disp_cur.execute("select * from order_log where Custid='"+a+"';")
        disp_data=disp_cur.fetchall()
        order_log.close()
        
        prev=ttk.Treeview(prev_scr)
        prev.pack()
        prev['columns']=('1','2','3','4','5','6','7','8','9','10','11','12')
        prev['show']='headings'

        prev.column('1',width=120,anchor='c')
        prev.column('2',width=120,anchor='c')
        prev.column('3',width=120,anchor='c')
        prev.column('4',width=120,anchor='c')
        prev.column('5',width=120,anchor='c')
        prev.column('6',width=120,anchor='c')
        prev.column('7',width=120,anchor='c')
        prev.column('8',width=120,anchor='c')
        prev.column('9',width=120,anchor='c')
        prev.column('10',width=120,anchor='c')
        prev.column('11',width=120,anchor='c')
        prev.column('12',width=120,anchor='c')

        prev.heading('1',text='Order ID')
        prev.heading('2',text='Cust ID')
        prev.heading('3',text='Name')
        prev.heading('4',text='Phone')
        prev.heading('5',text='Email')
        prev.heading('6',text='Book ID')
        prev.heading('7',text='Price')
        prev.heading('8',text='Price per Book')
        prev.heading('9',text='NOC')
        prev.heading('10',text='DOP')
        prev.heading('11',text='Discount')
        prev.heading('12',text='Discounted Price')

        for i in range(len(disp_data)):
                prev.insert('','end',text='L1',values=(str(disp_data[i][0]),str(disp_data[i][1]),str(disp_data[i][8]),str(disp_data[i][2]),str(disp_data[i][3]),str(disp_data[i][4]),str(disp_data[i][6]),str(int(disp_data[i][6])/int(disp_data[i][5])),str(disp_data[i][5]),str(disp_data[i][7]),str(disp_data[i][9]),str(disp_data[i][10])))

        
def display_info(a):
        info_scr=tkg.Toplevel(parent)
        info_scr_img=tkg.Label(info_scr,image=mainscreen_img,height=40,width=130).grid(row=0,column=0,columnspan=2)
        info_scr.iconbitmap('5faaf8e369d95204cf8848e495a983af.ico')
        cust_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        cruise_cursor=cust_log.cursor()
        cruise_cursor.execute("select * from cust_log where Custid='"+a+"';")
        cust_data=cruise_cursor.fetchall()
        tkg.Label(info_scr,text='Name: ').grid(row=1,column=0)
        tkg.Label(info_scr,text='Cust ID: ').grid(row=2,column=0)
        tkg.Label(info_scr,text='Phone: ').grid(row=3,column=0)
        tkg.Label(info_scr,text='Email: ').grid(row=4,column=0)
        for i in cust_data[0]:
               tkg.Label(info_scr,text=i).grid(row=cust_data[0].index(i)+1,column=1)
        cust_log.close()
        
#---------------------------------------------------------------------------NEW CUSTOMER/Customer Info----------------------------------------------------------------------------------    
def new_customer():
        new_cust=tkg.Toplevel(parent)
        new_cust.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
        new_cust_img=tkg.Label(new_cust,image=mainscreen_img,height=200,width=400).grid(row=0,column=0,columnspan=2)
        cust_name_lab=tkg.Label(new_cust,text='Name: ').grid(row=1,column=0)
        cust_name_entry=tkg.Entry(new_cust)
        cust_name_entry.grid(row=1,column=1)
        cust_id=tkg.Label(new_cust,text='Customer ID: ').grid(row=2,column=0)
        text_code=code_gen()
        cust_id_disp=tkg.Label(new_cust,text=text_code).grid(row=2,column=1)
        phone_lab=tkg.Label(new_cust,text='Phone: ').grid(row=3,column=0)
        phone_entry=tkg.Entry(new_cust)
        phone_entry.grid(row=3,column=1)
        email_lab=tkg.Label(new_cust,text='Email: ').grid(row=4,column=0)
        email_entry=tkg.Entry(new_cust)
        email_entry.grid(row=4,column=1)
        add_button_info=tkg.Button(new_cust,text='ADD',command= lambda: add_cust_info(cust_name_entry.get(),text_code,phone_entry.get(),email_entry.get(),new_cust)).grid(row=5,column=0,columnspan=2)
def code_gen():
        cust_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        customer_cursor=cust_log.cursor()
        customer_cursor.execute("select Custid from cust_log")
        temp=customer_cursor.fetchall()
        existing_codes=[]
        code_gen_wr='BMS#'+str(random.randint(1,1000000))
        for i in temp:
                existing_codes.append(i[0])
        while str(code_gen_wr) in existing_codes:
                code_gen_wr='BMS#'+str(random.randint(1,1000000))
        cust_log.close()
        return code_gen_wr
def add_cust_info(a,b,c,d,e):
        cust_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        add_cust_cursor=cust_log.cursor()
        if a=='' or b=='' or c=='' or d=='' :
                msgbox.showinfo('Warning','All fields are mandatory!')
        else:
                add_cust_cursor.execute("insert into cust_log values('"+a+"','"+b+"',"+c+",'"+d+"');")
                cust_log.commit()
                e.destroy()
        cust_log.close()
#--------------------------------------------------------------------------BROWSE BOOKS PAGE------------------------------------------------------------------------------
#function for browse books page
# column headings:  SNo., Name of book, author, total copies, copies left, genre, price, 
def bbooks():
        book_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        disp_cursor=book_log.cursor()
        browse=tkg.Toplevel(parent,bg='white')
        browse.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
        browse.geometry('720x500')
        tkg.Label(browse,image=mainscreen_img,height=200,width=800).pack(side='top')
        heading=tkg.Label(browse,text='BROWSE BOOKS',font=("Courier", 24))
        heading.place(x=250,y=65)
        search_txt=tkg.Button(browse,text='SEARCH',font=('Courier',18),command=lambda: searchbook(search_bar.get(),opt_menu.get()))
        search_txt.place(x=580,y=110)
        search_bar=tkg.Entry(browse,width=60)
        search_bar.place(x=210,y=125)
        opt_menu=tkg.Spinbox(browse,values=('Name','Genre','Author'))
        opt_menu.place(x=70,y=125)
        disp_cursor.execute("select * from book_log;")
        all_data=disp_cursor.fetchall()
        display_table=ttk.Treeview(browse)
        display_table.pack(side='right')
        display_table['columns']=('1','2','3','4','5','6')
        display_table['show']='headings'

        display_table.column('1',width=120,anchor='c')
        display_table.column('2',width=120,anchor='c')
        display_table.column('3',width=120,anchor='c')
        display_table.column('4',width=120,anchor='c')
        display_table.column('5',width=120,anchor='c')
        display_table.column('6',width=120,anchor='c')

        display_table.heading('1',text='Name')
        display_table.heading('2',text='Book ID')
        display_table.heading('3',text='Genre')
        display_table.heading('4',text='Author')
        display_table.heading('5',text='Price')
        display_table.heading('6',text='No of Copies')
        
        for Row in range(len(all_data)):
               display_table.insert('','end',text='L1',values=(str(all_data[Row][0]),str(all_data[Row][1]),str(all_data[Row][2]),str(all_data[Row][3]),str(all_data[Row][4]),str(all_data[Row][5])))
        book_log.close()


def searchbook(sr,ty):
        if sr=='':
                msgbox.showinfo('Warning','Search Field Is Empty!!')
                return
        search_result=tkg.Toplevel(parent)
        search_result.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
        tkg.Label(search_result,image=mainscreen_img,height=100,width=720).pack()
        tkg.Label(search_result,text='Search Result',font=('Courier',24)).place(x=240,y=30)
        book_log=mysql.connect(host='localhost',user='root',password='cbytes',database='bookshop_log')
        all_data=book_log.cursor()
        all_data.execute("select * from book_log where "+str(ty)+" like '%"+str(sr).title()+"%';")
        search_data=all_data.fetchall()
        
        display_table=ttk.Treeview(search_result)
        display_table.pack(side='right')
        display_table['columns']=('1','2','3','4','5','6')
        display_table['show']='headings'

        display_table.column('1',width=120,anchor='c')
        display_table.column('2',width=120,anchor='c')
        display_table.column('3',width=120,anchor='c')
        display_table.column('4',width=120,anchor='c')
        display_table.column('5',width=120,anchor='c')
        display_table.column('6',width=120,anchor='c')

        display_table.heading('1',text='Name')
        display_table.heading('2',text='Book ID')
        display_table.heading('3',text='Genre')
        display_table.heading('4',text='Author')
        display_table.heading('5',text='Price')
        display_table.heading('6',text='No of Copies')
        
        for Row in range(len(search_data)):
               display_table.insert('','end',text='L1',values=(str(search_data[Row][0]),str(search_data[Row][1]),str(search_data[Row][2]),str(search_data[Row][3]),str(search_data[Row][4]),str(search_data[Row][5])))
        book_log.close()
       
#-------------------------------------------------------------------------------MAINLOOP-----------------------------------------------------------------------------------
parent=tkg.Tk()
parent.title('BookSoul Bookstore')  
#icon editing and image
parent.iconbitmap("5faaf8e369d95204cf8848e495a983af.ico")
mainscreen_img=ImageTk.PhotoImage(Image.open("1884665.jpg"))
mainimage_lab=tkg.Label(parent,image=mainscreen_img, height=200, width=500)
mainimage_lab.grid(row=0, column=0,columnspan=2)
#welcome text
welcome_text=tkg.Label(parent,text="BOOKSOUL BOOKSTORE")
welcome_text.config(anchor="center", font=("Courier","25"))
welcome_text.grid(row=1, column=0, columnspan=2)
#adding widgets mainframe
adminlog_button=tkg.Button(parent,text="Admin Login",width=35,height=5,command=lambda: adminlog())
adminlog_button.grid(row=3,column=0)
browse_button=tkg.Button(parent, text="Browse Books", width=35, height=5,command=bbooks)
browse_button.grid(row=3,column=1)

tkg.Label(parent,text='Made BY: AAYUSHMAAN GARG',font=('Courier',20)).grid(row=4,column=0,columnspan=2,pady=20)
parent.mainloop()

