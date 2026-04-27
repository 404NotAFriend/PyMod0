<div align="center">

*This project has been created as part of the 42 curriculum by bramalho*

# 🌱 PyMod0 - Growing Code

<img src="https://img.shields.io/badge/Circle-0-00BABC?style=for-the-badge&logo=42&logoColor=white"/>
<img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/42-Porto-000000?style=for-the-badge&logo=42&logoColor=white"/>
<img src="https://img.shields.io/badge/Exercises-8-success?style=for-the-badge"/>

**Your first steps into Python — where code grows like a garden! 🌿**

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="600"/>

</div>

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Light%20Bulb.png" width="25"/> About The Project

**PyMod0** is the very beginning of your Python journey at 42! This module introduces the **core building blocks** of programming using a fun gardening theme — because just like plants, code needs the right foundations to grow.

Through 8 exercises you'll learn:
- 🖨️ **Output** — printing to the terminal
- ⌨️ **Input** — reading data from the user
- 🔢 **Variables & types** — integers, strings, and more
- ➕ **Arithmetic operations** — doing math with code
- 🔀 **Conditionals** — making decisions with `if/else`
- 🔁 **Loops** — repeating actions iteratively and recursively
- 🏷️ **Type hints** — writing cleaner, more readable functions

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" width="25"/> Exercises

| # | File | Concepts | Description |
|---|------|----------|-------------|
| ex0 | `ft_hello_garden.py` | `print()` | Say hello to the Garden Community |
| ex1 | `ft_garden_name.py` | `input()`, f-strings | Read and display a garden name |
| ex2 | `ft_plot_area.py` | `int()`, arithmetic | Calculate plot area from length × width |
| ex3 | `ft_harvest_total.py` | variables, `+` operator | Sum 3 days of harvest weights |
| ex4 | `ft_plant_age.py` | `if/else` | Check if a plant is ready to harvest |
| ex5 | `ft_water_reminder.py` | conditionals | Decide if plants need watering |
| ex6 | `ft_count_harvest_iterative.py` + `ft_count_harvest_recursive.py` | `for` loop, recursion | Count days to harvest — two ways |
| ex7 | `ft_seed_inventory.py` | type hints, `elif` | Display seed inventory by unit type |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" width="25"/> Technical Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-000000?style=for-the-badge&logo=gnu-bash&logoColor=white)

No external libraries — pure Python 3, standard input/output only.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/File%20Folder.png" width="25"/> Project Structure

```
PyMod0/
├── main.py                              # Test runner — run all exercises here
├── ex0/
│   └── ft_hello_garden.py              # Print "Hello, Garden Community!"
├── ex1/
│   └── ft_garden_name.py               # Read & display garden name
├── ex2/
│   └── ft_plot_area.py                 # Calculate plot area
├── ex3/
│   └── ft_harvest_total.py             # Sum 3-day harvest
├── ex4/
│   └── ft_plant_age.py                 # Check if plant is ready
├── ex5/
│   └── ft_water_reminder.py            # Watering reminder
├── ex6/
│   ├── ft_count_harvest_iterative.py   # Count days with a loop
│   └── ft_count_harvest_recursive.py  # Count days with recursion
└── ex7/
    └── ft_seed_inventory.py            # Seed inventory with type hints
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" width="25"/> Getting Started

### Prerequisites

- Python 3 installed (`python3 --version`)
- No pip packages needed

### Clone & Run

```bash
# Clone the repository
git clone https://github.com/404NotAFriend/PyMod0.git
cd PyMod0

# Launch the interactive test runner
python3 main.py
```

### Test Runner Menu

```
🌱 Welcome to Growing Code! 🌱

0 - ft_hello_garden     (Say hello to the garden community)
1 - ft_garden_name      (Display garden name)
2 - ft_plot_area        (Calculate garden plot area)
3 - ft_harvest_total    (Add up harvest weights)
4 - ft_plant_age        (Check if plant is ready)
5 - ft_water_reminder   (Check if plants need water)
6 - ft_count_harvest    (Count days to harvest)
7 - ft_seed_inventory   (Seed inventory with type hints)
a - test all exercises

