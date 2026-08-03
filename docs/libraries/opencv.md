# :material-face-recognition:{ .lg .middle } OpenCV library

**OpenCV** (imported as `cv2`) is Python's standard library for computer vision — real-time image and video analysis, rather than the straightforward photo editing [Pillow](pillow.md) is built for. It's a third-party package (`pip install opencv-python`), originally written in C++ with a thin Python wrapper over it, which shows up in a couple of its API choices: images load as plain NumPy arrays instead of a dedicated `Image` class, and in **BGR** (blue-green-red) channel order rather than the RGB most other tools expect. Like Pillow and [Tkinter](tkinter.md), OpenCV produces visual, often interactive output — a window showing an image or a live camera feed — that can't run inside this site's browser sandbox, so the examples below aren't runnable here. Copy them into a local `.py` file alongside an image and run them with `python` to see the results.

| Concept | What it is |
|---------|------------|
| `Mat` | OpenCV's name (from its C++ origins) for an image — in Python it's just a NumPy `ndarray`, so array indexing and slicing double as OpenCV's crop tool. |
| BGR | The channel order OpenCV loads color images in by default — blue, green, red — the reverse of the RGB order most other tools (and humans) expect. |
| Grayscale | A single-channel image storing brightness only, no color — required by several operations (thresholding, edge detection, face detection) before they'll run. |
| Kernel | A small matrix of numbers used to blur, sharpen, or otherwise transform an image by combining each pixel with its neighbors. |
| Threshold | A cutoff brightness value used to turn a grayscale image into pure black and white. |
| Contour | A curve joining the continuous points along a shape's boundary, used to count, measure, or outline objects in an image. |
| Cascade classifier | A pre-trained model, shipped with OpenCV, that scans an image for a specific object — most commonly a face. |
| Frame | One still image out of a video, read and processed one at a time in a loop. |

