# Libraries

Libraries allow us to apply the Python fundamentals to real tasks. These are a few popular ones, but there are many. 

They each need to be `import`ed at the top of the file.

## Built-in libraries

Python is already preloaded with these, and puts the above fundamentals to use on real tasks.

<div class="grid cards" markdown="block">

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](csv.md)

    Reading and writing spreadsheets.

    ---

    [`csv.writer`](csv.md#writing-csv-files) · [`csv.reader`](csv.md#reading-csv-files) · [`DictReader`](csv.md#reading-rows-as-dictionaries)


-   :material-calendar-clock:{ .lg .middle } [__datetime__](datetime.md)

    Calculating and formatting dates and times.

    ---

    [`date`](datetime.md#creating-dates-and-times) · [`strftime()`](datetime.md#formatting-with-strftime) · [`timedelta`](datetime.md#date-arithmetic) · [`strptime()`](datetime.md#parsing-a-string-with-strptime)

-   :material-dice-multiple:{ .lg .middle } [__random__](random.md)

    Random numbers, random picks, shuffled order.

    ---

    [`randint()`](random.md#random-numbers) · [`choice()`](random.md#random-selections) · [`shuffle()`](random.md#shuffling-a-list) · [`sample()`](random.md#sampling-without-replacement)

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](csv.md)

    Reading and writing spreadsheets.

    ---

    [`csv.writer`](csv.md#writing-csv-files) · [`csv.reader`](csv.md#reading-csv-files) · [`DictReader`](csv.md#reading-rows-as-dictionaries)

-   :material-application-outline:{ .lg .middle } [__Tkinter__](tkinter.md)

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    ---

    [`Tk()`](tkinter.md#creating-a-window) · [`Button`](tkinter.md#widgets) · [`pack()`](tkinter.md#layout-managers) · [`configure()`](tkinter.md#configuring-widgets) · [`command`](tkinter.md#handling-events) · [`ttk.Style`](tkinter.md#styling-with-ttk) · [`messagebox`](tkinter.md#dialogs) · [`winfo_width()`](tkinter.md#introspecting-widgets)

</div>

## Third-party libraries

These additional Python libraries can be installed on your computer for free with `pip`.

<div class="grid cards" markdown="block">

-   :material-matrix:{ .lg .middle } [__NumPy__](numpy.md)

    Fast numeric arrays — math applied to a whole array at once, instead of item by item.

    ---

    [`ndarray`](numpy.md#creating-arrays) · [`arange()`](numpy.md#building-arrays-without-a-list) · [`mean()`](numpy.md#aggregating-an-array) · [`boolean mask`](numpy.md#filtering-with-a-boolean-mask)

-   :material-table:{ .lg .middle } [__pandas__](pandas.md)

    Tabular data — rows and columns, like a spreadsheet, built on top of NumPy.

    ---

    [`DataFrame`](pandas.md#building-a-dataframe) · [`sort_values()`](pandas.md#sorting-rows) · [`mean()`](pandas.md#summarizing-a-column)

-   :material-image-outline:{ .lg .middle } [__Pillow__](pillow.md)

    Opening, editing, and saving images, built around one `Image` object.

    ---

    [`Image`](pillow.md#the-image) · [`ImageOps`](pillow.md#imageops-module) · [`ImageDraw`](pillow.md#imagedraw-module) · [`ImageFont`](pillow.md#imagefont-module) · [`ImageColor`](pillow.md#imagecolor-module) · [`ImageFilter`](pillow.md#imagefilter-module) · [`ImageEnhance`](pillow.md#imageenhance-module) · [`ImageChops`](pillow.md#imagechops-module) · [`convert()`](pillow.md#format-conversion) · [`ImageSequence`](pillow.md#imagesequence-module)

-   :material-api:{ .lg .middle } [__requests__](requests.md)

    Fetching data over the internet, like asking a website or API for information.

    ---

    [`get()`](requests.md#making-a-request) · [`status_code`](requests.md#checking-the-status-code) · [`json()`](requests.md#parsing-json) · [`params`](requests.md#query-parameters) · [`error handling`](requests.md#handling-request-errors)

</div>
