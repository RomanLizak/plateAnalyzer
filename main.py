
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

# Function to configure the scrollbar
def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Functions to handle scrolling with mouse wheel and touchpad
def on_vertical_scroll(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

def on_horizontal_scroll(event):
    canvas.xview_scroll(-1 * (event.delta // 120), "units")

if __name__ == '__main__':
    root = TkinterDnD.Tk()
    root.title('Plate Analyzer 1.0')

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size to match the screen size
    root.geometry(f"{int(screen_width*0.8)}x{int(screen_height*0.8)}")

    # Maximize the window
    root.state('zoomed')
    root.iconbitmap('logo.ico')

    # Create a Frame to hold the Canvas and both Scrollbars
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=True)

    # Create a Canvas widget
    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Add a vertical Scrollbar widget
    v_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    v_scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=v_scrollbar.set)

    # Add a horizontal Scrollbar widget
    h_scrollbar = Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
    h_scrollbar.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=h_scrollbar.set)

    # Configure the Canvas to work with the Scrollbars
    canvas.config(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

    # Create a Frame to hold all the other frames
    container = Frame(canvas)
    canvas.create_window((0, 0), window=container, anchor=NW)

    # Bind the frame configure event to update the scroll region
    container.bind("<Configure>", lambda event: on_frame_configure(canvas))

    # Bind mouse wheel events for scrolling
    canvas.bind_all("<MouseWheel>", on_vertical_scroll)
    canvas.bind_all("<Shift-MouseWheel>", on_horizontal_scroll)

    plate_info_frame = LabelFrame(container, text="Plate Info", width=550, height=280)
    plate_info_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nws')
    #plate_info_frame.grid_propagate(flag=False)

    job_info_frame = LabelFrame(container, text="Job Info", width=650, height=280)
    job_info_frame.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky='w')
    #job_info_frame.grid_propagate(flag=False)

    plot_frame = LabelFrame(container, text="Plot selection", width=400, height=600)
    plot_frame.grid(row=1, column=0, columnspan=2, rowspan=6, padx=10, pady=10, sticky='news')
    plot_frame.grid_propagate(flag=False)

    Button(container, text='New figure\n--->').grid(row=1, column=2, sticky='n', pady=20)
    Button(container, text='Delete').grid(row=1, column=2, pady=100, sticky='n')
    Button(container, text='Plot').grid(row=6, column=4, pady=10, sticky='n')

    entry_figure_name = Entry(container)
    entry_figure_name.grid(row=1, column=2, sticky='n', pady=80)

    figures_frame = LabelFrame(container, text='Figures', height=150, width=500)
    figures_frame.grid(row=1, column=3, sticky='nwe', padx=10, pady=10)
    figures_frame.grid_propagate(flag=False)
    figures_frame.grid_rowconfigure([0,1,2,3,4,5,6], minsize=21)
    figures_frame.grid_columnconfigure([0,1,2,3,4], minsize=100)


    radio_color_var = [IntVar() for i in range(5)]
    radio_var_figure = StringVar()
    entry_text_variable = StringVar()

    ax_setting_frame = LabelFrame(container, text='Plot settings', height=350, width=500)
    ax_setting_frame.grid(row=2, column=2, columnspan=2, rowspan=5, pady=20, padx=10, sticky='news')
    ax_setting_frame.grid_propagate(flag=False)
    ax_setting_frame.grid_rowconfigure(0, weight=1)
    ax_setting_frame.grid_columnconfigure(0, weight=1)


    LabelFrame(container, text='Template', height=150, width=200).grid(row=0, column=4, sticky='news', pady=10, padx=10)
    preview_frame = LabelFrame(container, text='Preview', height=375, width=500)
    preview_frame.grid(row=1, column=4, columnspan=2, rowspan=6, sticky='nw', padx=10, pady=10)
    preview_frame.grid_propagate(flag=False)

    # Create a Notebook widget
    notebook = ttk.Notebook(ax_setting_frame, height=ax_setting_frame.winfo_height()-48, width=ax_setting_frame.winfo_width()-8)
    notebook.grid(row=0, column=0, sticky='nsew')
    tab = Frame(notebook)
    notebook.add(tab, text='')

    root.mainloop()