# Python Learning Projects Repository

Welcome to the Python Learning Projects repository! This collection contains three beginner-to-intermediate Python web projects covering essential topics from general Python programming, use of modern web frameworks, object-oriented design, and file handling.

Each project is organized in its own directory, with setup instructions and code for quick hands-on experimentation.

---

## Repository Structure

```
/
├── streamlit-data-explorer/
├── streamlit-module-explorer/
├── flask-oop-file-manager/
├── README.md
```

---

## Projects

### 1. Streamlit Interactive Python Data Explorer

**Path:** `streamlit-data-explorer/`  
**Description:**  
A Streamlit app for exploring Python data types, control flow, lambda functions, and file handling interactively.

**Features:**

- Demonstrate and experiment with strings, lists, sets, tuples, and dictionaries.
- Experiment with control flow (`if/else`, loops).
- Try map/filter/lambda functions.
- Upload text files and display their contents.

**Getting Started:**

```
cd streamlit-data-explorer
pip install -r requirements.txt
streamlit run streamlit_python_explorer.py
```

---

### 2. Streamlit Python Module Function Explorer

**Path:** `streamlit-module-explorer/`  
**Description:**  
A Streamlit app to explore Python functions, lambdas, argument handling, built-in modules, namespaces, and higher-order functions.

**Features:**

- Input and run Python functions and lambdas.
- Use `help()` and `dir()` to view documentation for Python modules (`math`, `random`, `datetime`, `os`).
- Visualize variable namespaces and scope dynamically.
- See demonstrations of higher order function patterns.

**Getting Started:**

```
cd streamlit-module-explorer
pip install -r requirements.txt
streamlit run streamlit_module_explorer.py
```

---

### 3. Flask OOP and File Management Mini App

**Path:** `flask-oop-file-manager/`  
**Description:**  
A Flask web app showcasing object-oriented programming (OOP) concepts (inheritance, encapsulation, polymorphism) and robust file upload/read with error handling.

**Features:**

- Create and manage Python objects using OOP concepts.
- Demonstrate inheritance and method overriding.
- Upload `.txt`/`.csv` files, view and manage their content.
- Handle errors gracefully and provide user feedback.

**Getting Started:**

```
cd flask-oop-file-manager
pip install -r requirements.txt
python flask_oop_file_app.py
```

App runs at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## How to Use This Repository

- Each project is **independent**—use them as learning modules or prototypes for classroom/lab use.
- Clone this repo and explore each folder for code, templates, and instructions.
- Customize or extend with your own Python concepts or datasets.

## Contribution

Pull requests and issues are welcome for improvements, bugfixes, and extensions, especially for new Python pedagogy modules or UI/UX enhancements.
