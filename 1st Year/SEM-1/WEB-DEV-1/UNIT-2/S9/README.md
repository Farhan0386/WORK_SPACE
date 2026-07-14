
# 🎨 CSS Session 1– Full Reference Guide (Web Development-I)

This README is a complete summary of Lecture 9: Introduction to CSS

---

## 📘 What is CSS?

**CSS (Cascading Style Sheets)** is a language used to style HTML documents. It defines how elements should appear on the screen, including:

- Colors
- Fonts
- Layouts
- Spacing
- Borders
- Positioning

Without CSS, websites would look like plain, unstyled text—boring and hard to navigate. CSS makes websites attractive, readable, and user-friendly.

---

## 🧱 CSS Syntax

```css
selector {
  property: value;
}
```

### 🔹 Terms Explained

- **Selector**: Targets the HTML element (e.g., `p`, `h1`, `.class`, `#id`)
- **Property**: The style you want to apply (e.g., `color`, `font-size`)
- **Value**: The setting for that property (e.g., `red`, `20px`)

### 🔹 Example

```css
p {
  color: red;
  font-size: 18px;
}
```

This will style all `<p>` tags with red text and 18px font size.

---

## 🧩 Types of CSS

### 1. Inline CSS

- Written directly inside the HTML tag using the `style` attribute.
- Highest priority.
- Not reusable.
- Best for quick fixes or testing.

**Example:**

```html
<p style="color: navy; font-size: 22px;">This is inline CSS.</p>
```

---

### 2. Internal CSS

- Written inside a `<style>` tag within the `<head>` section of the HTML file.
- Medium priority.
- Limited reuse.
- Good for small projects or demos.

**Example:**

```html
<head>
  <style>
    h1 {
      color: purple;
    }
    p {
      color: gray;
    }
  </style>
</head>
```

---

### 3. External CSS

- Written in a separate `.css` file and linked to the HTML page.
- Lowest priority.
- Highly reusable.
- Best for large, multi-page websites.

**HTML:**

```html
<link rel="stylesheet" href="style.css">
```

**style.css:**

```css
p {
  color: red;
  font-size: 22px;
}
```

---

## ⚖️ CSS Priority Rules (Specificity)

| Type        | Priority Level |
|-------------|----------------|
| Inline      | Highest        |
| Internal    | Medium         |
| External    | Lowest         |

> ✅ Inline styles override internal and external styles.  
> ✅ Internal styles override external styles.  
> ✅ External styles are best for maintainability.

---

## 🆔 ID vs. 🏷️ Class

### 🔹 ID

- Uniquely identifies one element.
- Use `#idname` in CSS.
- Higher specificity.

**Example:**

```html
<p id="intro">Welcome!</p>
```

```css
#intro {
  color: blue;
}
```

---

### 🔹 Class

- Can be used on multiple elements.
- Use `.classname` in CSS.
- Ideal for grouping and reusing styles.

**Example:**

```html
<p class="highlight">First</p>
<p class="highlight">Second</p>
```

```css
.highlight {
  color: green;
}
```

---

## 🧱 The `<div>` Tag

- A **block-level container** used to group HTML elements.
- Helps organize layout and apply styles.
- Can be styled using `class` or `id`.

**Example:**

```html
<div class="box">
  <h1>Heading</h1>
  <p>Paragraph inside div</p>
</div>
```

```css
.box {
  background-color: lightgray;
  color: darkblue;
}
```

> ✅ If you apply `color` to a `<div>`, all text inside inherits that color unless overridden.

---
