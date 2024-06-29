import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        # Dictionary to store contacts
        self.contacts = {}

        # Create and pack GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for contact details
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone = tk.Label(self.root, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_address = tk.Label(self.root, text="Address:")
        self.label_address.grid(row=3, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(self.root)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for actions
        self.button_add = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, column=0, padx=10, pady=10)

        self.button_view = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.button_view.grid(row=4, column=1, padx=10, pady=10)

        self.label_search = tk.Label(self.root, text="Search:")
        self.label_search.grid(row=5, column=0, padx=10, pady=5)
        self.entry_search = tk.Entry(self.root)
        self.entry_search.grid(row=5, column=1, padx=10, pady=5)

        self.button_search = tk.Button(self.root, text="Search", command=self.search_contact)
        self.button_search.grid(row=6, column=0, padx=10, pady=10)

        self.button_update = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.button_update.grid(row=6, column=1, padx=10, pady=10)

        self.button_delete = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Text area for displaying contact details
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone fields are required.")

    def view_contacts(self):
        self.text_area.delete(1.0, tk.END)
        if not self.contacts:
            self.text_area.insert(tk.END, "No contacts found.")
        else:
            for name, info in self.contacts.items():
                self.text_area.insert(tk.END, f"Name: {name}\n")
                self.text_area.insert(tk.END, f"Phone: {info['phone']}\n")
                self.text_area.insert(tk.END, f"Email: {info['email']}\n")
                self.text_area.insert(tk.END, f"Address: {info['address']}\n")
                self.text_area.insert(tk.END, "-------------------------\n")

    def search_contact(self):
        search_key = self.entry_search.get().lower()
        self.text_area.delete(1.0, tk.END)
        found = False
        for name, info in self.contacts.items():
            if search_key in name.lower() or search_key in info['phone']:
                self.text_area.insert(tk.END, f"Name: {name}\n")
                self.text_area.insert(tk.END, f"Phone: {info['phone']}\n")
                self.text_area.insert(tk.END, f"Email: {info['email']}\n")
                self.text_area.insert(tk.END, f"Address: {info['address']}\n")
                self.text_area.insert(tk.END, "-------------------------\n")
                found = True
        if not found:
            self.text_area.insert(tk.END, f"No contacts found for '{search_key}'.")

    def update_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"Contact '{name}' not found.")

    def delete_contact(self):
        name = self.entry_name.get()

        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"Contact '{name}' not found.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_search.delete(0, tk.END)
        self.text_area.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
