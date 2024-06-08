import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def encrypt_image():
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[('JPEG files', '*.jpg;*.jpeg')])
        if file_path:
            key = entry_key.get("1.0", "end-1c")  # Get key from the entry field
            with open(file_path, 'rb') as file:
                image_data = bytearray(file.read())
                for index, value in enumerate(image_data):
                    image_data[index] = value ^ int(key)  # XOR encryption
            with open(file_path, 'wb') as file:
                file.write(image_data)
            messagebox.showinfo("Success", "Image encrypted successfully.")
        else:
            messagebox.showwarning("Warning", "No file selected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.geometry("300x150")
root.title("Simple Image Encryption Tool")

# Create widgets
button_encrypt = tk.Button(root, text="Encrypt Image", command=encrypt_image)
button_encrypt.pack(pady=10)

label_key = tk.Label(root, text="Enter Encryption Key:")
label_key.pack()

entry_key = tk.Text(root, height=1, width=20)
entry_key.pack()

# Run the application
root.mainloop()
