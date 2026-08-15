---
description: >-
  Opening, editing, and saving images in Python with Pillow: resizing, cropping, drawing,
  filters, and format conversion.
---

# :material-image-outline:{ .lg .middle } Pillow library

**Pillow** (imported as `PIL`) is Python's standard library for opening, editing, and saving image files — photos, screenshots, thumbnails, anything in a common format like JPEG or PNG. It's a third-party package, not part of the standard library, but it's the de facto standard for image work in Python. Like [Tkinter](tkinter.md), Pillow ultimately produces visual output — a saved or displayed image — which can't be shown inside this site's browser sandbox, so the examples below aren't runnable here. Copy them into a local `.py` file alongside an image and run them with `python` to see the results.

## Install

```bash
pip install pillow
```

## Import

Pillow's package name (`pillow`) doesn't match its import name — it's imported as `PIL`, and `Image` specifically is used throughout this page.

```python-ref
from PIL import Image
```

## Why Pillow?

Pillow is the direct successor to PIL (the original Python Imaging Library, now unmaintained), and has become the standard way to work with images in Python — resizing thumbnails, converting formats, watermarking, or feeding images into a machine learning pipeline. It wraps all of this in one consistent `Image` object, so once you know how to open, transform, and save an image, the same handful of methods carry over to almost any task.

**Python image libraries**

- **Pillow** — the standard choice for everyday image tasks: opening, resizing, cropping, format conversion, basic drawing.
- **OpenCV** — built for computer vision (face detection, video, real-time processing), but a much larger, more complex API for tasks that don't need it.
- **scikit-image** — geared toward scientific image analysis (measuring, segmenting), with a more research-oriented API than Pillow's straightforward editing tools.
- **ImageIO** — handles reading/writing a wide range of formats, including scientific and video ones, but doesn't offer Pillow's editing operations on top.

For everyday image manipulation, Pillow offers the best balance of simplicity and capability — most tasks are one or two method calls on an `Image` object.

| Concept | What it is |
|---------|------------|
| `Image` object | A grid of pixel values, plus a bit of metadata (size, mode, format) — nothing more. It has no built-in ability to draw shapes, apply filters, or combine with another image. |
| Companion module | A separate module (`ImageDraw`, `ImageFilter`, `ImageOps`, ...) that operates on an `Image` from the outside, rather than `Image` itself growing a method for everything. |
| Mode | How pixel color is stored — `"RGB"` (red/green/blue), `"RGBA"` (adds transparency), `"L"` (grayscale), and others. |
| Band | One channel of a mode — an `"RGB"` image has three bands (red, green, blue) stacked together. |
| Size | The image's `(width, height)` in pixels, accessed via `.size`. |
| Bounding box | A `(left, upper, right, lower)` tuple of pixel coordinates describing a rectangular region of an image. |
| Drawing context | The object returned by `ImageDraw.Draw(img)` — every shape/line/text method is called on this, not on the `Image` itself. |
| Alpha | The transparency value of a pixel, from `0` (fully invisible) to `255` (fully solid) — only present on images in `"RGBA"` mode. |
| Frame | One image within an animated file (like a GIF) — `ImageSequence` is what lets you loop over all of them. |

