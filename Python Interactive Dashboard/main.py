import streamlit as st
import pandas as pd

st.title("Interactive Python Data Explorer")

st.sidebar.header("Configuration")
data_type_option = st.sidebar.selectbox(
     "Select Data Type to Explore",
     ["Variables & Data Types", "Control Flow & Loops", "Lambda & Higher-Order Functions", "File Handling"]
)

if data_type_option == "Variables & Data Types":
    st.header("Variables & Data Types")
    var_name = st.text_input("Variable Name", value="my_string")
    var_value = st.text_input("Variable Value", value="Hello World")
    
    if var_name and var_value:
        code = f"{var_name} = {repr(var_value)}"
        exec(code)
        st.code(code, language='python')
        st.write(f"**Variable `{var_name}` set to:**")
        st.write(globals()[var_name])
        
    data_obj = {"String": "Hello", "List": [1, 2, 3], "Tuple": (4, 5), "Set": {6, 7}, "Dictionary": {"a": 1}}
    st.subheader("Sample Data Types")
    for name, obj in data_obj.items():
        st.write(f"**{name}:**")
        st.write(obj)
        st.write(f"Type: {type(obj)}")
        st.markdown("---")

elif data_type_option == "Control Flow & Loops":
    st.header("Control Flow & Loops")
    condition = st.text_input("Enter a number for condition check", value="5")
    
    try:
        num = int(condition)

        st.write("### If/Elif/Else Example")
        if num > 10:
            st.write(f"{num} is greater than 10.")
        elif num == 10:
            st.write(f"{num} is equal to 10.")
        else:
            st.write(f"{num} is less than 10.")
                
        st.write("### For Loop Example (List of numbers)")
        numbers = list(range(1, num+1))
        for i in numbers:
            st.write(i)
        
        st.write("### While Loop (Countdown)")
        counter = num
        countdown = []
        while counter > 0:
            countdown.append(counter)
            counter -= 1
        st.write(countdown)
    
    except ValueError:
        st.error("Please enter a valid integer.")

elif data_type_option == "Lambda & Higher-Order Functions":
    st.header("Lambda & Higher-Order Functions")
    list_input = st.text_input("Enter a list of numbers (comma separated)", value="1,2,3,4,5")
    try:
        user_list = list(map(int, list_input.split(',')))
        st.write("Original List:", user_list)
        
        squared = list(map(lambda x: x**2, user_list))
        st.write("Squared List:", squared)
        
        even_numbers = list(filter(lambda x: x % 2 == 0, user_list))
        st.write("Even Numbers:", even_numbers)
        
        def add_one(x):
            return x + 1
        incremented = list(map(add_one, user_list))
        st.write("Incremented List:", incremented)
        
    except Exception as e:
        st.error(f"Error processing list: {e}")

elif data_type_option == "File Handling":
    st.header("File Handling")
    uploaded_file = st.file_uploader("Upload a text file", type=["txt", "csv"])
    if uploaded_file:        
        file_content = uploaded_file.read()
        try:
            text_content = file_content.decode("utf-8")
            st.write("File Content:")
            st.text_area("Content", text_content, height=300)
        except:
            st.write("Binary file uploaded, cannot display text.")
                
        save_path = st.text_input("Enter path to save uploaded file (optional)", value="uploaded_file.txt")
        if st.button("Save File"):
            try:
                with open(save_path, "wb") as f:
                    f.write(file_content)
                st.success(f"File saved to {save_path}")
            except Exception as e:
                st.error(f"Error saving file: {e}")

