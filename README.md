# Collatz Conjecture Visualizer & Data Exporter
A high-caliber Python tool that explores the $3n + 1$ problem while providing options of further data analysis and visualization.


Inspired by:
*[The Simplest Math Problem No One Can Solve - Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg)* by [Veritasium on YouTube](https://www.youtube.com/@veritasium)

---

#### Note: entered numbers lose precision as they become more unspeakably high
#### To test unspeakably high numbers accurately or see the Research behind this project: *[Click Here](https://github.com/Skayyali3/Collatz_Research)*

---

## Features
- Algorithmic Calculation: Fast processing of the Collatz sequence for any integer, positive or negative

- Interactive Visualization: Generates dynamic line graphs using Matplotlib to show the hailstone peaks and valleys.

- Data Export: Utilizes Pandas to serialize sequence data into a `.csv` file for external analysis in Excel or SQL.

- Adaptive Logarithmic Scaling: Automatically switches to $Log_{10}$ visualization for unspeakably high numbers to prevent hardware overflow and maintain graph readability.

- Loop Detection using Floyd's Algorithm

---

## Technologies Used:
* Programming Language: *Python*

* Libraries Used: `Tkinter`, `Pandas` and `Matplolib`

* Concepts: Data Engineering pipelines, State Management and Mathematical Modeling.

---

## How to Run:
Follow these steps to run the project locally:

### 1. Clone the repository and enter:
```bash
git clone https://github.com/Skayyali3/CollatzStandard.git
cd CollatzStandard
```

### 2. Make a virtual environment
```bash
python -m venv venv

source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

### 3. Install the needed requirements
```bash
pip install -r requirements.txt
```

### 4. Run
```bash
python Collatz_Conjecture.py
```

## License

This project is licensed under the MIT License – see the **[license file](LICENSE)** for details.

## Author
**Saif Kayyali**
