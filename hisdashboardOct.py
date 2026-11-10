import matplotlib.pyplot as plt
import psycopg2
import os
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

conn = psycopg2.connect(
    dbname=os.environ['DBNAME'],
    user=os.environ['DBUSER'],
    host=os.environ['DBHOST'],
    password=os.environ['DBPASSWORD'])
curs=conn.cursor()

#plt.show()

def update_plot(axes,canvas):
    global  conn,curs
    """Clears the old data and draws a new random wave configuration."""
    # Clear previous elements on the axis
    axes[0].clear()
    axes[1].clear()
    axes[2].clear()
    #start=input("Enter the start date in YYYY-MM-DD format:")
    #end=input("Enter the end date in YYYY-MM-DD format:")
    start="2026-10-01"
    end="2026-10-31"
    where=f"where time>=TIMESTAMP '{start}' and time<TIMESTAMP '{end}'"
    #where=""
    curs.execute(f"select time,disc,temp from dataOct {where}")
    rows=curs.fetchall()
    x=[]
    y=[]
    for r in rows:
        y.append(r[1])
        x.append(r[2])

    curs.execute(f"""select 
    corr(disc,temp) as corrDT,
    min(temp) as minT,
    max(temp) as maxT,
    avg(temp) as meanT,
    stddev(temp) as stdT,
    min(disc) as minD,
    max(disc) as maxD,
    avg(disc) as meanD,
    stddev(disc) as stdD
    from dataOct {where}""");
    row=curs.fetchone()
    print (row[1])

#    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4))
    #plt.title("Colorado River in Oct 2026")
    axes[0].scatter(x, y,marker='x',s=10)
    axes[0].set_title("Temperature vs Discharge")
    axes[0].set_xlabel("Temp degC")
    axes[0].set_ylabel("Discharge ft^3/s")
    axes[0].text(0.5, 0.9,f"Corr:{row[0]:.3f}",transform=axes[0].transAxes)

    axes[1].hist(x,bins=30)
    axes[1].set_title("Temperature")
    axes[1].set_xlabel("degC")
    axes[1].set_ylabel("Count")
    axes[1].text(0.5, 0.9,f"Min:{row[1]}",transform=axes[1].transAxes)
    axes[1].text(0.5, 0.8,f"Max:{row[2]}",transform=axes[1].transAxes)
    axes[1].text(0.5, 0.7,f"Mean:{row[3]:.1f}",transform=axes[1].transAxes)
    axes[1].text(0.5, 0.6,f"Stdev:{row[4]:.1f}",transform=axes[1].transAxes)

    axes[2].hist(y,bins=30)
    axes[2].set_title("Discharge")
    axes[2].set_xlabel("ft^3/s")
    axes[2].set_ylabel("Count")
    axes[2].text(0.5, 0.9,f"Min:{row[5]}",transform=axes[2].transAxes)
    axes[2].text(0.5, 0.8,f"Max:{row[6]}",transform=axes[2].transAxes)
    axes[2].text(0.5, 0.7,f"Mean:{row[7]:.1f}",transform=axes[2].transAxes)
    axes[2].text(0.5, 0.6,f"Stdev:{row[8]:.1f}",transform=axes[2].transAxes)

    # Refresh the Tkinter canvas wrapper
    canvas.draw()

root = Tk()
root.geometry("1024x600")
frm = Frame(root)
frm.grid()

Label(frm, text="Label Placeholder:").grid(column=0, row=0)
fig = Figure(figsize=(8.5, 4), dpi=100)
axes=[]
axes.append(fig.add_subplot(1,3,1))
axes.append(fig.add_subplot(1,3,2))
axes.append(fig.add_subplot(1,3,3))
canvas = FigureCanvasTkAgg(fig, master=frm)
canvas_widget = canvas.get_tk_widget().grid(column=0, row=1,columnspan=4,rowspan=4)
Button(frm, text="Update", command=lambda :update_plot(axes,canvas)).grid(column=0, row=5)
root.mainloop()