For a broader comparison of OpenCV against Pillow and other Python image libraries, see the table on the [Pillow page](pillow.md#why-pillow).

| Section | Used for |
|---------|----------|
| [Reading, displaying, and saving images](#reading-displaying-and-saving-images) | Getting a file from disk into a variable, and back out again. |
| [Color spaces](#color-spaces) | Converting between BGR, RGB, grayscale, and HSV. |
| [Basic operations](#basic-operations) | Resizing, cropping (via NumPy slicing), and rotating. |
| [Drawing shapes and text](#drawing-shapes-and-text) | Annotating an image directly, in place. |
| [Thresholding and edge detection](#thresholding-and-edge-detection) | Reducing an image to just the boundaries or regions that matter. |
| [Blurring](#blurring) | Smoothing out noise before further analysis. |
| [Contours](#contours) | Finding and outlining distinct shapes in a black-and-white image. |
| [Face detection with cascade classifiers](#face-detection-with-cascade-classifiers) | Locating faces (or other objects) at multiple positions and scales. |
| [Working with video](#working-with-video) | Applying any of the above to a live camera feed or video file, one frame at a time. |

## Import

OpenCV's package name (`opencv-python`) doesn't match its import name — it's always imported as `cv2`.

```python-ref
import cv2
```

## Reading, displaying, and saving images

Every OpenCV workflow starts the same way: load a file into an array, do something to it, then optionally write the result back out.

```python-ref
import cv2

img = cv2.imread("snake.jpg")
print(img.shape)   # (600, 800, 3) -- height, width, channels

cv2.imshow("field guide", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("snake_copy.png", img)
```

### Reading a file

`cv2.imread(path)` loads immediately into a full NumPy array — unlike Pillow's `Image.open()`, there's no lazy header-only read; the whole pixel grid is decoded right away. `.shape` reports `(height, width, channels)`, the opposite order of Pillow's `.size`, which gives `(width, height)`. If the path is wrong, `imread()` doesn't raise an error — it silently returns `None`, so check for that before doing anything else with the result.

```python-ref
img = cv2.imread("snake.jpg")
if img is None:
    print("could not read file")
else:
    print(img.shape)   # (600, 800, 3)
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
if img is None:
    print("could not read file")
else:
    print(img.shape)
```

### Displaying a window

`cv2.imshow(title, img)` opens a window showing the image, but it closes immediately unless paired with `cv2.waitKey(0)`, which pauses the program until a key is pressed. `cv2.destroyAllWindows()` then closes every OpenCV window still open. All three need a real display attached — they're for local development, not headless scripts.

```python-ref
cv2.imshow("field guide", img)
cv2.waitKey(0)          # 0 = wait forever for a keypress
cv2.destroyAllWindows()
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
cv2.imshow("field guide", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Saving a file

`cv2.imwrite(path, img)` writes the array back to disk, inferring the format from the file extension the same way Pillow's `.save()` does. It returns `True`/`False` instead of raising an exception on failure, so check the return value if the write matters.

```python-ref
saved = cv2.imwrite("snake_copy.png", img)
print(saved)   # True
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
saved = cv2.imwrite("snake_copy.png", img)
print(saved)
```

## Color spaces

OpenCV loads color images in **BGR** order rather than RGB — a holdover from its early camera-driver roots — so handing a BGR array to a tool that expects RGB (like `matplotlib`) shows swapped colors unless it's converted first. `cv2.cvtColor()` handles every conversion between color spaces.

```python-ref
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

### Converting color spaces

`cv2.cvtColor(img, code)` — the `code` names which conversion to run, always written `COLOR_<FROM>2<TO>`. `COLOR_BGR2GRAY` collapses color down to a single grayscale channel, `COLOR_BGR2RGB` just reorders channels for tools that expect RGB, and `COLOR_BGR2HSV` switches to hue/saturation/value, which turns "everything that's green" into a range check on one channel instead of three.

```python-ref
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)   # (600, 800) -- no channel dimension
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
cv2.imwrite("snake_gray.png", gray)
```

??? tip "The BGR vs RGB gotcha"
    Forgetting this conversion is one of the most common OpenCV mistakes — a photo loaded with `cv2.imread()` and handed straight to something expecting RGB (like `matplotlib.pyplot.imshow()`) renders with blue and red swapped, with no error raised to explain why the colors look wrong.

    ```python-ref
    import cv2
    import matplotlib.pyplot as plt

    img = cv2.imread("snake.jpg")               # loaded as BGR
    correct = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(correct)                          # colors display correctly
    ```

## Basic operations

A `Mat` is really just a NumPy array under the hood, so some "operations" are plain NumPy indexing rather than an OpenCV-specific method — cropping in particular.

```python-ref
resized = cv2.resize(img, (400, 300))
cropped = img[50:250, 0:200]
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
```

### Resize

`cv2.resize(img, (width, height))` stretches the image to an exact new size — the same tradeoff as Pillow's `.resize()`, it doesn't preserve the original aspect ratio unless the new dimensions are computed to match it.

```python-ref
resized = cv2.resize(img, (200, 150))
print(resized.shape)   # (150, 200, 3)
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
resized = cv2.resize(img, (200, 150))
print(resized.shape)
```

### Cropping

Since a `Mat` is just a NumPy array, cropping is a plain slice: `img[y1:y2, x1:x2]` — rows (height) first, then columns (width), the reverse of the `(x, y)` order most drawing functions use. There's no dedicated `.crop()` method to reach for.

```python-ref
cropped = img[50:250, 0:200]   # rows 50-250, columns 0-200
print(cropped.shape)   # (200, 200, 3)
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
cropped = img[50:250, 0:200]
print(cropped.shape)
```

### Rotating

`cv2.rotate(img, code)` handles clean 90°-multiple rotations with a fixed set of codes (`ROTATE_90_CLOCKWISE`, `ROTATE_180`, `ROTATE_90_COUNTERCLOCKWISE`). For an arbitrary angle, build a rotation matrix with `cv2.getRotationMatrix2D()` and apply it with `cv2.warpAffine()`.

```python-ref
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

height, width = img.shape[:2]
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1.0)
rotated_45 = cv2.warpAffine(img, matrix, (width, height))
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

height, width = img.shape[:2]
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1.0)
rotated_45 = cv2.warpAffine(img, matrix, (width, height))
cv2.imwrite("rotated.jpg", rotated_45)
```

## Drawing shapes and text

Drawing functions modify a `Mat` directly, in place — there's no separate drawing-context object like Pillow's `ImageDraw.Draw()`.

```python-ref
cv2.rectangle(img, (10, 10), (100, 60), (0, 128, 0), 3)
cv2.putText(img, "handler", (15, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 0), 2)
```

### Shapes and lines

`cv2.rectangle()`, `cv2.circle()`, and `cv2.line()` each take two corner/center points, a **BGR** color tuple, and a thickness in pixels — pass `-1` as the thickness to fill the shape solid instead of outlining it.

```python-ref
cv2.rectangle(img, (10, 10), (100, 60), (0, 128, 0), 3)     # outline, 3px
cv2.circle(img, (150, 40), 25, (0, 200, 255), -1)           # filled
cv2.line(img, (0, 0), (100, 100), (0, 0, 0), 2)
```

```python-ref
import cv2
import numpy as np

canvas = np.full((120, 200, 3), 255, dtype="uint8")   # blank white canvas
cv2.rectangle(canvas, (10, 10), (100, 60), (0, 128, 0), 3)
cv2.circle(canvas, (150, 40), 25, (0, 200, 255), -1)
cv2.imwrite("shapes.png", canvas)
```

### Text

`cv2.putText()` needs a font (one of the built-in `cv2.FONT_HERSHEY_*` constants — there's no custom font loading the way Pillow's `ImageFont` offers), a size scale rather than a point size, and a position given as the text's **bottom-left** corner rather than its top-left.

```python-ref
cv2.putText(canvas, "burmese python", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
```

```python-ref
import cv2
import numpy as np

canvas = np.full((120, 200, 3), 255, dtype="uint8")
cv2.putText(canvas, "burmese python", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
cv2.imwrite("labeled.png", canvas)
```

## Thresholding and edge detection

Both operations reduce an image down to just the information that matters for a specific analysis task, throwing away "how bright" or "how gradual" in favor of a hard yes/no per pixel.

```python-ref
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
edges = cv2.Canny(gray, 100, 200)
```

### Threshold

`cv2.threshold(img, cutoff, max_value, method)` turns a grayscale image into pure black-and-white: every pixel above `cutoff` becomes `max_value` (usually `255`, white), everything else becomes `0` (black). It returns a tuple — the cutoff value actually used, and the resulting image — which is why the example throws the first value away with `_`.

```python-ref
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("thresholded.png", thresholded)
```

### Edge detection

`cv2.Canny(img, low, high)` traces outlines wherever brightness changes sharply, and works best on a grayscale image. `low` and `high` set two brightness-change thresholds — a change above `high` is always kept as an edge, a change below `low` is always discarded, and anything in between is kept only if it connects to a pixel already counted as an edge.

```python-ref
edges = cv2.Canny(gray, 100, 200)
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imwrite("edges.png", edges)
```

## Blurring

Smoothing an image slightly, before edge detection or thresholding, often removes small specks of noise that would otherwise show up as false edges or scattered dark pixels.

```python-ref
blurred = cv2.GaussianBlur(img, (5, 5), 0)
```

### Gaussian blur

`cv2.GaussianBlur(img, kernel_size, sigma)` averages each pixel with its neighbors, weighted so nearby pixels count more than far ones. Both numbers in `kernel_size` (width, height) must be odd, and a larger kernel blurs more heavily. `sigma` — the spread of that weighting — can usually be left at `0` to let OpenCV calculate it automatically from the kernel size.

```python-ref
blurred = cv2.GaussianBlur(img, (5, 5), 0)
heavily_blurred = cv2.GaussianBlur(img, (21, 21), 0)
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
blurred = cv2.GaussianBlur(img, (5, 5), 0)
heavily_blurred = cv2.GaussianBlur(img, (21, 21), 0)
cv2.imwrite("blurred.jpg", blurred)
```

## Contours

A **contour** is a curve joining the continuous points along a shape's boundary — useful for counting objects in an image, measuring their size, or outlining just the shapes rather than the whole image.

```python-ref
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 128, 0), 2)
```

### Finding and drawing contours

`cv2.findContours()` needs a black-and-white image (usually the output of `cv2.threshold()` or `cv2.Canny()`) and returns a list of contours, each a list of boundary points. `cv2.drawContours(img, contours, index, color, thickness)` draws them back onto an image — pass `-1` as the index to draw every contour found rather than just one.

```python-ref
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))   # number of separate shapes found
cv2.drawContours(img, contours, -1, (0, 128, 0), 2)
```

```python-ref
import cv2

img = cv2.imread("snake.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 128, 0), 2)
cv2.imwrite("contours.png", img)
```

## Face detection with cascade classifiers

A **cascade classifier** is a pre-trained model, shipped with OpenCV itself, that scans an image at many positions and scales looking for a specific object — most commonly, faces.

```python-ref
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
```

### Detecting and labeling faces

`cv2.data.haarcascades` points to OpenCV's own folder of pre-trained `.xml` cascade files, so no separate download is needed for common detectors like frontal faces. `.detectMultiScale()` returns a list of `(x, y, width, height)` boxes, one per match — looping over them lets you draw a box (and a label) around each one found.

```python-ref
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 128, 0), 2)
    cv2.putText(img, "handler", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 128, 0), 2)
```

```python-ref
import cv2

img = cv2.imread("handler.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 128, 0), 2)
    cv2.putText(img, "handler", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 128, 0), 2)

cv2.imwrite("detected.jpg", img)
```

## Working with video

A video is really just a sequence of frames, read and processed one at a time — everything covered above (color conversion, drawing, detection) applies to a single video frame exactly the same way it applies to a still image.

```python-ref
capture = cv2.VideoCapture(0)   # 0 = default webcam
while True:
    success, frame = capture.read()
    if not success:
        break
    cv2.imshow("field guide", frame)
    if cv2.waitKey(1) == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()
```

### Reading frames

`cv2.VideoCapture(source)` opens a webcam (an integer index, `0` for the default camera) or a video file (a path string). `.read()` returns `(success, frame)` each time it's called — `success` becomes `False` once a video file runs out of frames, which is what ends the loop naturally. `cv2.waitKey(1)` keeps the display window responsive and doubles as a keypress check (here, `q` to quit) without blocking the way `waitKey(0)` does. `.release()` frees the camera/file so other programs can use it again.

```python-ref
import cv2

capture = cv2.VideoCapture("snake_slither.mp4")
frame_count = 0

while True:
    success, frame = capture.read()
    if not success:
        break
    frame_count += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"frame_{frame_count}.png", gray)

capture.release()
print(f"saved {frame_count} frames")
```
