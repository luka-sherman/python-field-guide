---
description: An overview of popular Python libraries covered on this site, both built-in and third-party.
---

# Libraries

Libraries allow us to apply the Python fundamentals to real tasks. These are a few popular ones, but there are many.

<div class="pt-category-grid pt-category-grid--stacked" markdown="block">

<div class="pt-category" markdown="block">
#### Built-in libraries { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](csv.md) [:material-language-python:](csv.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Reading and writing spreadsheets.

    [`install`](csv.md#install) · [`import`](csv.md#import) · [`csv.writer`](csv.md#writing-csv-files) · [`csv.reader`](csv.md#reading-csv-files) · [`DictReader`](csv.md#reading-rows-as-dictionaries)

-   :material-calendar-clock:{ .lg .middle } [__datetime__](datetime.md) [:material-language-python:](datetime.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Calculating and formatting dates and times.

    [`install`](datetime.md#install) · [`import`](datetime.md#import) · [`date`](datetime.md#creating-dates-and-times) · [`timedelta`](datetime.md#date-arithmetic) · [`strftime()`](datetime.md#formatting-with-strftime) · [`strptime()`](datetime.md#parsing-a-string-with-strptime)

-   :material-code-json:{ .lg .middle } [__json__](json.md) [:material-language-python:](json.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Reading and writing JSON data: nested dicts and lists, saved to a file or a string.

    [`install`](json.md#install) · [`import`](json.md#import) · [`json.dump()`](json.md#writing-json-files) · [`json.load()`](json.md#reading-json-files) · [`json.dumps()`](json.md#working-with-strings-instead-of-files) · [`json.loads()`](json.md#working-with-strings-instead-of-files)

-   :material-dice-multiple:{ .lg .middle } [__random__](random.md) [:material-language-python:](random.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Random numbers, random picks, shuffled order.

    [`install`](random.md#install) · [`import`](random.md#import) · [`randint()`](random.md#random-numbers) · [`choice()`](random.md#random-selections) · [`shuffle()`](random.md#shuffling-a-list) · [`sample()`](random.md#sampling-without-replacement)

-   :material-application-outline:{ .lg .middle } [__Tkinter__](tkinter.md) [:material-language-python:](tkinter.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    [`install`](tkinter.md#install) · [`import`](tkinter.md#import) · [`Tk()`](tkinter.md#creating-a-window) · [`Button`](tkinter.md#widgets) · [`pack()`](tkinter.md#layout-managers) · [`configure()`](tkinter.md#configuring-widgets) · [`command`](tkinter.md#handling-events) · [`ttk.Style`](tkinter.md#styling-with-ttk) · [`messagebox`](tkinter.md#dialogs) · [`winfo_width()`](tkinter.md#introspecting-widgets) · [`putting it together`](tkinter.md#putting-it-together)

</div>
</div>

<div class="pt-category" markdown="block">
#### Third-party libraries { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-chart-line:{ .lg .middle } [__matplotlib__](matplotlib.md) [:material-download-outline:](matplotlib.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Charts and plots: line, bar, and scatter, built directly from plain Python data.

    [`install`](matplotlib.md#install) · [`import`](matplotlib.md#import) · [`line plots`](matplotlib.md#line-plots) · [`bar charts`](matplotlib.md#bar-charts) · [`scatter plots`](matplotlib.md#scatter-plots) · [`subplots`](matplotlib.md#subplots) · [`saving a figure`](matplotlib.md#saving-a-figure)

-   :material-matrix:{ .lg .middle } [__NumPy__](numpy.md) [:material-download-outline:](numpy.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Fast numeric arrays, with math applied to a whole array at once instead of item by item.

    [`install`](numpy.md#install) · [`import`](numpy.md#import) · [`ndarray`](numpy.md#creating-arrays) · [`array operations`](numpy.md#array-operations) · [`arange()`](numpy.md#building-arrays-without-a-list) · [`mean()`](numpy.md#aggregating-an-array) · [`boolean mask`](numpy.md#filtering-with-a-boolean-mask)

-   :material-face-recognition:{ .lg .middle } [__OpenCV__](opencv.md) [:material-download-outline:](opencv.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Real-time image and video analysis, built directly on NumPy arrays: color spaces, edge detection, face detection.

    [`install`](opencv.md#install) · [`import`](opencv.md#import) · [`reading, displaying, saving images`](opencv.md#reading-displaying-and-saving-images) · [`drawing`](opencv.md#drawing-shapes-and-text) · [`color spaces`](opencv.md#color-spaces) · [`CascadeClassifier`](opencv.md#face-detection-with-cascade-classifiers) · [`VideoCapture()`](opencv.md#working-with-video) · [`basic operations`](opencv.md#basic-operations) · [`thresholding, edge detection`](opencv.md#thresholding-and-edge-detection) · [`blurring`](opencv.md#blurring) · [`contours`](opencv.md#contours) · [`imread()`](opencv.md#reading-a-file) · [`cvtColor()`](opencv.md#converting-color-spaces) · [`Canny()`](opencv.md#edge-detection) · [`resize()`](opencv.md#resize)

-   :material-table:{ .lg .middle } [__pandas__](pandas.md) [:material-download-outline:](pandas.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Tabular data: rows and columns, like a spreadsheet, built on top of NumPy.

    [`install`](pandas.md#install) · [`import`](pandas.md#import) · [`DataFrame`](pandas.md#building-a-dataframe) · [`working with a DataFrame`](pandas.md#working-with-a-dataframe) · [`sort_values()`](pandas.md#sorting-rows) · [`mean()`](pandas.md#summarizing-a-column)

-   :material-image-outline:{ .lg .middle } [__Pillow__](pillow.md) [:material-download-outline:](pillow.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Opening, editing, and saving images, built around one `Image` object.

    [`install`](pillow.md#install) · [`import`](pillow.md#import) · [`why Pillow?`](pillow.md#why-pillow) · [`Image`](pillow.md#the-image) · [`ImageOps`](pillow.md#imageops-module) · [`ImageDraw`](pillow.md#imagedraw-module) · [`ImageFont`](pillow.md#imagefont-module) · [`ImageColor`](pillow.md#imagecolor-module) · [`ImageFilter`](pillow.md#imagefilter-module) · [`ImageEnhance`](pillow.md#imageenhance-module) · [`ImageChops`](pillow.md#imagechops-module) · [`convert()`](pillow.md#format-conversion) · [`ImageSequence`](pillow.md#imagesequence-module) · [`putting it together`](pillow.md#putting-it-together)

-   :material-api:{ .lg .middle } [__requests__](requests.md) [:material-download-outline:](requests.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Fetching data over the internet, like asking a website or API for information.

    [`install`](requests.md#install) · [`import`](requests.md#import) · [`get()`](requests.md#making-a-request) · [`error handling`](requests.md#handling-request-errors) · [`status_code`](requests.md#checking-the-status-code) · [`json()`](requests.md#parsing-json) · [`params`](requests.md#query-parameters)

</div>
</div>

</div>
