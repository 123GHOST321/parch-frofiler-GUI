from customtkinter import *
from PIL import Image

t = CTk()
t.geometry("900x600")
t.resizable(False, False)
t.title("Parch Profiler")


def ch_pps() :
    softwaremgr_frame.grid_forget()
    profmgr_frame.grid(row=0, column=1, columnspan=3, pady=10, padx=10)


def ch_sm() :
    profmgr_frame.grid_forget()
    softwaremgr_frame.grid(row=0, column=1, columnspan=3, pady=10, padx=10)


chfr_frame = CTkScrollableFrame(t, corner_radius=0, height=600)
settings_frame = CTkFrame(chfr_frame)
CTkLabel(settings_frame, text="Parch Profiler").grid(row=0, column=0, padx=10)
CTkButton(settings_frame, text="", fg_color="#dbdbdb", hover_color="#9a9a9a", width=10, image=CTkImage(
    Image.open("/home/ghost/parch-profiler-stable/GUI/images/settings.png")
)).grid(row=0, column=1, pady=10)
settings_frame.grid(row=0, column=0)
CTkButton(chfr_frame, text="Parch Profile Stable", command=ch_pps).grid(row=1, column=0, pady=5)
CTkButton(chfr_frame, text="Software Managers", command=ch_sm).grid(row=2, column=0, pady=5)
chfr_frame.grid(row=0, rowspan=2, column=0)

bl = CTkButton(t, text="load", width=8);bl.grid(row=1, column=1, padx=3, pady=10)
be = CTkButton(t, text="export", width=8);be.grid(row=1, column=2, padx=3, pady=10)
ba = CTkButton(t, text="apply", width=8);ba.grid(row=1, column=3, padx=3, pady=10)

softwaremgr_frame = CTkFrame(t)
bl = CTkLabel(softwaremgr_frame, text="Select your software manager");bl.grid(padx=10, pady=10)
bl = CTkButton(softwaremgr_frame, text="pacman ➜");bl.grid(padx=10, pady=10)
be = CTkButton(softwaremgr_frame, text="AUR ➜");be.grid(padx=10, pady=10)
ba = CTkButton(softwaremgr_frame, text="FlatPak ➜");ba.grid(padx=10, pady=10)

profmgr_frame = CTkFrame(t, height=430)
profmgr_frame.grid(row=0, column=1, columnspan=3, pady=10, padx=10)

t.mainloop()
