from customtkinter import *
from tkfontchooser import askfont
from os import listdir
from PIL import Image
import sqlite3 as q

t = CTk()
# t.overrideredirect(True)
t.attributes("-alpha", 0.6)
t.geometry(f"900x600+300+150")
t.resizable(False, False)
t.title("Parch Profiler")

set_appearance_mode("dark")
conn = q.connect("database.db")
cur = conn.cursor()

cur.execute("SELECT * FROM theme")
if (color := next(cur)[-1]) in ["dark-blue", "blue", "green"] :
    set_default_color_theme(color)
else :
    set_default_color_theme("CTkThemesPack/themes/" + color + ".json")

cur.execute("SELECT * FROM font")
font = next(cur)
conn.commit()
conn.close()


def ch_pps() :
    softwaremgr_frame.grid_forget()
    profmgr_frame.grid(row=0, column=1, columnspan=3, padx=(250, 0), pady=(170, 0))


def ch_sm() :
    profmgr_frame.grid_forget()
    softwaremgr_frame.grid(row=0, column=1, columnspan=3, padx=(250, 0), pady=(170, 0))


def settings() :
    t.withdraw()
    sw = CTkToplevel(t)
    sw.bind("<Destroy>", lambda x : t.deiconify())
    sw.geometry("+750+250")

    sw.resizable(False, False)

    def chth(choice) :
        conn = q.connect("database.db")
        conn.cursor().execute(f"UPDATE theme SET name='{choice}'")
        conn.commit()
        conn.close()
        lbl.grid(padx=10, pady=10)

    def chfnt() :
        sw.withdraw()
        if font := askfont(apear_tab, "choose font") :
            conn = q.connect("database.db")
            cur = conn.cursor()
            cur.execute(f"UPDATE font SET family='{font['family']}'")
            cur.execute(f"UPDATE font SET font_size='{font['size']}'")
            cur.execute(f"UPDATE font SET effect='{font['weight']}'")
            conn.commit()
            conn.close()
            lbl.grid(padx=10, pady=10)
        sw.deiconify()

    apear_tab = CTkTabview(sw, width=300, height=300)
    apear_tab.add("settings")
    apear_tab.add("appearance")
    lbl = CTkLabel(sw, text="restart to apply")
    values = [i.replace(".json", "") for i in listdir("CTkThemesPack/themes")]
    values.append("dark-blue")
    values.append("blue")
    values.append("green")
    ts = CTkOptionMenu(apear_tab.tab("appearance"), font=font, values=values, anchor="center", corner_radius=10, command=chth)
    ts.set(color)
    ts.grid(padx=80, pady=50)

    apear_tab.add("font")
    CTkButton(apear_tab.tab("font"), text="choose font".title(), font=font, corner_radius=999, command=chfnt).grid(padx=80, pady=50)

    apear_tab.grid()
    sw.mainloop()


chfr_frame = CTkScrollableFrame(t, corner_radius=0, height=600, width=150)
chfr_frame.grid(row=0, rowspan=2, column=0)
settings_frame = CTkFrame(chfr_frame)
CTkLabel(settings_frame, text="Parch Profiler").grid(row=0, column=0, padx=10, pady=(10, 20))
settings_btn = CTkButton(settings_frame, text="", width=1, font=font, corner_radius=999, image=CTkImage(
    Image.open("/home/ghost/parch-profiler-stable/GUI/CTkThemesPack/images/settings.png")),
          command=settings)
settings_btn.grid(row=0, column=1, pady=(0, 10))
settings_frame.grid(row=0, column=0)
CTkButton(chfr_frame, text="Software Managers", font=font, corner_radius=999, command=ch_sm).grid(row=1, column=0, pady=5)
CTkButton(chfr_frame, text="Parch Profile Stable", font=font, corner_radius=999, command=ch_pps).grid(row=2, column=0, pady=5)

plcholder_drame = CTkFrame(t, corner_radius=0, height=28, width=526)
plcholder_drame.grid(row=1, column=1)

btn_frame = CTkFrame(t, corner_radius=0)
btn_frame.grid(row=1, column=2)
bl = CTkButton(btn_frame, text="import", width=60);bl.grid(row=1, column=1, padx=5)
be = CTkButton(btn_frame, text="export", width=60);be.grid(row=1, column=2, padx=5)
ba = CTkButton(btn_frame, text="apply", width=60);ba.grid(row=1, column=3, padx=5)

content_frame = CTkScrollableFrame(t, corner_radius=0, height=572, width=720)
content_frame.grid(row=0, column=1, columnspan=2)

softwaremgr_frame = CTkFrame(content_frame)
softwaremgr_frame.grid(row=0, column=1, columnspan=3, padx=(250, 0), pady=(170, 0))
bl = CTkLabel(softwaremgr_frame, text="Select your software manager");bl.grid(padx=10, pady=10)
bl = CTkButton(softwaremgr_frame, text="pacman ➜", font=font, corner_radius=999);bl.grid(padx=10, pady=10)
be = CTkButton(softwaremgr_frame, text="AUR ➜", font=font, corner_radius=999);be.grid(padx=10, pady=10)
ba = CTkButton(softwaremgr_frame, text="FlatPak ➜", font=font, corner_radius=999);ba.grid(padx=10, pady=10)

profmgr_frame = CTkFrame(content_frame, fg_color="yellow")

t.mainloop()