Beyond the base [`Image`](#the-image) object, Pillow's functionality is spread across several companion modules under the `PIL` package:

| Module | Used for |
|--------|----------|
| [`ImageDraw`](#imagedraw-module) | Drawing shapes, lines, and polygons directly onto an image. |
| [`ImageFont`](#imagefont-module) | Loading a custom font, for then drawing text with `ImageDraw`. |
| [`ImageColor`](#imagecolor-module) | Converting a color name or hex string into an `(r, g, b)` tuple. |
| [`ImageFilter`](#imagefilter-module) | Applying ready-made pixel effects — blur, sharpen, edge-detection. |
| [`ImageEnhance`](#imageenhance-module) | Dialing brightness, contrast, color, or sharpness up or down by an exact amount. |
| [`ImageOps`](#imageops-module) | One-line convenience operations — auto-contrast, mirroring, inverting. |
| [`ImageChops`](#imagechops-module) | Combining two same-size images pixel by pixel — diffing, blending. |
| [`ImageSequence`](#imagesequence-module) | Looping over every frame of an animated image, like a GIF. |

## The Image

The `Image` object is where every Pillow workflow starts and ends — opening a file, transforming it, and saving the result all happen through methods on this one class.

### Opening and saving images

Every Pillow workflow starts the same way: open a file into an `Image` object, do something to it, then save the result — Pillow infers the file format from the extension you save to, so converting formats is often just a matter of changing the file extension.

```python-ref
from PIL import Image

img = Image.open("snake.jpg")
print(img.size, img.mode)   # (800, 600) RGB

img.save("snake_copy.png")
```

??? tip "Opening a file"
    Reads a file's header immediately but delays loading the full pixel data until you need it. Fast even for large images if all you want is its size or format. `.format` reports the file type Pillow detected, `.size` gives `(width, height)`, and `.mode` gives its color mode.

    ```python-ref
    img = Image.open("snake.jpg")
    print(img.format, img.size, img.mode)   # JPEG (800, 600) RGB
    ```

    ```python-ref
    from PIL import Image

    img = Image.open("snake.jpg")
    print(img.format, img.size, img.mode)
    ```

??? tip "Saving a file"
    Writes the image to disk, picking the file format from the extension — unless you pass `format=` explicitly. Some formats accept extra keyword options — JPEG's `quality` (0–100) trades file size for image quality, for example.

    ```python-ref
    img.save("snake_copy.png")            # format inferred from ".png"
    img.save("snake_copy.jpg", quality=85)  # JPEG-specific option
    ```

    ```python-ref
    from PIL import Image

    img = Image.open("snake.jpg")
    img.save("snake_copy.png")
    img.save("snake_copy.jpg", quality=85)
    ```

??? tip "Displaying an image"
    Opens the image in whatever program your operating system uses to view images. Handy for a quick look while writing a script, since it doesn't require saving a file first. It's meant for local development rather than production code, since it depends on external programs actually being installed.

    ```python-ref
    img.show()   # opens in your OS's default image viewer
    ```

    ```python-ref
    from PIL import Image

    img = Image.open("snake.jpg")
    img.show()
    ```

### Basic operations

Pillow's core editing operations — resizing, cropping, rotating, flipping — are all methods on an `Image` that return a *new* `Image`, leaving the original untouched.

```python-ref
resized = img.resize((400, 300))
cropped = img.crop((0, 0, 200, 200))
rotated = img.rotate(90)
```

#### Resize

Scales the image to an exact new size. `.resize((width, height))` doesn't preserve the original aspect ratio for you, so stretching happens if the new dimensions don't match the original proportions. For a quick, ratio-preserving thumbnail instead, use `.thumbnail((max_width, max_height))`, which resizes in place rather than returning a new image.

```python-ref
thumbnail = img.resize((200, 150))
print(thumbnail.size)   # (200, 150)
```

```python-ref
from PIL import Image

img = Image.open("snake.jpg")
thumbnail = img.resize((200, 150))
print(thumbnail.size)
```

#### Crop

Takes a bounding box and returns just that rectangular region. `.crop()` takes `(left, upper, right, lower)` pixel coordinates. `(0, 0)` is the top-left corner of the image, with `x` increasing rightward and `y` increasing downward.

```python-ref
cropped = img.crop((50, 50, 250, 200))   # left, upper, right, lower
print(cropped.size)   # (200, 150)
```

```python-ref
from PIL import Image

img = Image.open("snake.jpg")
cropped = img.crop((50, 50, 250, 200))
print(cropped.size)
```

#### Rotate and flip

`.rotate(degrees)` rotates counter-clockwise around the image's center. Pass `expand=True` to grow the canvas so corners aren't clipped off (without it, the image keeps its original size and rotated corners are cropped away). `.transpose()` handles flips and 90°-multiple rotations without any clipping concerns, using constants like `Image.FLIP_LEFT_RIGHT` or `Image.ROTATE_90`.

```python-ref
rotated = img.rotate(90, expand=True)
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
```

```python-ref
from PIL import Image

img = Image.open("snake.jpg")
rotated = img.rotate(90, expand=True)
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
print(rotated.size, flipped.size)
```

### Image modes

An image's **mode** determines how each pixel's color is stored — how many bands it has and what each one means. Converting between modes is a single method call, and it's often a required first step before an operation that only works on one mode (like grayscale-only filters). `.convert(mode)` returns a new image re-encoded into the given mode — `"L"` collapses color down to a single grayscale band; `"RGBA"` adds an alpha (transparency) band on top of red/green/blue, where `0` is fully transparent and `255` is fully opaque.

```python-ref
grayscale = img.convert("L")     # single band, 0 (black) to 255 (white)
rgba = img.convert("RGBA")       # adds a 4th, transparency band
print(grayscale.mode, rgba.mode)  # L RGBA
```

```python-ref
from PIL import Image

img = Image.open("snake.jpg")
grayscale = img.convert("L")
rgba = img.convert("RGBA")
print(grayscale.mode, rgba.mode)
```

## ImageOps module

The `ImageOps` module collects common one-line transforms that would otherwise take several steps to write by hand — contrast fixes, mirroring, and color inversion among them.

```python-ref
from PIL import ImageOps

fixed = ImageOps.autocontrast(img)
mirrored = ImageOps.mirror(img)
```

### Common ImageOps functions

`.autocontrast()` stretches an image's darkest and lightest pixels out to pure black and white, which can fix a flat, washed-out photo without manually tuning `ImageEnhance.Contrast`. `.mirror()`/`.flip()` cover the same ground as `.transpose()` with more direct names. `.invert()` flips every pixel to its opposite color — it only works on `"RGB"` (or `"L"`) images, so convert first if the source has an alpha band.

```python-ref
fixed = ImageOps.autocontrast(img)   # stretches contrast to use the full range
mirrored = ImageOps.mirror(img)      # flips left-to-right
inverted = ImageOps.invert(img.convert("RGB"))   # like a photo negative
```

```python-ref
from PIL import Image, ImageOps

img = Image.open("snake.jpg")
fixed = ImageOps.autocontrast(img)
mirrored = ImageOps.mirror(img)
inverted = ImageOps.invert(img.convert("RGB"))
fixed.save("fixed.jpg")
```

## ImageDraw module

An `Image` object is really just a grid of pixel values — it has no drawing tools of its own. `ImageDraw` is the first example of a **companion module**: a separate class that wraps an `Image` and adds one specific ability, here turning it into a canvas you can draw directly onto — shapes and lines, useful for annotating a photo or generating an image from scratch rather than editing an existing file. `ImageFont`, `ImageFilter`, `ImageEnhance`, `ImageOps`, and the modules further down this page all follow the same pattern: they act on an `Image` from the outside, rather than `Image` itself growing a method for everything.

```python-ref
from PIL import ImageDraw

draw = ImageDraw.Draw(img)
draw.rectangle((10, 10, 100, 60), outline="green", width=3)
draw.text((15, 20), "ball python", fill="green")
```

### Shapes and lines

`ImageDraw.Draw(img)` creates a drawing context bound to an image. Every call on it modifies `img` directly, in place. `.rectangle()`, `.ellipse()`, and `.line()` each take a bounding box or set of coordinates, plus `outline`/`fill` colors and an optional `width`.

```python-ref
draw.rectangle((10, 10, 100, 60), outline="green", width=3)
draw.ellipse((20, 20, 80, 50), fill="yellow")
draw.line((0, 0, 100, 100), fill="black", width=2)
```

```python-ref
from PIL import Image, ImageDraw

img = Image.new("RGB", (120, 80), "white")
draw = ImageDraw.Draw(img)
draw.rectangle((10, 10, 100, 60), outline="green", width=3)
draw.ellipse((20, 20, 80, 50), fill="yellow")
img.save("shapes.png")
```

??? tip "Polygons"
    Draws any straight-edged shape from a list of `(x, y)` points. `.polygon()` connects the points in order, with the last point automatically connected back to the first. Unlike `.rectangle()`/`.ellipse()`, there's no bounding-box shortcut: you calculate each corner's coordinates yourself, usually from a center position and size.

    ```python-ref
    points = [(60, 10), (110, 70), (10, 70)]   # a triangle
    draw.polygon(points, fill="green")
    ```

    ```python-ref
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (120, 80), "white")
    draw = ImageDraw.Draw(img)
    points = [(60, 10), (110, 70), (10, 70)]
    draw.polygon(points, fill="green")
    img.save("triangle.png")
    ```

??? tip "Transparent colors"
    A color can include a fourth number — alpha — to draw something translucent, from `0` (fully invisible) to `255` (fully solid), so shapes underneath still show through. This only works on an image in `"RGBA"` mode; drawing an RGBA color onto a plain `"RGB"` image just silently drops the transparency.

    ```python-ref
    draw.ellipse((20, 20, 80, 80), fill=(255, 0, 0, 120))   # translucent red
    ```

    ```python-ref
    from PIL import Image, ImageDraw

    img = Image.new("RGBA", (120, 80), "white")
    draw = ImageDraw.Draw(img)
    draw.ellipse((10, 10, 70, 70), fill=(255, 0, 0, 255))
    draw.ellipse((40, 30, 100, 70), fill=(0, 0, 255, 120))   # overlaps, translucent
    img.save("overlap.png")
    ```

??? tip "Drawing with objects"
    Once a drawing gets complicated, it's common to wrap each thing you're drawing in its own class — an object that stores its own position/size/color, and knows how to draw itself given a drawing context. Nothing here is Pillow-specific: it's the same pattern covered in [Classes](../oop.md) — bundling data with the behavior that acts on it — just applied to a shape instead of a snake. A calling function loops over a list of these objects and calls `.draw()` on each, so building a complex image — dozens of randomly placed shapes, say, using the `random` module — is just a loop appending new `Shape` objects rather than dozens of manual `draw_context` calls.

    ```python-ref
    class Shape:
        def __init__(self, position, size, color):
            self.position = position
            self.size = size
            self.color = color

        def draw(self, draw_context):
            x, y = self.position
            half = self.size / 2
            box = (x - half, y - half, x + half, y + half)
            draw_context.ellipse(box, fill=self.color)
    ```

    ```python-ref
    import random
    from PIL import Image, ImageDraw


    class Shape:
        def __init__(self, position, size, color):
            self.position = position
            self.size = size
            self.color = color

        def draw(self, draw_context):
            x, y = self.position
            half = self.size / 2
            box = (x - half, y - half, x + half, y + half)
            draw_context.ellipse(box, fill=self.color)

    img = Image.new("RGB", (200, 200), "white")
    draw_context = ImageDraw.Draw(img)
    palette = ["green", "yellow", "brown"]

    shapes = []
    for _ in range(10):
        position = (random.randint(0, 200), random.randint(0, 200))
        size = random.randint(10, 40)
        color = random.choice(palette)
        shapes.append(Shape(position, size, color))

    for shape in shapes:
        shape.draw(draw_context)

    img.save("generated.png")
    ```

## ImageFont module

`ImageDraw.text()` works with no extra setup, but falls back to a small built-in bitmap font. `ImageFont` loads an actual `.ttf` font file at a chosen size, for anything larger or more legible.

```python-ref
from PIL import ImageFont

font = ImageFont.truetype("arial.ttf", 20)
draw.text((10, 10), "burmese python", fill="black", font=font)
```

### Loading a font

Loads a `.ttf` (or `.otf`) font file at a specific point size. `ImageFont.truetype(path, size)` returns a font object to pass into `draw.text(..., font=font)`. The path can be a font file sitting next to your script, or a system font's full path — sizes aren't interchangeable between fonts, so reload at a new size rather than trying to scale a loaded font after the fact.

```python-ref
font = ImageFont.truetype("arial.ttf", 20)
draw.text((10, 10), "burmese python", fill="black", font=font)
```

```python-ref
from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (200, 60), "white")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 20)
draw.text((10, 15), "burmese python", fill="black", font=font)
img.save("labeled.png")
```

## ImageColor module

Drawing methods accept a color as a plain name (`"green"`) or a hex string (`"#3f6b52"`), but sometimes you need that same color as an actual `(r, g, b)` tuple — to do math on it, blend it with another color, or store it in a data structure like the `Shape` class above. `ImageColor.getrgb()` converts either format into the tuple Pillow uses internally.

```python-ref
from PIL import ImageColor

rgb = ImageColor.getrgb("green")        # (0, 128, 0)
rgb2 = ImageColor.getrgb("#3f6b52")     # (63, 107, 82)
```

### Converting color names

Accepts most CSS-style color names and `#rrggbb`/`#rgb` hex strings, returning a plain `(r, g, b)` tuple. `.getrgb()` returns `(r, g, b, a)` if the input included transparency. Useful once a palette is defined as hex codes rather than named colors, or when a color needs to be manipulated as numbers rather than passed straight into a drawing method.

```python-ref
green_rgb = ImageColor.getrgb("green")
hex_rgb = ImageColor.getrgb("#3f6b52")
print(green_rgb, hex_rgb)
```

```python-ref
from PIL import ImageColor

green_rgb = ImageColor.getrgb("green")
hex_rgb = ImageColor.getrgb("#3f6b52")
print(green_rgb, hex_rgb)
```

## ImageFilter module

Beyond geometric edits, `ImageFilter` can adjust an image's *look* — blurring, sharpening, or tracing its edges — by applying a ready-made pixel transformation, no convolution or kernel math required.

```python-ref
from PIL import ImageFilter

blurred = img.filter(ImageFilter.BLUR)
```

### Applying a filter

Applies one of Pillow's built-in filter presets, each a ready-made pixel transformation. `.filter()` — `ImageFilter.CONTOUR` traces edges into a sketch-like outline, distinct from `FIND_EDGES`, which highlights edges while keeping the rest of the image dark.

```python-ref
blurred = img.filter(ImageFilter.BLUR)
sharpened = img.filter(ImageFilter.SHARPEN)
edges = img.filter(ImageFilter.FIND_EDGES)
outlined = img.filter(ImageFilter.CONTOUR)
```

```python-ref
from PIL import Image, ImageFilter

img = Image.open("snake.jpg")
blurred = img.filter(ImageFilter.BLUR)
sharpened = img.filter(ImageFilter.SHARPEN)
outlined = img.filter(ImageFilter.CONTOUR)
blurred.save("blurred.jpg")
sharpened.save("sharpened.jpg")
outlined.save("outlined.jpg")
```

## ImageEnhance module

Where `ImageFilter` applies a fixed preset, `ImageEnhance` lets you dial an existing quality — brightness, contrast, color, sharpness — up or down by an exact amount.

```python-ref
from PIL import ImageEnhance

brighter = ImageEnhance.Brightness(img).enhance(1.5)
```

### Enhancing an image

Each `ImageEnhance` class wraps an image and exposes `.enhance(factor)`. `Brightness`, `Contrast`, `Color`, `Sharpness` — `1.0` leaves the image unchanged, below `1.0` reduces the effect, and above `1.0` increases it. `Color` controls saturation specifically: pushed toward `0.0` the image slides to grayscale, pushed well above `1.0` colors become more vivid and saturated.

```python-ref
brighter = ImageEnhance.Brightness(img).enhance(1.5)   # 1.0 = unchanged
higher_contrast = ImageEnhance.Contrast(img).enhance(1.3)
more_colorful = ImageEnhance.Color(img).enhance(2.0)   # boost saturation
```

```python-ref
from PIL import Image, ImageEnhance

img = Image.open("snake.jpg")
brighter = ImageEnhance.Brightness(img).enhance(1.5)
higher_contrast = ImageEnhance.Contrast(img).enhance(1.3)
more_colorful = ImageEnhance.Color(img).enhance(2.0)
brighter.save("brighter.jpg")
more_colorful.save("more_colorful.jpg")
```

## ImageChops module

Everything so far transforms a *single* image. `ImageChops` ("channel operations") instead combines two images of the same size, pixel by pixel — spotting what changed between two photos, or blending one image into another.

```python-ref
from PIL import ImageChops

diff = ImageChops.difference(before, after)
blended = ImageChops.multiply(img, mask)
```

### Comparing and combining images

`.difference(im1, im2)` subtracts one image from the other pixel by pixel. Identical areas come out solid black, and anything that changed shows up as a bright patch. Calling `.getbbox()` on the result gives the bounding box of everything that differs (or `None` if the two images are pixel-for-pixel identical), a quick way to check "did anything change?" without comparing every pixel yourself. `.multiply()`/`.screen()`/`.add()` combine two images with different blending math, similar to layer blend modes in photo-editing software.

```python-ref
diff = ImageChops.difference(before, after)
diff.getbbox()   # bounding box of everything that changed, or None if identical
```

```python-ref
from PIL import Image, ImageChops

before = Image.open("snake_before.jpg")
after = Image.open("snake_after.jpg")

diff = ImageChops.difference(before, after)
print(diff.getbbox())
diff.save("diff.jpg")
```

## Format conversion

Because `.save()` infers the output format from the file extension, converting between formats is usually just an open-then-save with a different name — with a couple of format-specific details worth knowing.

```python-ref
img = Image.open("snake.png")
img.convert("RGB").save("snake.jpg")   # JPEG has no transparency, so drop RGBA first
```

### Converting between formats

JPEG doesn't support transparency, so saving an `"RGBA"` image straight to `.jpg` raises an error. Convert to `"RGB"` first, which drops the alpha band. PNG, by contrast, supports both `"RGB"` and `"RGBA"` natively, so no conversion is needed going the other direction.

```python-ref
img = Image.open("snake.png")        # RGBA, with transparency
img.convert("RGB").save("snake.jpg")  # JPEG can't store alpha — convert first
```

```python-ref
from PIL import Image

img = Image.open("snake.png")
img.convert("RGB").save("snake.jpg")
```

## ImageSequence module

An animated GIF is really a whole stack of images shown one after another. `Image.open()` only gives you the first frame by default — `ImageSequence` lets a [`for` loop](../loops.md) step through every frame in order.

```python-ref
from PIL import Image, ImageSequence

gif = Image.open("snake_slither.gif")
for frame in ImageSequence.Iterator(gif):
    frame.save(f"frame_{frame.tell()}.png")
```

### Looping over GIF frames

Hands a `for` loop one frame at a time, in order, from an animated image. `ImageSequence.Iterator(img)` — each frame is a regular `Image` object, so every operation covered on this page (resize, filter, draw) works on it the same way. `.tell()` reports which frame number you're currently on, useful for numbering saved output files.

```python-ref
for frame in ImageSequence.Iterator(gif):
    print(frame.tell(), frame.size)   # frame index, then its size
```

```python-ref
from PIL import Image, ImageSequence

gif = Image.open("snake_slither.gif")
for frame in ImageSequence.Iterator(gif):
    print(frame.tell(), frame.size)
    frame.save(f"frame_{frame.tell()}.png")
```

## Putting it together

Pillow doesn't need anything special to combine with the rest of Python — a function wrapping one transformation, called from an `if`/`elif` chosen by [user input](../conditionals.md), looped until the user's done, is enough to build a small interactive tool out of the operations above.

```python-ref
def apply_filter(img, choice):
    if choice == "blur":
        return img.filter(ImageFilter.BLUR)
    elif choice == "grayscale":
        return img.convert("L")
    elif choice == "sharpen":
        return img.filter(ImageFilter.SHARPEN)
    else:
        return img
```

### An interactive filter tool

Combines a function, an `if`/`elif` chain, and a `while` loop — nothing here is Pillow-specific. Each piece here is something covered elsewhere on this site — a [function](../functions.md) wrapping one transformation, an [`if`/`elif` chain](../conditionals.md) picking which one to run, and a [`while` loop](../loops.md#while-loops) that keeps asking until the user's satisfied. Pillow itself only shows up inside `apply_filter`.

```python-ref
while True:
    choice = input("filter (blur/grayscale/sharpen/done): ")
    if choice == "done":
        break
    result = apply_filter(img, choice)
    result.save(f"{choice}.jpg")
    print(f"saved {choice}.jpg")
```

```python-ref
from PIL import Image, ImageFilter


def apply_filter(img, choice):
    if choice == "blur":
        return img.filter(ImageFilter.BLUR)
    elif choice == "grayscale":
        return img.convert("L")
    elif choice == "sharpen":
        return img.filter(ImageFilter.SHARPEN)
    else:
        return img

img = Image.open("snake.jpg")

while True:
    choice = input("filter (blur/grayscale/sharpen/done): ")
    if choice == "done":
        break
    result = apply_filter(img, choice)
    result.save(f"{choice}.jpg")
    print(f"saved {choice}.jpg")
```
