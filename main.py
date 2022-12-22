import tkinter as tk
from tkinter import ttk
import pandas as pd

BOOKS = "file_books.csv"
books_df = pd.read_csv(BOOKS)

GAMES = "file_games.csv"
games_df = pd.read_csv(GAMES)

MOVIES = "file_movies.csv"
movies_df = pd.read_csv(MOVIES)

def save_files():
    global books_df, movies_df, games_df
    books_df = books_df.drop_duplicates()
    games_df = games_df.drop_duplicates()
    movies_df = movies_df.drop_duplicates()

    books_df.to_csv(BOOKS, index = False)
    movies_df.to_csv(MOVIES, index = False)
    games_df.to_csv(GAMES, index = False)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("802x435")
        self.title("Collection Manager")
        self.resizable(False, False)

        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
        for F in (BooksFrame, GamesFrame, MoviesFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(BooksFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class BooksFrame(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.books_btn = tk.Button(self, text = "Books", height = 1, width = 10, command = lambda: controller.show_frame(BooksFrame))
        self.books_btn.grid(row = 0, column = 0)

        self.games_btn = tk.Button(self, text = "Games", height = 1, width = 10, command = lambda: controller.show_frame(GamesFrame))
        self.games_btn.grid(row = 0, column = 1)

        self.movies_btn = tk.Button(self, text = "Movies", height = 1, width = 10, command = lambda: controller.show_frame(MoviesFrame))
        self.movies_btn.grid(row = 0, column = 2)

        self.input_label = ttk.LabelFrame(self, text = "Input Fields - Books")
        self.input_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

        self.title = tk.StringVar()
        self.title_label = tk.Label(self.input_label, text = "Title")
        self.title_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
        self.title_entry = tk.Entry(self.input_label, textvariable = self.title)
        self.title_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.author = tk.StringVar()
        self.author_label = tk.Label(self.input_label, text = "Author")
        self.author_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        self.author_entry = tk.Entry(self.input_label, textvariable = self.author)
        self.author_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.genre = tk.StringVar()
        self.genre_label = tk.Label(self.input_label, text = "Genre")
        self.genre_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        self.genre_entry = tk.Entry(self.input_label, textvariable = self.genre)
        self.genre_entry.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.year = tk.StringVar()
        self.year_label = tk.Label(self.input_label, text = "Release year")
        self.year_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
        self.year_entry = tk.Entry(self.input_label, textvariable = self.year)
        self.year_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

        self.page_num = tk.StringVar()
        self.page_num_label = tk.Label(self.input_label, text = "Number of pages")
        self.page_num_label.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "w")
        self.page_num_entry = tk.Entry(self.input_label, textvariable = self.page_num)
        self.page_num_entry.grid(row = 4, column = 1, padx = 5, pady = 5)

        self.language = tk.StringVar()
        self.language_label = tk.Label(self.input_label, text = "Language")
        self.language_label.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "w")
        self.language_entry = tk.Entry(self.input_label, textvariable = self.language)
        self.language_entry.grid(row = 5, column = 1, padx = 5, pady = 5)

        self.create_btn = tk.Button(self, text = "Create", command = lambda: [self.append_to_dataframe(self.get_entry_data()), self.clear_inputs(), self.show_treeview(books_df)], height = 1, width = 25)
        self.create_btn.grid(row = 2, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.show_btn = tk.Button(self, text = "Show All", command = lambda: [self.show_treeview(books_df), self.clear_inputs()], height = 1, width = 25)
        self.show_btn.grid(row = 3, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.edit_btn = tk.Button(self, text = "Edit", command = lambda: [self.edit(self.selected_data, self.get_entry_data()), self.clear_inputs(), self.show_treeview(books_df)], height = 1, width = 25)
        self.edit_btn.grid(row = 4, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.delete_btn = tk.Button(self, text = "Delete", command = lambda: [self.delete(self.selected_data), self.clear_inputs(), self.show_treeview(books_df)], height = 1, width = 25)
        self.delete_btn.grid(row = 5, column = 0, columnspan = 3, padx = 5 , pady = 5)

        search = tk.StringVar()
        self.search_btn = tk.Button(self, text = "Search", height = 1, width = 10, command = lambda: self.search())
        self.search_btn.grid(row = 0, column = 4, padx = 0, pady = 5, sticky = "w")
        self.search_entry = tk.Entry(self, width = 72, textvariable = search)
        self.search_entry.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "e")

        self.treeview = ttk.Treeview(self, columns = ("1", "2", "3", "4", "5", "6"), show = "headings", height = 18)
        self.treeview.grid(row = 1, rowspan = 5, column = 3, columnspan = 2, padx = 0, pady = 0)

        self.treeview.column("1", anchor = "center", stretch = False, width = 152)
        self.treeview.heading("1", text = "Title")

        self.treeview.column("2", anchor = "center", stretch = False, width = 50)
        self.treeview.heading("2", text = "Author")

        self.treeview.column("3", anchor = "center", stretch = False, width = 50)
        self.treeview.heading("3", text = "Genre")

        self.treeview.column("4", anchor = "center", stretch = False, width = 100)
        self.treeview.heading("4", text = "Release year")

        self.treeview.column("5", anchor = "center", stretch = False, width = 102)
        self.treeview.heading("5", text = "Number of pages")

        self.treeview.column("6", anchor = "center", stretch = False, width = 75)
        self.treeview.heading("6", text = "Language")

        self.treeview.bind("<ButtonRelease-1>", self.selected)

        self.v_scrollbar = ttk.Scrollbar(self, orient = "vertical", command = self.treeview.yview)
        self.v_scrollbar.grid(row = 1, rowspan = 4, column = 5, sticky = "nsew")
        self.treeview.configure(yscrollcommand = self.v_scrollbar.set)

        self.h_scrollbar = ttk.Scrollbar(self, orient = "horizontal", command = self.treeview.xview)
        self.h_scrollbar.grid(row = 6, column = 3, columnspan = 2, sticky = "nsew")
        self.treeview.configure(xscrollcommand = self.h_scrollbar.set)

        self.show_treeview(books_df)

        self.selected_data = {}

    def selected(self, a):
        selected = self.treeview.focus()
        items = self.treeview.item(selected)

        self.title_entry.delete(0,tk.END)
        self.title_entry.insert(0,items["values"][0])

        self.author_entry.delete(0,tk.END)
        self.author_entry.insert(0,items["values"][1])

        self.genre_entry.delete(0,tk.END)
        self.genre_entry.insert(0,items["values"][2])

        self.year_entry.delete(0,tk.END)
        self.year_entry.insert(0,items["values"][3])

        self.page_num_entry.delete(0,tk.END)
        self.page_num_entry.insert(0,items["values"][4])

        self.language_entry.delete(0,tk.END)
        self.language_entry.insert(0,items["values"][5])
        
        self.selected_data = {"Title": items["values"][0], 
        "Author": items["values"][1], 
        "Genre": items["values"][2], 
        "Release_year": items["values"][3], 
        "Number_of_pages": items["values"][4], 
        "Language": items["values"][5]}

    def clear_inputs(self):
        self.title_entry.delete(0,tk.END)
        self.author_entry.delete(0,tk.END)
        self.genre_entry.delete(0,tk.END)
        self.year_entry.delete(0,tk.END)
        self.page_num_entry.delete(0,tk.END)
        self.language_entry.delete(0,tk.END)

    def show_treeview(self, dataframe):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for i in range(len(dataframe.index)):
            self.treeview.insert("","end", iid = None, values=(dataframe.iloc[i]["Title"],dataframe.iloc[i]["Author"],dataframe.iloc[i]["Genre"],dataframe.iloc[i]["Release_year"],dataframe.iloc[i]["Number_of_pages"],dataframe.iloc[i]["Language"]))

    def get_entry_data(self):
        return {"Title": self.title.get(), 
        "Author": self.author.get(), 
        "Genre": self.genre.get(), 
        "Release_year": self.year.get(), 
        "Number_of_pages": self.page_num.get(), 
        "Language": self.language.get()}

    def append_to_dataframe(self, row):
        global books_df
        books_df = books_df.append(row, ignore_index = True)
        save_files()
    
    def delete(self, row):
        global books_df
        books_df = books_df[(books_df.Title != row["Title"]) & 
            (books_df.Author != row["Author"]) & 
            (books_df.Genre != row["Genre"]) & 
            (books_df.Release_year != row["Release_year"]) & 
            (books_df.Number_of_pages != row["Number_of_pages"]) & 
            (books_df.Language != row["Language"])]
        save_files()

    def edit(self, previous, new):
        global books_df
        self.delete(previous)
        self.append_to_dataframe(new)

    def search(self):
        text = self.search_entry.get()
        temp_df = pd.DataFrame()
        temp_df = books_df[(books_df["Title"] == text) | (books_df["Author"] == text) | (books_df["Genre"] == text) | (books_df["Release_year"] == text) | (books_df["Number_of_pages"] == text) | (books_df["Language"] == text)]
        self.show_treeview(temp_df)
        self.search_entry.delete(0,tk.END)

class GamesFrame(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.books_btn = tk.Button(self, text = "Books", height = 1, width = 10, command = lambda: controller.show_frame(BooksFrame))
        self.books_btn.grid(row = 0, column = 0)

        self.games_btn = tk.Button(self, text = "Games", height = 1, width = 10, command = lambda: controller.show_frame(GamesFrame))
        self.games_btn.grid(row = 0, column = 1)

        self.movies_btn = tk.Button(self, text = "Movies", height = 1, width = 10, command = lambda: controller.show_frame(MoviesFrame))
        self.movies_btn.grid(row = 0, column = 2)

        self.input_label = ttk.LabelFrame(self, text = "Input Fields - Games")
        self.input_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

        self.title = tk.StringVar()
        self.title_label = tk.Label(self.input_label, text = "Title")
        self.title_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
        self.title_entry = tk.Entry(self.input_label, textvariable = self.title)
        self.title_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.prd_std = tk.StringVar()
        self.prd_std_label = tk.Label(self.input_label, text = "Production Studio")
        self.prd_std_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        self.prd_std_entry = tk.Entry(self.input_label, textvariable = self.prd_std)
        self.prd_std_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.genre = tk.StringVar()
        self.genre_label = tk.Label(self.input_label, text = "Genre")
        self.genre_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        self.genre_entry = tk.Entry(self.input_label, textvariable = self.genre)
        self.genre_entry.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.year = tk.StringVar()
        self.year_label = tk.Label(self.input_label, text = "Release year")
        self.year_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
        self.year_entry = tk.Entry(self.input_label, textvariable = self.year)
        self.year_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

        self.platform = tk.StringVar()
        self.platform_label = tk.Label(self.input_label, text = "Platform")
        self.platform_label.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "w")
        self.platform_entry = tk.Entry(self.input_label, textvariable = self.platform)
        self.platform_entry.grid(row = 4, column = 1, padx = 5, pady = 5)


        self.create_btn = tk.Button(self, text = "Create", command = lambda: [self.append_to_dataframe(self.get_entry_data()), self.clear_inputs(), self.show_treeview(games_df)], height = 1, width = 25)
        self.create_btn.grid(row = 2, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.show_btn = tk.Button(self, text = "Show All", command = lambda: [self.show_treeview(games_df), self.clear_inputs()], height = 1, width = 25)
        self.show_btn.grid(row = 3, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.edit_btn = tk.Button(self, text = "Edit", command = lambda: [self.edit(self.selected_data, self.get_entry_data()), self.clear_inputs(), self.show_treeview(games_df)], height = 1, width = 25)
        self.edit_btn.grid(row = 4, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.delete_btn = tk.Button(self, text = "Delete", command = lambda: [self.delete(self.selected_data), self.clear_inputs(), self.show_treeview(games_df)], height = 1, width = 25)
        self.delete_btn.grid(row = 5, column = 0, columnspan = 3, padx = 5 , pady = 5)

        search = tk.StringVar()
        self.search_btn = tk.Button(self, text = "Search", height = 1, width = 10, command = lambda: self.search())
        self.search_btn.grid(row = 0, column = 4, padx = 0, pady = 5, sticky = "w")
        self.search_entry = tk.Entry(self, width = 72, textvariable = search)
        self.search_entry.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "e")

        self.treeview = ttk.Treeview(self, columns = ("1", "2", "3", "4", "5"), show = "headings", height = 18)
        self.treeview.grid(row = 1, rowspan = 5, column = 3, columnspan = 2, padx = 0, pady = 0)

        self.treeview.column("1", anchor = "center", stretch = False, width = 150)
        self.treeview.heading("1", text = "Title")

        self.treeview.column("2", anchor = "center", stretch = False, width = 125)
        self.treeview.heading("2", text = "Production studio")

        self.treeview.column("3", anchor = "center", stretch = False, width = 50)
        self.treeview.heading("3", text = "Genre")

        self.treeview.column("4", anchor = "center", stretch = False, width = 100)
        self.treeview.heading("4", text = "Release year")

        self.treeview.column("5", anchor = "center", stretch = False, width = 100)
        self.treeview.heading("5", text = "Platform")


        self.treeview.bind("<ButtonRelease-1>", self.selected)

        self.v_scrollbar = ttk.Scrollbar(self, orient = "vertical", command = self.treeview.yview)
        self.v_scrollbar.grid(row = 1, rowspan = 4, column = 5, sticky = "nsew")
        self.treeview.configure(yscrollcommand = self.v_scrollbar.set)

        self.h_scrollbar = ttk.Scrollbar(self, orient = "horizontal", command = self.treeview.xview)
        self.h_scrollbar.grid(row = 6, column = 3, columnspan = 2, sticky = "nsew")
        self.treeview.configure(xscrollcommand = self.h_scrollbar.set)

        self.show_treeview(games_df)

        self.selected_data = {}

    def selected(self, a):
        selected = self.treeview.focus()
        items = self.treeview.item(selected)
        print(items)
        self.title_entry.delete(0,tk.END)
        self.title_entry.insert(0,items["values"][0])

        self.prd_std_entry.delete(0,tk.END)
        self.prd_std_entry.insert(0,items["values"][1])

        self.genre_entry.delete(0,tk.END)
        self.genre_entry.insert(0,items["values"][2])

        self.year_entry.delete(0,tk.END)
        self.year_entry.insert(0,items["values"][3])

        self.platform_entry.delete(0,tk.END)
        self.platform_entry.insert(0,items["values"][4])
        
        self.selected_data = {"Title": items["values"][0], 
        "Production_studio": items["values"][1], 
        "Genre": items["values"][2], 
        "Release_year": items["values"][3], 
        "Platform": items["values"][4]}

    def clear_inputs(self):
        self.title_entry.delete(0,tk.END)
        self.prd_std_entry.delete(0,tk.END)
        self.genre_entry.delete(0,tk.END)
        self.year_entry.delete(0,tk.END)
        self.platform_entry.delete(0,tk.END)

    def show_treeview(self, dataframe):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for i in range(len(dataframe.index)):
            self.treeview.insert("","end", iid = None, values=(dataframe.iloc[i]["Title"],dataframe.iloc[i]["Production_studio"],dataframe.iloc[i]["Genre"],dataframe.iloc[i]["Release_year"],dataframe.iloc[i]["Platform"]))

    def get_entry_data(self):
        return {"Title": self.title.get(), 
        "Production_studio": self.prd_std.get(), 
        "Genre": self.genre.get(), 
        "Release_year": self.year.get(), 
        "Platform": self.platform.get()}

    def append_to_dataframe(self, row):
        global games_df
        games_df = games_df.append(row, ignore_index = True)
        save_files()
    
    def delete(self, row):
        global games_df
        games_df = games_df[(games_df.Title != row["Title"]) & (games_df.Production_studio != row["Production_studio"]) & (games_df.Genre != row["Genre"]) & (games_df.Release_year != row["Release_year"]) & (games_df.Platform != row["Platform"])]
        save_files()

    def edit(self, previous, new):
        global games_df
        self.delete(previous)
        self.append_to_dataframe(new)

    def search(self):
        text = self.search_entry.get()
        temp_df = pd.DataFrame()
        temp_df = games_df[(games_df["Title"] == text) | (games_df["Production_studio"] == text) | (games_df["Genre"] == text) | (games_df["Release_year"] == text) | (games_df["Platform"] == text)]
        self.show_treeview(temp_df)
        self.search_entry.delete(0,tk.END)

class MoviesFrame(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.books_btn = tk.Button(self, text = "Books", height = 1, width = 10, command = lambda: controller.show_frame(BooksFrame))
        self.books_btn.grid(row = 0, column = 0)

        self.games_btn = tk.Button(self, text = "Games", height = 1, width = 10, command = lambda: controller.show_frame(GamesFrame))
        self.games_btn.grid(row = 0, column = 1)

        self.movies_btn = tk.Button(self, text = "Movies", height = 1, width = 10, command = lambda: controller.show_frame(MoviesFrame))
        self.movies_btn.grid(row = 0, column = 2)

        self.input_label = ttk.LabelFrame(self, text = "Input Fields - Books")
        self.input_label.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)

        self.title = tk.StringVar()
        self.title_label = tk.Label(self.input_label, text = "Title")
        self.title_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
        self.title_entry = tk.Entry(self.input_label, textvariable = self.title)
        self.title_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.director = tk.StringVar()
        self.director_label = tk.Label(self.input_label, text = "Directed by")
        self.director_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        self.director_entry = tk.Entry(self.input_label, textvariable = self.director)
        self.director_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.genre = tk.StringVar()
        self.genre_label = tk.Label(self.input_label, text = "Genre")
        self.genre_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        self.genre_entry = tk.Entry(self.input_label, textvariable = self.genre)
        self.genre_entry.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.year = tk.StringVar()
        self.year_label = tk.Label(self.input_label, text = "Release year")
        self.year_label.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "w")
        self.year_entry = tk.Entry(self.input_label, textvariable = self.year)
        self.year_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

        self.runtime = tk.StringVar()
        self.runtime_label = tk.Label(self.input_label, text = "Runtime")
        self.runtime_label.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "w")
        self.runtime_entry = tk.Entry(self.input_label, textvariable = self.runtime)
        self.runtime_entry.grid(row = 4, column = 1, padx = 5, pady = 5)

        self.awards = tk.StringVar()
        self.awards_label = tk.Label(self.input_label, text = "Number of awards")
        self.awards_label.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "w")
        self.awards_entry = tk.Entry(self.input_label, textvariable = self.awards)
        self.awards_entry.grid(row = 5, column = 1, padx = 5, pady = 5)

        self.create_btn = tk.Button(self, text = "Create", command = lambda: [self.append_to_dataframe(self.get_entry_data()), self.clear_inputs(), self.show_treeview(movies_df)], height = 1, width = 25)
        self.create_btn.grid(row = 2, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.show_btn = tk.Button(self, text = "Show All", command = lambda: [self.show_treeview(movies_df), self.clear_inputs()], height = 1, width = 25)
        self.show_btn.grid(row = 3, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.edit_btn = tk.Button(self, text = "Edit", command = lambda: [self.edit(self.selected_data, self.get_entry_data()), self.clear_inputs(), self.show_treeview(movies_df)], height = 1, width = 25)
        self.edit_btn.grid(row = 4, column = 0, columnspan = 3, padx = 5 , pady = 5)
        self.delete_btn = tk.Button(self, text = "Delete", command = lambda: [self.delete(self.selected_data), self.clear_inputs(), self.show_treeview(movies_df)], height = 1, width = 25)
        self.delete_btn.grid(row = 5, column = 0, columnspan = 3, padx = 5 , pady = 5)

        search = tk.StringVar()
        self.search_btn = tk.Button(self, text = "Search", height = 1, width = 10, command = lambda: self.search())
        self.search_btn.grid(row = 0, column = 4, padx = 0, pady = 5, sticky = "w")
        self.search_entry = tk.Entry(self, width = 72, textvariable = search)
        self.search_entry.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "e")

        self.treeview = ttk.Treeview(self, columns = ("1", "2", "3", "4", "5", "6"), show = "headings", height = 18)
        self.treeview.grid(row = 1, rowspan = 5, column = 3, columnspan = 2, padx = 0, pady = 0)

        self.treeview.column("1", anchor = "center", stretch = False, width = 148)
        self.treeview.heading("1", text = "Title")

        self.treeview.column("2", anchor = "center", stretch = False, width = 75)
        self.treeview.heading("2", text = "Directed by")

        self.treeview.column("3", anchor = "center", stretch = False, width = 45)
        self.treeview.heading("3", text = "Genre")

        self.treeview.column("4", anchor = "center", stretch = False, width = 90)
        self.treeview.heading("4", text = "Release year")

        self.treeview.column("5", anchor = "center", stretch = False, width = 65)
        self.treeview.heading("5", text = "Runtime")

        self.treeview.column("6", anchor = "center", stretch = False, width = 100)
        self.treeview.heading("6", text = "Number of awards")

        self.treeview.bind("<ButtonRelease-1>", self.selected)

        self.v_scrollbar = ttk.Scrollbar(self, orient = "vertical", command = self.treeview.yview)
        self.v_scrollbar.grid(row = 1, rowspan = 4, column = 5, sticky = "nsew")
        self.treeview.configure(yscrollcommand = self.v_scrollbar.set)

        self.h_scrollbar = ttk.Scrollbar(self, orient = "horizontal", command = self.treeview.xview)
        self.h_scrollbar.grid(row = 6, column = 3, columnspan = 2, sticky = "nsew")
        self.treeview.configure(xscrollcommand = self.h_scrollbar.set)

        self.show_treeview(movies_df)

        self.selected_data = {}

    def selected(self, a):
        selected = self.treeview.focus()
        items = self.treeview.item(selected)

        self.title_entry.delete(0,tk.END)
        self.title_entry.insert(0,items["values"][0])

        self.director_entry.delete(0,tk.END)
        self.director_entry.insert(0,items["values"][1])

        self.genre_entry.delete(0,tk.END)
        self.genre_entry.insert(0,items["values"][2])

        self.year_entry.delete(0,tk.END)
        self.year_entry.insert(0,items["values"][3])

        self.runtime_entry.delete(0,tk.END)
        self.runtime_entry.insert(0,items["values"][4])

        self.awards_entry.delete(0,tk.END)
        self.awards_entry.insert(0,items["values"][5])
        
        self.selected_data = {"Title": items["values"][0], 
        "Directed_by": items["values"][1], 
        "Genre": items["values"][2], 
        "Release_year": items["values"][3], 
        "Runtime": items["values"][4], 
        "Number_of_awards": items["values"][5]}

    def clear_inputs(self):
        self.title_entry.delete(0,tk.END)
        self.director_entry.delete(0,tk.END)
        self.genre_entry.delete(0,tk.END)
        self.year_entry.delete(0,tk.END)
        self.runtime_entry.delete(0,tk.END)
        self.awards_entry.delete(0,tk.END)

    def show_treeview(self, dataframe):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for i in range(len(dataframe.index)):
            self.treeview.insert("","end", iid = None, values=(dataframe.iloc[i]["Title"],dataframe.iloc[i]["Directed_by"],dataframe.iloc[i]["Genre"],dataframe.iloc[i]["Release_year"],dataframe.iloc[i]["Runtime"],dataframe.iloc[i]["Number_of_awards"]))
    def get_entry_data(self):
        return {"Title": self.title.get(), 
        "Directed_by": self.director.get(), 
        "Genre": self.genre.get(), 
        "Release_year": self.year.get(), 
        "Runtime": self.runtime.get(), 
        "Number_of_awards": self.awards.get()}

    def append_to_dataframe(self, row):
        global movies_df
        movies_df = movies_df.append(row, ignore_index = True)
        save_files()
    
    def delete(self, row):
        global movies_df
        movies_df = movies_df[(movies_df.Title != row["Title"]) & 
            (movies_df.Directed_by != row["Directed_by"]) & 
            (movies_df.Genre != row["Genre"]) & 
            (movies_df.Release_year != row["Release_year"]) & 
            (movies_df.Runtime != row["Runtime"]) & 
            (movies_df.Number_of_awards != row["Number_of_awards"])]
        save_files()

    def edit(self, previous, new):
        global movies_df
        self.delete(previous)
        self.append_to_dataframe(new)

    def search(self):
        text = self.search_entry.get()
        temp_df = pd.DataFrame()
        temp_df = movies_df[(movies_df["Title"] == text) | (movies_df["Directed_by"] == text) | (movies_df["Genre"] == text) | (movies_df["Release_year"] == text) | (movies_df["Runtime"] == text) | (movies_df["Number_of_awards"] == text)]
        self.show_treeview(temp_df)
        self.search_entry.delete(0,tk.END)

app = App()
app.mainloop()