---
description: An overview of popular Python libraries covered on this site, both built-in and third-party.
hide:
  - navigation
  - toc
---

# Libraries

Libraries allow us to apply Python to real tasks. These are a few popular ones, but there are many.

<div class="pt-category-grid" markdown="block">

<div class="pt-category pt-category--wide" markdown="block">
#### Utilities { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-format-list-group:{ .lg .middle } [__collections__](collections.md) [:material-language-python:](collections.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Specialized containers: counting items, grouping with defaults, named tuples, fast queues.

    [**`Counter`**](collections.md#counter) [`counts[item]`](collections.md#count) [`most_common()`](collections.md#count) [`total()`](collections.md#count) [`elements()`](collections.md#inspect) [`update()`](collections.md#update) [`subtract()`](collections.md#update) [`+ - & |`](collections.md#combine)

    [**`defaultdict`**](collections.md#defaultdict) [`default_factory`](collections.md#defaultdict) [`.get()`](collections.md#reading-vs-writing)

    [**`namedtuple`**](collections.md#namedtuple) [`defaults=`](collections.md#create) [`_make()`](collections.md#create) [`_asdict()`](collections.md#convert) [`_replace()`](collections.md#convert) [`_fields`](collections.md#inspect_1) [`_field_defaults`](collections.md#inspect_1)

    [**`deque`**](collections.md#deque) [`append()`](collections.md#add) [`appendleft()`](collections.md#add) [`extend()`](collections.md#add) [`extendleft()`](collections.md#add) [`insert()`](collections.md#add) [`pop()`](collections.md#remove) [`popleft()`](collections.md#remove) [`remove()`](collections.md#remove) [`clear()`](collections.md#remove) [`count()`](collections.md#inspect_2) [`index()`](collections.md#inspect_2) [`copy()`](collections.md#inspect_2) [`rotate()`](collections.md#reorder) [`reverse()`](collections.md#reorder) [`maxlen=`](collections.md#reorder)

    [**`OrderedDict`**](collections.md#ordereddict) [`move_to_end()`](collections.md#reorder_1) [`popitem()`](collections.md#reorder_1) [`==`](collections.md#compare)

    [**`ChainMap`**](collections.md#chainmap) [`new_child()`](collections.md#extend) [`.maps`](collections.md#inspect_3) [`.parents`](collections.md#inspect_3)

    [**`User* wrapper`**](collections.md#user-wrapper-classes) [`UserDict`](collections.md#user-wrapper-classes) [`UserList`](collections.md#user-wrapper-classes) [`UserString`](collections.md#user-wrapper-classes)

-   :material-calendar-clock:{ .lg .middle } [__datetime__](datetime.md) [:material-language-python:](datetime.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Calculating and formatting dates and times.

    [`date`](datetime.md#creating-dates-and-times) [`strftime()`](datetime.md#formatting-with-strftime) [`creating a specific date`](datetime.md#creating-a-specific-date)

    [`timedelta`](datetime.md#date-arithmetic) [`strptime()`](datetime.md#parsing-a-string-with-strptime) [`difference between two dates`](datetime.md#difference-between-two-dates)

-   :material-dice-multiple:{ .lg .middle } [__random__](random.md) [:material-language-python:](random.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Random numbers, random picks, shuffled order.

    [**`randint()`**](random.md#random-numbers)

    [**`choice()`**](random.md#random-selections) [`shuffle()`](random.md#shuffling-a-list) [`sample()`](random.md#sampling-without-replacement)

</div>
</div>

<div class="pt-category pt-category--wide" markdown="block">
#### Data analysis { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](csv.md) [:material-language-python:](csv.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Reading and writing spreadsheets.

    [`csv.writer`](csv.md#writing-csv-files)

    [`csv.reader`](csv.md#reading-csv-files) [`DictReader`](csv.md#reading-rows-as-dictionaries)

-   :material-chart-line:{ .lg .middle } [__matplotlib__](matplotlib.md) [:material-download-outline:](matplotlib.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Charts and plots: line, bar, and scatter, built directly from plain Python data.

    [**`line plots`**](matplotlib.md#line-plots) [`labels and title`](matplotlib.md#labels-and-title) [`multiple lines and a legend`](matplotlib.md#multiple-lines-and-a-legend)

    [**`bar charts`**](matplotlib.md#bar-charts)

    [**`scatter plots`**](matplotlib.md#scatter-plots)

    [**`subplots`**](matplotlib.md#subplots)

    [**`saving a figure`**](matplotlib.md#saving-a-figure)

-   :material-matrix:{ .lg .middle } [__NumPy__](numpy.md) [:material-download-outline:](numpy.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Fast numeric arrays, with math applied to a whole array at once instead of item by item.

    [**`array operations`**](numpy.md#array-operations) [`mean()`](numpy.md#aggregating-an-array) [`boolean mask`](numpy.md#filtering-with-a-boolean-mask)

    [`ndarray`](numpy.md#creating-arrays) [`arange()`](numpy.md#building-arrays-without-a-list)

-   :material-table:{ .lg .middle } [__pandas__](pandas.md) [:material-download-outline:](pandas.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Tabular data: rows and columns, like a spreadsheet, built on top of NumPy.

    [**`DataFrame`**](pandas.md#building-a-dataframe)

    [**`working with a DataFrame`**](pandas.md#working-with-a-dataframe) [`sort_values()`](pandas.md#sorting-rows) [`mean()`](pandas.md#summarizing-a-column)

</div>
</div>

<div class="pt-category pt-category--wide" markdown="block">
#### APIs { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-code-json:{ .lg .middle } [__json__](json.md) [:material-language-python:](json.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Reading and writing JSON data: nested dicts and lists, saved to a file or a string.

    [`json.dump()`](json.md#writing-json-files)

    [`json.load()`](json.md#reading-json-files) [`nested data`](json.md#nested-data)

    [`json.loads()`](json.md#working-with-strings-instead-of-files)

-   :material-webhook:{ .lg .middle } [__requests__](requests.md) [:material-download-outline:](requests.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Fetching data over the internet, like asking a website or API for information.

    [**`get()`**](requests.md#making-a-request) [`status_code`](requests.md#checking-the-status-code) [`json()`](requests.md#parsing-json) [`params`](requests.md#query-parameters)

    [**`error handling`**](requests.md#handling-request-errors)

</div>
</div>

<div class="pt-category pt-category--wide" markdown="block">
#### Image editing { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-image-outline:{ .lg .middle } [__Pillow__](pillow.md) [:material-download-outline:](pillow.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Opening, editing, and saving images, built around one `Image` object.

    [**`why Pillow?`**](pillow.md#why-pillow)

    [**`Image`**](pillow.md#the-image) [`opening and saving images`](pillow.md#opening-and-saving-images) [`basic operations`](pillow.md#basic-operations) [`image modes`](pillow.md#image-modes) [`resize`](pillow.md#resize) [`crop`](pillow.md#crop) [`rotate and flip`](pillow.md#rotate-and-flip)

    [**`ImageOps`**](pillow.md#imageops-module) [`common ImageOps functions`](pillow.md#common-imageops-functions)

    [**`ImageDraw`**](pillow.md#imagedraw-module) [`shapes and lines`](pillow.md#shapes-and-lines)

    [**`ImageFont`**](pillow.md#imagefont-module) [`loading a font`](pillow.md#loading-a-font)

    [**`ImageColor`**](pillow.md#imagecolor-module) [`converting color names`](pillow.md#converting-color-names)

    [**`ImageFilter`**](pillow.md#imagefilter-module) [`applying a filter`](pillow.md#applying-a-filter)

    [**`ImageEnhance`**](pillow.md#imageenhance-module) [`enhancing an image`](pillow.md#enhancing-an-image)

    [**`ImageChops`**](pillow.md#imagechops-module) [`comparing and combining images`](pillow.md#comparing-and-combining-images)

    [**`convert()`**](pillow.md#format-conversion) [`converting between formats`](pillow.md#converting-between-formats)

    [**`ImageSequence`**](pillow.md#imagesequence-module) [`looping over GIF frames`](pillow.md#looping-over-gif-frames)

    [**`putting it together`**](pillow.md#putting-it-together) [`an interactive filter tool`](pillow.md#an-interactive-filter-tool)

</div>
</div>

<div class="pt-category pt-category--wide" markdown="block">
#### Computer vision { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-face-recognition:{ .lg .middle } [__OpenCV__](opencv.md) [:material-download-outline:](opencv.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" }

    Real-time image and video analysis, built directly on NumPy arrays: color spaces, edge detection, face detection.

    [**`reading, displaying, saving images`**](opencv.md#reading-displaying-and-saving-images) [`imread()`](opencv.md#reading-a-file) [`displaying a window`](opencv.md#displaying-a-window) [`saving a file`](opencv.md#saving-a-file)

    [**`drawing`**](opencv.md#drawing-shapes-and-text) [`shapes and lines`](opencv.md#shapes-and-lines) [`text`](opencv.md#text)

    [**`color spaces`**](opencv.md#color-spaces) [`cvtColor()`](opencv.md#converting-color-spaces)

    [**`CascadeClassifier`**](opencv.md#face-detection-with-cascade-classifiers) [`detecting and labeling faces`](opencv.md#detecting-and-labeling-faces)

    [**`VideoCapture()`**](opencv.md#working-with-video) [`reading frames`](opencv.md#reading-frames)

    [**`basic operations`**](opencv.md#basic-operations) [`resize()`](opencv.md#resize) [`cropping`](opencv.md#cropping) [`rotating`](opencv.md#rotating)

    [**`thresholding, edge detection`**](opencv.md#thresholding-and-edge-detection) [`Canny()`](opencv.md#edge-detection) [`threshold`](opencv.md#threshold)

    [**`blurring`**](opencv.md#blurring) [`gaussian blur`](opencv.md#gaussian-blur)

    [**`contours`**](opencv.md#contours) [`finding and drawing contours`](opencv.md#finding-and-drawing-contours)

</div>
</div>

<div class="pt-category pt-category--wide" markdown="block">
#### Desktop UIs { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-application-outline:{ .lg .middle } [__Tkinter__](tkinter.md) [:material-language-python:](tkinter.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" }

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    [**`Tk()`**](tkinter.md#creating-a-window)

    [**`Button`**](tkinter.md#widgets) [`Label`](tkinter.md#label) [`Button`](tkinter.md#button) [`Entry`](tkinter.md#entry)

    [**`pack()`**](tkinter.md#layout-managers) [`pack`](tkinter.md#pack) [`grid`](tkinter.md#grid)

    [**`configure()`**](tkinter.md#configuring-widgets) [`reading and changing options`](tkinter.md#reading-and-changing-options)

    [**`command`**](tkinter.md#handling-events) [`command callbacks`](tkinter.md#command-callbacks) [`binding events`](tkinter.md#binding-events)

    [**`ttk.Style`**](tkinter.md#styling-with-ttk) [`customizing a style`](tkinter.md#customizing-a-style)

    [**`messagebox`**](tkinter.md#dialogs) [`message boxes`](tkinter.md#message-boxes) [`file dialogs`](tkinter.md#file-dialogs)

    [**`winfo_width()`**](tkinter.md#introspecting-widgets) [`winfo methods`](tkinter.md#winfo-methods)

    [**`putting it together`**](tkinter.md#putting-it-together) [`a simple form`](tkinter.md#a-simple-form)

</div>
</div>

</div>