Enter your choice:
```

### Run a Single Exercise Directly

```bash
python3 -c "import sys; sys.path.insert(0, 'ex2'); from ft_plot_area import ft_plot_area; ft_plot_area()"
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Memo.png" width="25"/> Key Concepts Explained

### ex0 — Hello Garden
```python
def ft_hello_garden():
    print("Hello, Garden Community!")
```
Your very first Python function! `print()` outputs text to the terminal.

---

### ex2 — Plot Area (Arithmetic)
```python
length = int(input("Enter length:"))
width = int(input("Enter width:"))
area = length * width
print(f"Plot area: {area}")
```
`input()` always returns a string — `int()` converts it to a number you can do math with.

---

### ex4 & ex5 — Conditionals
```python
if age > 60:
    print("Plant is ready to harvest!")
else:
    print("Plant needs more time to grow.")
```
`if/else` lets your program make decisions based on conditions.

---

### ex6 — Two Ways to Loop

**Iterative (with `for`):**
```python
for i in range(1, days + 1):
    print(f"Day {i}")
```

**Recursive (function calling itself):**
```python
def counter(current, limit):
    if current > limit:
        return
    print(f"Day {current}")
    counter(current + 1, limit)
```
Same result, two different mindsets — both are valid approaches!

---

### ex7 — Type Hints
```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```
Type hints (`str`, `int`, `-> None`) don't change how the code runs, but they make it **much easier to read and maintain**. Get used to them early!

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Pushpin.png" width="25"/> Common Pitfalls

| ❌ Issue | ✅ Solution |
|---------|------------|
| `TypeError: can't add int and str` | Wrap `input()` with `int()` before arithmetic |
| Function not found in test runner | Make sure the filename matches the function name exactly |
| `IndentationError` | Python uses indentation instead of `{}` — be consistent (4 spaces) |
| `RecursionError` | Your base case is missing or never reached — check the `if` in the recursive function |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Star-Struck.png" width="25"/> What's Next?

After mastering PyMod0, you'll move on to:
- 🐍 **PyMod1** — Lists, dictionaries, and file I/O
- 🔧 **PyMod2** — Object-oriented programming
- 📊 **Data Science** modules — NumPy, Pandas, and beyond
- 🤖 **ML/AI** modules — the future of the 42 curriculum!

Python is the language of data science, AI, automation, and the web — you're in the right place!

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Link.png" width="25"/> Resources

- [Python 3 Official Docs](https://docs.python.org/3/)
- [Python `input()` and `print()`](https://docs.python.org/3/library/functions.html#input)
- [Type Hints — PEP 484](https://peps.python.org/pep-0484/)
- [Recursion Explained](https://realpython.com/python-recursion/)
- [42 Intranet](https://intra.42.fr)

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Mobile%20Phone.png" width="25"/> Contact

**Bruno Gomes** — 42 Porto Student

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:brunodrcgomes@gmail.com)
[!https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Nature/Herb.png[LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/meetbrunogomes/)
[![42](https://img.shields.io/badge/42-000000?style=for-the-badge&logo=42&logoColor=white)](https://profile.intra.42.fr/users/bramalho)

---

<div align="center">

### 💡 Pro Tips from Development

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Nerd%20Face.png" width="20"/> **Read the error message** — Python error messages are surprisingly helpful

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Hot%20Beverage.png" width="20"/> **Test one function at a time** — Use `main.py` to isolate issues

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Star-Struck.png" width="20"/> **Type hints from day one** — Build the habit early, thank yourself later

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Smiling%20Face%20with%20Sunglasses.png" width="20"/> **Understand both loops** — Iterative and recursive both matter at 42

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Exploding%20Head.png" width="20"/> **`int(input())` is your best friend** — You'll type this a thousand times

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer"/>

**Thanks for checking out PyMod0! From `print("Hello")` to Python mastery — one line at a time.** 🌱

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" width="40"/>

*"First make it work. Then make it beautiful. Then make it grow."*

### 💻 Built with dedication at 42 School Porto

</div>
