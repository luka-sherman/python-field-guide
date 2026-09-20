---
title: Libraries
description: An overview of popular Python libraries covered on this site, both built-in and third-party.
hide:
  - navigation
  - toc
---

# Libraries

Libraries allow us to apply Python to real tasks. These are a few popular ones, but there are many.

<div class="pt-category-grid" markdown="block">

<div class="pt-category pt-category--wide pt-lib--5" markdown="block">
#### Utilities { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-format-list-group:{ .lg .middle } [__collections__](collections.md) 
[:material-language-python:](collections.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 
    {: data-advanced="card" }

    Specialized containers: counting items, grouping with defaults, named tuples, fast queues.

    [**`Counter`**](collections.md#counter): 
    [`+ - & |`](collections.md#combine) 
    [`counts[item]`](collections.md#count) 
    [`elements`](collections.md#inspect) 
    [`most_common`](collections.md#count) 
    [`subtract`](collections.md#update) 
    [`total`](collections.md#count) 
    [`update`](collections.md#update) 

    [**`defaultdict`**](collections.md#defaultdict): 
    [`default_factory`](collections.md#defaultdict) 
    [`get`](collections.md#reading-vs-writing) 

    [**`namedtuple`**](collections.md#namedtuple): 
    [`_asdict`](collections.md#convert) 
    [`_field_defaults`](collections.md#inspect_1) 
    [`_fields`](collections.md#inspect_1) 
    [`_make`](collections.md#create) 
    [`_replace`](collections.md#convert) 
    [`defaults=`](collections.md#create) 

    [**`deque`**](collections.md#deque): 
    [`append`](collections.md#add) 
    [`appendleft`](collections.md#add) 
    [`clear`](collections.md#remove) 
    [`copy`](collections.md#inspect_2) 
    [`count`](collections.md#inspect_2) 
    [`extend`](collections.md#add) 
    [`extendleft`](collections.md#add) 
    [`index`](collections.md#inspect_2) 
    [`insert`](collections.md#add) 
    [`maxlen=`](collections.md#reorder) 
    [`pop`](collections.md#remove) 
    [`popleft`](collections.md#remove) 
    [`remove`](collections.md#remove) 
    [`reverse`](collections.md#reorder) 
    [`rotate`](collections.md#reorder) 

    [**`OrderedDict`**](collections.md#ordereddict): 
    [`==`](collections.md#compare) 
    [`move_to_end`](collections.md#reorder_1) 
    [`popitem`](collections.md#reorder_1) 

    [**`ChainMap`**](collections.md#chainmap): 
    [`maps`](collections.md#inspect_3) 
    [`new_child`](collections.md#extend) 
    [`parents`](collections.md#inspect_3) 

    [**`User* wrapper`**](collections.md#user-wrapper-classes): 
    [`UserDict`](collections.md#user-wrapper-classes) 
    [`UserList`](collections.md#user-wrapper-classes) 
    [`UserString`](collections.md#user-wrapper-classes) 

-   :material-calendar-clock:{ .lg .middle } [__datetime__](datetime.md) 
[:material-language-python:](datetime.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Calculating and formatting dates and times.

    [`creating a specific date`](datetime.md#creating-a-specific-date) 
    [`date`](datetime.md#creating-dates-and-times) 
    [`strftime`](datetime.md#formatting-with-strftime) 

    [`difference between two dates`](datetime.md#difference-between-two-dates) 
    [`strptime`](datetime.md#parsing-a-string-with-strptime) 
    [`timedelta`](datetime.md#date-arithmetic) 

-   :material-square-root-box:{ .lg .middle } [__math__](math.md) 
[:material-language-python:](math.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Rounding, roots, constants, and logarithms.

    [**`floor`**](math.md#rounding): 
    [`ceil`](math.md#rounding) 
    [`trunc`](math.md#trunc) 

    [**`sqrt`**](math.md#roots-and-powers): 
    [`pow`](math.md#pow) 
    [`isqrt`](math.md#pow) 

    [**`pi`**](math.md#constants): 
    [`inf`](math.md#constants) 
    [`nan`](math.md#constants) 

    [**`log2`**](math.md#logarithms): 
    [`log10`](math.md#logarithms) 
    [`exp`](math.md#logarithms) 

    [**`isclose`**](math.md#comparing-floats)

-   :material-dice-multiple:{ .lg .middle } [__random__](random.md) 
[:material-language-python:](random.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Random numbers, random picks, shuffled order.

    [**`randint`**](random.md#random-numbers)

    [**`choice`**](random.md#random-selections): 
    [`sample`](random.md#sampling-without-replacement) 
    [`shuffle`](random.md#shuffling-a-list) 

-   :material-text-search:{ .lg .middle } [__re__](re.md) 
[:material-language-python:](re.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Regular expressions: searching, extracting, and replacing text by pattern.

    [**`search`**](re.md#searching-for-a-pattern): 
    [`compile`](re.md#searching-for-a-pattern) 

    [**`findall`**](re.md#finding-all-matches) 

    [**`groups`**](re.md#groups): 
    [`named groups`](re.md#groups) 

    [**`sub`**](re.md#replacing-text) 

    [**`split`**](re.md#splitting-on-a-pattern)

-   :material-clock-outline:{ .lg .middle } [__time__](time.md) 
[:material-language-python:](time.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Reading the system clock, pausing execution, and measuring elapsed time.

    [**`time`**](time.md#reading-the-clock) 

    [**`sleep`**](time.md#pausing-execution) 

    [**`perf_counter`**](time.md#measuring-elapsed-time) 

    [**`localtime`**](time.md#formatting-the-current-time): 
    [`strftime`](time.md#formatting-the-current-time) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--4" markdown="block">
#### Data analysis { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-file-delimited-outline:{ .lg .middle } [__csv__](csv.md) 
[:material-language-python:](csv.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Reading and writing spreadsheets.

    [`writer`](csv.md#writing-csv-files)

    [`DictReader`](csv.md#reading-rows-as-dictionaries) 
    [`reader`](csv.md#reading-csv-files) 

-   :material-chart-line:{ .lg .middle } [__matplotlib__](matplotlib.md) 
[:material-download-outline:](matplotlib.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Charts and plots: line, bar, and scatter, built directly from plain Python data.

    [**`line plots`**](matplotlib.md#line-plots): 
    [`labels and title`](matplotlib.md#labels-and-title) 
    [`multiple lines and a legend`](matplotlib.md#multiple-lines-and-a-legend) 

    [**`bar charts`**](matplotlib.md#bar-charts)

    [**`scatter plots`**](matplotlib.md#scatter-plots)

    [**`subplots`**](matplotlib.md#subplots)

    [**`saving a figure`**](matplotlib.md#saving-a-figure)

-   :material-matrix:{ .lg .middle } [__NumPy__](numpy.md) 
[:material-download-outline:](numpy.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 
    {: data-advanced="card" }

    Fast numeric arrays, with math applied to a whole array at once instead of item by item.

    [**`array operations`**](numpy.md#array-operations): 
    [`boolean mask`](numpy.md#filtering-with-a-boolean-mask) 
    [`mean`](numpy.md#aggregating-an-array) 

    [`arange`](numpy.md#building-arrays-without-a-list) 
    [`ndarray`](numpy.md#creating-arrays) 

-   :material-table:{ .lg .middle } [__pandas__](pandas.md) 
[:material-download-outline:](pandas.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 
    {: data-advanced="card" }

    Tabular data: rows and columns, like a spreadsheet, built on top of NumPy.

    [**`DataFrame`**](pandas.md#building-a-dataframe)

    [**`working with a DataFrame`**](pandas.md#working-with-a-dataframe): 
    [`mean`](pandas.md#summarizing-a-column) 
    [`sort_values`](pandas.md#sorting-rows) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--2" markdown="block">
#### APIs { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-code-json:{ .lg .middle } [__json__](json.md) 
[:material-language-python:](json.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Reading and writing JSON data: nested dicts and lists, saved to a file or a string.

    [`dump`](json.md#writing-json-files)

    [`load`](json.md#reading-json-files) 
    [`nested data`](json.md#nested-data) 

    [`loads`](json.md#working-with-strings-instead-of-files)

-   :material-webhook:{ .lg .middle } [__requests__](requests.md) 
[:material-download-outline:](requests.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Fetching data over the internet, like asking a website or API for information.

    [**`how requests work`**](requests.md#how-a-request-works)

    [**`get`**](requests.md#making-a-request): 
    [`headers`](requests.md#custom-headers) 
    [`json`](requests.md#parsing-json) 
    [`params`](requests.md#query-parameters) 
    [`status_code`](requests.md#checking-the-status-code) 

    [**`post`**](requests.md#sending-data)

    [**`error handling`**](requests.md#handling-request-errors)

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Web scraping { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-pot-steam-outline:{ .lg .middle } [__BeautifulSoup__](beautifulsoup.md) 
[:material-download-outline:](beautifulsoup.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Parsing HTML: finding tags, reading attributes and text, and turning a page into structured data.

    [**`HTML and web pages`**](beautifulsoup.md#html-and-web-pages)

    [**`Parsing HTML`**](beautifulsoup.md#parsing-html): 
    [`Finding tags`](beautifulsoup.md#finding-tags) 
    [`Reading text and attributes`](beautifulsoup.md#reading-text-and-attributes) 

    [**`Extracting structured data`**](beautifulsoup.md#extracting-structured-data)

    [**`Putting it together`**](beautifulsoup.md#putting-it-together): 
    [`Common tasks`](beautifulsoup.md#common-tasks) 
    [`Scraping a real page`](beautifulsoup.md#scraping-a-real-page) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Image editing { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-image-outline:{ .lg .middle } [__Pillow__](pillow.md) 
[:material-download-outline:](pillow.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Opening, editing, and saving images, built around one Image object.

    [**`why Pillow?`**](pillow.md#why-pillow)

    [**`Image`**](pillow.md#the-image): 
    [`basic operations`](pillow.md#basic-operations) 
    [`crop`](pillow.md#crop) 
    [`image modes`](pillow.md#image-modes) 
    [`opening and saving images`](pillow.md#opening-and-saving-images) 
    [`resize`](pillow.md#resize) 
    [`rotate and flip`](pillow.md#rotate-and-flip) 

    [**`ImageOps`**](pillow.md#imageops-module): 
    [`common ImageOps functions`](pillow.md#common-imageops-functions) 

    [**`ImageDraw`**](pillow.md#imagedraw-module): 
    [`shapes and lines`](pillow.md#shapes-and-lines) 

    [**`ImageFont`**](pillow.md#imagefont-module): 
    [`loading a font`](pillow.md#loading-a-font) 

    [**`ImageColor`**](pillow.md#imagecolor-module): 
    [`converting color names`](pillow.md#converting-color-names) 

    [**`ImageFilter`**](pillow.md#imagefilter-module): 
    [`applying a filter`](pillow.md#applying-a-filter) 

    [**`ImageEnhance`**](pillow.md#imageenhance-module): 
    [`enhancing an image`](pillow.md#enhancing-an-image) 

    [**`ImageChops`**](pillow.md#imagechops-module): 
    [`comparing and combining images`](pillow.md#comparing-and-combining-images) 

    [**`convert`**](pillow.md#format-conversion): 
    [`converting between formats`](pillow.md#converting-between-formats) 

    [**`ImageSequence`**](pillow.md#imagesequence-module): 
    [`looping over GIF frames`](pillow.md#looping-over-gif-frames) 

    [**`putting it together`**](pillow.md#putting-it-together): 
    [`an interactive filter tool`](pillow.md#an-interactive-filter-tool) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Desktop UIs { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-application-outline:{ .lg .middle } [__Tkinter__](tkinter.md) 
[:material-language-python:](tkinter.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Creating desktop applications: text, buttons, dropdowns, forms, output, etc.

    [**`Tk`**](tkinter.md#creating-a-window)

    [**`Button`**](tkinter.md#widgets): 
    [`Button`](tkinter.md#button) 
    [`Entry`](tkinter.md#entry) 
    [`Label`](tkinter.md#label) 

    [**`pack`**](tkinter.md#layout-managers): 
    [`grid`](tkinter.md#grid) 
    [`pack`](tkinter.md#pack) 

    [**`configure`**](tkinter.md#configuring-widgets): 
    [`reading and changing options`](tkinter.md#reading-and-changing-options) 

    [**`command`**](tkinter.md#handling-events): 
    [`binding events`](tkinter.md#binding-events) 
    [`command callbacks`](tkinter.md#command-callbacks) 

    [**`Style`**](tkinter.md#styling-with-ttk): 
    [`customizing a style`](tkinter.md#customizing-a-style) 

    [**`messagebox`**](tkinter.md#dialogs): 
    [`file dialogs`](tkinter.md#file-dialogs) 
    [`message boxes`](tkinter.md#message-boxes) 

    [**`winfo_width`**](tkinter.md#introspecting-widgets): 
    [`winfo methods`](tkinter.md#winfo-methods) 

    [**`putting it together`**](tkinter.md#putting-it-together): 
    [`a simple form`](tkinter.md#a-simple-form) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block">
#### Games { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-turtle:{ .lg .middle } [__turtle__](turtle.md) 
[:material-language-python:](turtle.md){ .pt-lib-badge .pt-lib-badge--builtin title="Built-in — included with Python" } 

    Build small movement-based games with a pen cursor.

    [**`Concepts`**](turtle.md#concepts) 

    [**`Screen`**](turtle.md#the-screen): 
    [`Background`](turtle.md#background) 
    [`Clear`](turtle.md#clear-screen) 
    [`Close`](turtle.md#closing-the-window) 
    [`Colors`](turtle.md#colors) 
    [`Setup`](turtle.md#screen-setup) 

    [**`turtle cursor`**](turtle.md#the-turtle-cursor): 
    [`Appearance`](turtle.md#shape) 
    [`Circle`](turtle.md#circle) 
    [`Color`](turtle.md#shape-color-size) 
    [`Custom images`](turtle.md#custom-images) 
    [`Dot`](turtle.md#dot) 
    [`Drawing shapes`](turtle.md#drawing-shapes) 
    [`Hide`](turtle.md#show-or-hide) 
    [`Ink`](turtle.md#ink) 
    [`Motion`](turtle.md#positions-and-motion) 
    [`Positions`](turtle.md#positions-and-motion) 
    [`Rectangle`](turtle.md#rectangle) 
    [`Shape`](turtle.md#shape-color-size) 
    [`Show`](turtle.md#show-or-hide) 
    [`Size`](turtle.md#shape-color-size) 
    [`Stamping`](turtle.md#stamping) 
    [`Text`](turtle.md#text) 
    [`Tracer`](turtle.md#trace-movement) 
     
    [**`Game loop`**](turtle.md#the-game-loop): 
    [`done()`](turtle.md#done) 

    [**`Input`**](turtle.md#input): 
    [`Dialog prompts`](turtle.md#dialog-prompts) 
    [`Keyboard`](turtle.md#keyboard) 
    [`Mouse`](turtle.md#mouse) 

    [**`inside`**](turtle.md#detecting-collisions): 
    [`Distance`](turtle.md#distance) 
    [`Membership`](turtle.md#membership) 
    [`Overlap`](turtle.md#overlap) 

    [**`Common patterns`**](turtle.md#common-patterns) 

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block" data-advanced="true">
#### Testing { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-test-tube:{ .lg .middle } [__pytest__](pytest.md) 
[:material-download-outline:](pytest.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 

    Writing and running tests: assertions, fixtures, and parametrizing.

    [**`writing and running a test`**](pytest.md#writing-and-running-a-test): 
    [`from the command line`](pytest.md#from-the-command-line) 

    [**`reading a failure`**](pytest.md#reading-a-failure)

    [**`fixtures`**](pytest.md#fixtures)

    [**`parametrizing tests`**](pytest.md#parametrizing-tests)

    [**`testing for exceptions`**](pytest.md#testing-for-exceptions)

</div>
</div>

<div class="pt-category pt-category--wide pt-lib--1" markdown="block" data-advanced="true">
#### Computer vision { .pt-homepage-heading }

<div class="grid cards" markdown="block">

-   :material-face-recognition:{ .lg .middle } [__OpenCV__](opencv.md) 
[:material-download-outline:](opencv.md){ .pt-lib-badge .pt-lib-badge--third-party title="Third-party — install separately with pip" } 
    {: data-advanced="card" }

    Real-time image and video analysis, built directly on NumPy arrays: color spaces, edge detection, face detection.

    [**`reading, displaying, saving images`**](opencv.md#reading-displaying-and-saving-images): 
    [`displaying a window`](opencv.md#displaying-a-window) 
    [`imread`](opencv.md#reading-a-file) 
    [`saving a file`](opencv.md#saving-a-file) 

    [**`drawing`**](opencv.md#drawing-shapes-and-text): 
    [`shapes and lines`](opencv.md#shapes-and-lines) 
    [`text`](opencv.md#text) 

    [**`color spaces`**](opencv.md#color-spaces): 
    [`cvtColor`](opencv.md#converting-color-spaces) 

    [**`CascadeClassifier`**](opencv.md#face-detection-with-cascade-classifiers): 
    [`detecting and labeling faces`](opencv.md#detecting-and-labeling-faces) 

    [**`VideoCapture`**](opencv.md#working-with-video): 
    [`reading frames`](opencv.md#reading-frames) 

    [**`basic operations`**](opencv.md#basic-operations): 
    [`cropping`](opencv.md#cropping) 
    [`resize`](opencv.md#resize) 
    [`rotating`](opencv.md#rotating) 

    [**`thresholding, edge detection`**](opencv.md#thresholding-and-edge-detection): 
    [`Canny`](opencv.md#edge-detection) 
    [`threshold`](opencv.md#threshold) 

    [**`blurring`**](opencv.md#blurring): 
    [`gaussian blur`](opencv.md#gaussian-blur) 

    [**`contours`**](opencv.md#contours): 
    [`finding and drawing contours`](opencv.md#finding-and-drawing-contours) 

</div>
</div>

</div>
