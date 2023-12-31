from tkinter import *
from tkinter import ttk 
from tkinter import messagebox 

def inserir():
    if vid.get()=="" or vnomeproduto.get()=="" or vdescricao.get()=="" or vregistro.get()=="" or vquantiloja.get()=="" or vquantiestoque.get()=="":
       messagebox.showinfo(title="ERRO", message="Digite todos os dados")
       return
    tv.insert("","end",values=(vid.get(),vnomeproduto.get(),vdescricao.get(),vregistro.get(),vquantiloja.get(),vquantiestoque.get()))
    vid.delete(0,END)
    vnomeproduto.delete(0,END)
    vdescricao.delete(0,END)
    vregistro.delete(0,END)
    vquantiloja.delete(0,END)
    vquantiestoque.delete(0,END)
    vid.focus()

def deletar():
    try:  
        itemSelecionado=tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")

def obter():
    try:  
        itemSelecionado=tv.selection()[0]
        valores=tv.item(itemSelecionado,"values")
        print("ID............:" + valores[0])
        print("Produto.......:"+ valores[1])
        print("Descrição.....:"+ valores[2])
        print("Num Registro..:" + valores[3])
        print("Qntd Loja.....:" + valores[4])
        print("Qntd Estoque..:" + valores[5])
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser mostrado")

app=Tk()
app.title("Loja Eletroeletrônica")
app.geometry("850x300")

lbid=Label(app,text="ID")#,anchor=W)
vid=Entry(app)

lbnomeproduto=Label(app,text="Produto")#,anchor=W)
vnomeproduto=Entry(app)

lbdescricao=Label(app,text="Descrição")#,anchor=W)
vdescricao=Entry(app)

lbregistro=Label(app,text="N Registro")#,anchor=W)
vregistro=Entry(app)

lbquantiloja=Label(app,text="Qntd Loja")#,anchor=W)
vquantiloja=Entry(app)

lbquantiestoque=Label(app,text="Qntd Estoque")#,anchor=W)
vquantiestoque=Entry(app)

tv=ttk.Treeview(app,columns=('id','nomeproduto','descricao','registro','quantiloja','quantiestoque'), show='headings')

tv.column('id',minwidth=0,width=140)
tv.column('nomeproduto',minwidth=0,width=140)
tv.column('descricao',minwidth=0,width=140)
tv.column('registro',minwidth=0,width=140)
tv.column('quantiloja',minwidth=0,width=140)
tv.column('quantiestoque',minwidth=0,width=140)

tv.heading('id',text='ID')
tv.heading('nomeproduto',text='Produto')
tv.heading('descricao',text='Descrição')
tv.heading('registro',text='N Registro')
tv.heading('quantiloja',text='Qntd Loja')
tv.heading('quantiestoque',text='Qntd Estoque')

btn_inserir=Button(app,text="Inserir",command=inserir)
btn_deletar=Button(app,text="Deletar",command=deletar)
btn_obter=Button(app,text="Obter",command=obter)

lbid.grid(column=0,row=0,sticky="w")
vid.grid(column=0,row=1,sticky="w")

lbnomeproduto.grid(column=1,row=0)
vnomeproduto.grid(column=1,row=1)

lbdescricao.grid(column=2,row=0)
vdescricao.grid(column=2,row=1)

lbregistro.grid(column=3,row=0)
vregistro.grid(column=3,row=1)

lbquantiloja.grid(column=4,row=0)
vquantiloja.grid(column=4,row=1)

lbquantiestoque.grid(column=5,row=0)
vquantiestoque.grid(column=5,row=1)

btn_inserir.grid(column=2,row=8)
btn_deletar.grid(column=3,row=8)
btn_obter.grid(column=4,row=8)

tv.grid(column=0,row=6,columnspan=6)

app.mainloop()
