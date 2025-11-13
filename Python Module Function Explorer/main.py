import streamlit as st
import builtins
import math
import random
import datetime
import os

st.title("Python Module Function Explorer")

st.header("Input Python Code Snippet")

code_input = st.text_area(
    "Enter your Python function or lambda code here:",
    value=(
        "def square(x):\n"
        "    return x * x\n\n"
        "my_lambda = lambda y: y + 10"
    ),
    height=150,
)

run_code = st.button("Run Code")
if run_code:
    namespace = {}
    try:
        exec(code_input, namespace)
        st.success("Code executed successfully!")
        
        st.subheader("Namespace Variables and Values")
        for var, val in namespace.items():
            if var not in ("__builtins__",):
                st.write(f"- **{var}**: {val}")

    except Exception as e:
        st.error(f"Error executing code: {e}")

st.header("Explore Python Standard Modules")

modules = {
    "math": math,
    "random": random,
    "datetime": datetime,
    "os": os,
    "builtins": builtins
}
selected_module = st.selectbox("Select a module", list(modules.keys()))

if selected_module:
    mod = modules[selected_module]

    st.subheader(f"dir({selected_module})")
    mod_dir = dir(mod)
    st.write(mod_dir)

    if st.button(f"Show help for {selected_module}"):
        with st.spinner(f"Loading help for {selected_module}..."):
            import io
            import sys
            buffer = io.StringIO()
            sys.stdout = buffer
            try:
                help(mod)
            finally:
                sys.stdout = sys.__stdout__
            help_text = buffer.getvalue()
        st.text_area(f"Help Documentation for {selected_module}", help_text, height=400)

st.header("Manual Higher Order Function Example")

st.write(
    """Define a function that accepts another function and applies it to a list."""
)

hoc_code = """
def apply_func(func, lst):
    return [func(x) for x in lst]

def increment(x):
    return x + 1

numbers = [1, 2, 3, 4]
result = apply_func(increment, numbers)
"""

st.code(hoc_code, language='python')

if st.button("Run Higher Order Function Example"):
    def apply_func(func, lst):
        return [func(x) for x in lst]

    def increment(x):
        return x + 1

    numbers = [1, 2, 3, 4]
    result = apply_func(increment, numbers)
    st.write("Original list:", numbers)
    st.write("After applying increment function:", result)

st.header("Namespace and Scope Demonstration")

namespace = {}

code_ns = st.text_area(
    "Enter code snippet to run with shared namespace:",
    value=(
        "a = 5\n"
        "def foo():\n"
        "    b = 10\n"
        "    return a + b\n"
        "result = foo()"
    ),
    height=150,
)

if st.button("Run Namespace Code"):
    try:        
        exec(code_ns, namespace, namespace)
        st.success("Code executed.")        
        filtered_vars = {k: v for k, v in namespace.items() if not k.startswith("__")}
        st.write("Namespace variables and values:")
        st.write(filtered_vars)
    except Exception as e:
        st.error(f"Error executing code: {e}")

