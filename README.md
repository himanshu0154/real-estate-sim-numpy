# real-estate-sim-numpy

Welcome to **real-estate-sim-numpy**, a Python-powered real estate price simulator and interactive CLI application built with NumPy! This project allows you to explore, analyze, and interact with a dataset of 100 houses with realistic price modifications like inflation and market crashes.

---

## About

This tool was created by **himanshu0154** as part of a project to practice Python, NumPy, and data handling skills. It generates random house data including prices, sizes, bedrooms, and ages, then applies dynamic changes to prices to simulate real-world market conditions.

---

## Features

- Generate data for 100 houses with attributes: price, square footage, bedrooms, and age.
- Apply inflation (6%) and renovation costs (10% increase if house age > 20 years).
- Simulate market crashes by randomly reducing prices of 5 houses by 20%.
- Display lists of houses sorted by price, price per square foot (best/worst deals), age (youngest/oldest).
- Calculate average prices and present detailed info on selected houses.
- Interactive menu-driven command line interface for easy navigation.

---

## Getting Started

### Prerequisites

- Python 3.6+
- NumPy library

Install NumPy if you don’t have it yet:

```bash
pip install numpy
```

## Running the Project

### Clone the repository:

```bash
git clone https://github.com/himanshu0154/real-estate-sim-numpy.git
cd real-estate-sim-numpy
```

Run the main program:

```bash
python main.py
```

Follow the on-screen menu to explore the houses and interact with the data.

---

# Usage

When you run the program, you’ll see a menu with options like:

- Show original or modified house prices

- View most expensive or cheapest houses

- Find best or worst deals based on price per square foot

- List oldest or youngest houses

- Calculate average house price

Simply enter the number corresponding to your choice and follow prompts.

---

# Code Structure

- main.py — The main script containing the full application logic.

- Uses NumPy for efficient data generation, manipulation, and sorting.

---

# Future Enhancements

- Add filtering options by bedrooms, price range, or age.

- Integrate machine learning models to predict house prices.

- Develop a graphical user interface (GUI) for improved user experience.

---

# Author

Himanshu
GitHub: **himanshu0154**

---

# License

This project is open-source and free to use under the MIT License.

Feel free to reach out if you want to collaborate or have any questions!

