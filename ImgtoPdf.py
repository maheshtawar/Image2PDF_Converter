# pip install img2pdf 
from email.mime import image
from tkinter import *
from tkinter import Label, PhotoImage
from PIL import ImageTk, Image
import os
from tkinter import filedialog

# GUI application window
root = Tk()
root.title('IMAGE TO PDF CONVERTER')
# root.geometry("260x160")
root.geometry('620x500')
root.iconphoto(False, PhotoImage(file = 'JPG-to-PDF.png'))
root.resizable(False, False)

def disable(btn):
    btn['state']='disabled'

def enable(btn):
    btn['state']='active'

files = {}
def upload_imgs():
    global files
    files['filename']=filedialog.askopenfilenames(filetypes=[('JPG','*.jpg'),('PNG','*.png'),('JPEG','*.jpeg')],
    initialdir = os.getcwd(), title='Select File/Files')
    if len(files['filename'])!=0:
        enable(download_button)
    

def saveas():
    try:
        img_list = []
        for file in files['filename']:
            img_list.append(Image.open(file).convert('RGB'))
        save_file_name = filedialog.asksaveasfilename(filetypes = [('PDF','*.pdf')], initialdir=os.getcwd(), title='Save File')
        img_list[0].save(f'{save_file_name}.pdf', save_all=True, append_images = img_list[1:])
        disable(download_button)
    except:
        return



# Image
photo = PhotoImage(file="JPG-to-PDF.png")
label1 = Label(root,image=photo,width=600,height=200).grid(pady=20)
# /Image

# upload button
upload_button = Button(root, text='UPLOAD IMAGES',font=('arial',14,'bold'), bg='white',fg='green', command=upload_imgs)
upload_button.grid(row =1, column = 0, padx=5, pady =10)

# Download button
download_button = Button(root, text='DOWNLOAD PDF',font=('arial',14,'bold'), bg='white',fg='red', command=saveas)
download_button.grid(row=2, column=0,padx=5,pady=10)
disable(download_button)




title_label=Label(root,text="Design & Develop by Mahesh Tawar",font="Arial 7").grid(padx=10,pady=10)

root.mainloop()