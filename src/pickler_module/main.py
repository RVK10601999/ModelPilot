import streamlit as st
import tkinter as tk
from tkinter import filedialog
import pickle as pkl

def app(model):
    st.header('Page 4 - Model Exporting Suite', divider="blue")    
    root = tk.Tk()
    file_path = filedialog.asksaveasfilename(defaultextension=".pkl", 
                                            filetypes=[("Pickle files", "*.pkl"), ("All files", "*.*")],
                                            title="Save model")
    if file_path:
        with open(file_path, 'wb') as file:
            pkl.dump(model, file)
        st.write(f"Model saved to {file_path}")
    else:
        st.write("Save cancelled.")