# 🎨 CSS Session 2 – Colors & Fonts in CSS (Lecture 10)

This README is a complete reference guide for **Lecture 10: Colors & Fonts in CSS** from Web Development-I . It explains how colors and fonts are used in CSS to make websites visually appealing, brand-consistent, and user-friendly.

---

## 📘 Why Colors & Fonts Matter

- Imagine Instagram without its vibrant pink-orange gradient—it wouldn’t feel the same.
- Colors bring **life, identity, and emotion** to a website.
- Fonts define **brand identity, readability, and uniqueness**.
- Together, they make interfaces attractive, guide user attention, and build recognition.

---

## 🎨 Colors in CSS

CSS allows you to add colors to:

- Text (`color`)
- Backgrounds (`background-color`)
- Borders, buttons, hover effects
- Improve readability & accessibility
- Reflect brand personality

---

## 🧩 Color Formats in CSS

CSS supports multiple formats for defining colors:

1. **HEX (Hexadecimal)**
2. **RGB (Red, Green, Blue)**
3. **RGBA (RGB + Alpha for transparency)**
4. **HSL (Hue, Saturation, Lightness)**

---

### 1️⃣ HEX (Hexadecimal)

- Uses a 6-digit code: `#RRGGBB`
- Each pair ranges from `00` to `FF` (0–255 in decimal).
- Syntax:

  ```css
  color: #RRGGBB;
  ```

**Examples:**

```css
color: #FF0000; /* Red */
color: #00FF00; /* Green */
color: #0000FF; /* Blue */
color: #000000; /* Black */
color: #FFFFFF; /* White */
color: #FF5733; /* Custom Orange */
```

**Program Example:**

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    h1 { color: #FF5733; } /* Orange-red */
    p  { color: #555555; } /* Dark gray */
  </style>
</head>
<body>
  <h1>Hello CSS Colors!</h1>
  <p>This text uses hex color codes.</p>
</body>
</html>
```

---

### 2️⃣ RGB (Red, Green, Blue)

- Defines colors by mixing red, green, and blue values.
- Range: `0–255` for each channel.
- Syntax:

  ```css
  color: rgb(R, G, B);
  ```

**Examples:**

```css
color: rgb(255, 0, 0);   /* Red */
color: rgb(0, 255, 0);   /* Green */
color: rgb(0, 0, 255);   /* Blue */
color: rgb(255, 255, 0); /* Yellow */
color: rgb(0, 0, 0);     /* Black */
color: rgb(255, 255, 255); /* White */
```

**Program Example:**

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    h1 { color: rgb(255, 87, 51); } /* Orange-red */
    p  { color: rgb(85, 85, 85); }  /* Dark gray */
  </style>
</head>
<body>
  <h1>Hello CSS Colors!</h1>
  <p>This text uses RGB color codes.</p>
</body>
</html>
```

---

### 3️⃣ RGBA (Red, Green, Blue, Alpha)

- Adds an **Alpha channel** for transparency.
- Alpha ranges from `0.0` (transparent) to `1.0` (opaque).
- Syntax:

  ```css
  color: rgba(R, G, B, A);
  ```

**Examples:**

```css
color: rgba(0, 255, 0, 0.7);   /* Semi-transparent green */
color: rgba(0, 0, 255, 0.3);   /* Light transparent blue */
color: rgba(255, 255, 0, 0.6); /* Semi-transparent yellow */
color: rgba(255, 165, 0, 0.8); /* Semi-transparent orange */
color: rgba(128, 0, 128, 0.4); /* Transparent purple */
color: rgba(0, 0, 0, 0.2);     /* Very light black */
```

**Program Example:**

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .box {
      width: 100px;
      height: 100px;
      margin: 10px;
      display: inline-block;
    }
    .red    { background: rgba(255, 0, 0, 0.2); }
    .green  { background: rgba(0, 255, 0, 0.5); }
    .yellow { background: rgba(255, 255, 0, 0.8); }
    .blue   { background: rgba(0, 0, 255, 1); }
  </style>
</head>
<body>
  <div class="box red"></div>
  <div class="box green"></div>
  <div class="box yellow"></div>
  <div class="box blue"></div>
</body>
</html>
```

---

### 4️⃣ HSL (Hue, Saturation, Lightness)

- **Hue**: Type of color (0–360° on color wheel).
- **Saturation**: Intensity (0% = gray, 100% = full color).
- **Lightness**: Brightness (0% = black, 100% = white).
- Syntax:

  ```css
  color: hsl(hue, saturation, lightness);
  ```

**Examples:**

```css
color: hsl(0, 100%, 50%);   /* Bright Red */
color: hsl(120, 100%, 50%); /* Bright Green */
color: hsl(240, 100%, 50%); /* Bright Blue */
color: hsl(60, 100%, 50%);  /* Bright Yellow */
color: hsl(200, 80%, 60%);  /* Soft Blue */
color: hsl(340, 80%, 70%);  /* Light Pinkish Red */
```

**Program Example:**

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    h1 { color: hsl(210, 100%, 40%); } /* Deep blue */
    p  { color: hsl(0, 0%, 40%); }     /* Gray */
  </style>
</head>
<body>
  <h1>Hello HSL Colors!</h1>
  <p>This text uses HSL color codes.</p>
</body>
</html>
```

---

## 🔤 Fonts in CSS

Fonts are critical for **brand identity, readability, and uniqueness**.

### 1️⃣ Google Fonts

- Free library of 1,400+ fonts hosted by Google.
- Easy to integrate with `<link>` tag.
- Lightweight and fast.

**Steps:**

1. Visit [Google Fonts](https://fonts.google.com).
2. Choose a font (e.g., Poppins).
3. Copy the `<link>` tag:

   ```html
   <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
   ```

4. Apply in CSS:

   ```css
   body {
     font-family: 'Poppins', sans-serif;
   }
   ```

**Complete Example:**

```html
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Poppins', sans-serif; }
  </style>
</head>
<body>
  <h1>Hello Google Fonts!</h1>
  <p>This text uses the Poppins font from Google Fonts.</p>
</body>
</html>
```

---

### 2️⃣ Custom Fonts

- Manually added to your project.
- Used for branded or premium fonts.
- Requires hosting font files (`.ttf`, `.woff`, `.woff2`).

**Steps:**

1. Download font files (e.g., from [fontsquirrel.com](https://www.fontsquirrel.com)).
2. Add font files to your project folder.
3. Define with `@font-face`:

   ```css
   @font-face {
     font-family: 'MyFont';
     src: url('fonts/MyFont.woff2') format('woff2');
     font-weight: normal;
     font-style: normal;
   }
   ```

4. Apply in CSS:

   ```css
   body {
     font-family: 'MyFont', sans-serif;
   }
   ```
