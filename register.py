import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import time, json, mysql.connector, os
from PIL import Image, ImageTk
from dotenv import load_dotenv

load_dotenv()
hostname = os.getenv('HOSTNAME')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
table = os.getenv('TABLE')

mydb = mysql.connector.connect(host=hostname, user=username, password=password, database=database)
if not mydb:
  exit()
history = {}

def showname():
  pass
def register():
  
  x,pw, cnfmpw, crntime = name.get(), password.get(), confirmPassword.get(), time.strftime('%D - %H:%M:%S', time.localtime())
  if x and len(pw) >5 and cnfmpw == pw:
    history[x] = crntime
    sql = f"INSERT INTO {table}(name, password) value ('{x}', '{pw}');"
    with mydb.cursor() as cursor:
      cursor.execute(sql)
      showinfo(title='registration status', message='user ' + x +  ' successfully registered')
      mydb.commit()
  elif len(pw) <6:
    showinfo(title='registration status', message='password must be more than 5 character')
  elif pw != cnfmpw:
    showinfo(title='registration status', message='password does not match')
  else:
    print('error occur')
    showinfo(title='registeration status', message='error occurs, please retry')
def showpass():
  passEntry.config(show='')
  confirmPassEntry.config(show='')
  showPassBtn.config(image=hidpassimg)
  showPassBtn.config(command=hidpass)
def hidpass():
  passEntry.config(show='X')
  confirmPassEntry.config(show='X')
  showPassBtn.config(image=showpassimg)
  showPassBtn.config(command=showpass)
  

root = tk.Tk()
root.title('9-Cheerful')
root.geometry('300x300')
root.resizable(True, True)
name = tk.StringVar() 
password = tk.StringVar()
confirmPassword= tk.StringVar()

registerSection = ttk.Frame(root)
registerSection.pack(padx=5, pady=5, fill='x', expand=True)
nameLabel = ttk.Label(registerSection, text='name: ')
nameLabel.pack(padx=5, pady=5, expand=True,  fill='x')

nameEntry = ttk.Entry(registerSection, textvariable=name, show='') #show='x' for password entry
nameEntry.pack(expand=True, fill='x', )
nameEntry.focus()

passLabel = ttk.Label(registerSection, text='password: ').pack(padx=5, pady=5, expand=True, fill='x')

passEntry = ttk.Entry(registerSection, textvariable=password, show='X')
passEntry.pack(padx=5, pady=5, expand=True, fill='x')

confirmPassLabel = ttk.Label(registerSection, text='retype: ').pack(padx=5, pady=5, expand=True, fill='x')

confirmPassEntry = ttk.Entry(registerSection, textvariable=confirmPassword, show='X')
confirmPassEntry.pack(padx=5, pady=5, expand=True, fill='x')

showpassimg = Image.open('OIP.jpeg')
showpassimg = showpassimg.resize((40, 20))
showpassimg = ImageTk.PhotoImage(showpassimg)

hidpassimg = Image.open('10863657.png')
hidpassimg = hidpassimg.resize((40, 20))
hidpassimg = ImageTk.PhotoImage(hidpassimg)


showPassBtn = ttk.Button(registerSection, compound=tk.RIGHT, image=showpassimg, command=showpass)
showPassBtn.pack(padx=5, pady=5, expand=True, side='left')

confirmBtn = ttk.Button(registerSection, text='register', command=register)
confirmBtn.pack(padx=5, pady=5, expand=True, side='right')

checkBtn = ttk.Button(registerSection, text='check', command=showname).pack(padx=5, pady=5, expand=True, side='right')

root.mainloop()
print(history)
with open('registerlog.txt', mode='a') as file:
  for key, val in history.items():
    file.write(key +' - '+ val +'\n')
# with open('registerLog.json', 'r+') as regLog:
#   jsondata=json.load(regLog)
#   for i in history:
#     jsondata['reglog'].append(i.item())
#   regLog.seek(0)
#   json.dump(jsondata, regLog, indent=4)