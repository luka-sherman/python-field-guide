# Libraries

Once the language fundamentals feel comfortable, libraries put them to use on real tasks — some ship with Python and need no install, others are third-party packages installed separately with `pip`.

**Standard Library** — ships with Python, no install required:

<div class="grid cards" markdown="block">

- **[datetime](datetime.md)**

    Python's built-in toolkit for dates and times — logging when something happened, and measuring how long ago.

    [`date`](datetime.md#creating-dates-and-times) · [`strftime()`](datetime.md#formatting-with-strftime) · [`timedelta`](datetime.md#date-arithmetic) · [`strptime()`](datetime.md#parsing-a-string-with-strptime)

- **[random](random.md)**

    Python's built-in toolkit for randomness — random numbers, random picks, shuffled order.

    [`randint()`](random.md#random-numbers) · [`choice()`](random.md#random-selections) · [`shuffle()`](random.md#shuffling-a-list) · [`sample()`](random.md#sampling-without-replacement)

- **[csv](csv.md)**

    Python's built-in toolkit for reading and writing CSV files — the plain-text table format spreadsheets open too.

    [`csv.writer`](csv.md#writing-csv-files) · [`csv.reader`](csv.md#reading-csv-files) · [`DictReader`](csv.md#reading-rows-as-dictionaries)

- **[Tkinter](tkinter.md)**

    Python's built-in toolkit for desktop applications: windows, widgets, and events — no extra install needed to give a program a real interface.

    [`Tk()`](tkinter.md#creating-a-window) · [`Button`](tkinter.md#widgets) · [`pack()`](tkinter.md#layout-managers) · [`configure()`](tkinter.md#configuring-widgets) · [`command`](tkinter.md#handling-events) · [`ttk.Style`](tkinter.md#styling-with-ttk) · [`messagebox`](tkinter.md#dialogs) · [`winfo_width()`](tkinter.md#introspecting-widgets)

</div>

**Third-Party** — installed separately with `pip`:

<div class="grid cards" markdown="block">

- **[NumPy](numpy.md)**

    A third-party toolkit for fast numeric arrays — math applied to a whole array at once, instead of item by item.

    [`ndarray`](numpy.md#creating-arrays) · [`arange()`](numpy.md#building-arrays-without-a-list) · [`mean()`](numpy.md#aggregating-an-array) · [boolean mask](numpy.md#filtering-with-a-boolean-mask)

- **[pandas](pandas.md)**

    A third-party toolkit for tabular data — rows and columns, like a spreadsheet, built on top of NumPy.

    [`DataFrame`](pandas.md#building-a-dataframe) · [`sort_values()`](pandas.md#sorting-rows) · [`mean()`](pandas.md#summarizing-a-column)

- **[Pillow](pillow.md)**

    A third-party toolkit for opening, editing, and saving images, built around one `Image` object — useful anytime a program needs to touch actual image files.

    [`Image`](pillow.md#the-image) · [`ImageOps`](pillow.md#imageops-module) · [`ImageDraw`](pillow.md#imagedraw-module) · [`ImageFont`](pillow.md#imagefont-module) · [`ImageColor`](pillow.md#imagecolor-module) · [`ImageFilter`](pillow.md#imagefilter-module) · [`ImageEnhance`](pillow.md#imageenhance-module) · [`ImageChops`](pillow.md#imagechops-module) · [`convert()`](pillow.md#format-conversion) · [`ImageSequence`](pillow.md#imagesequence-module)

</div>
