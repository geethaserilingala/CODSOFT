import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.contact_listbox.grid(row=0, column=2, rowspan=10, padx=10, pady=5, sticky=tk.NSEW)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)

        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)
        self.exit_button.grid(row=9, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.update_listbox()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join([f"{contact['Name']} - {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        keyword = self.name_entry.get()
        results = [contact for contact in self.contacts if keyword.lower() in contact["Name"].lower()]
        if results:
            contact_list = "\n".join([f"{contact['Name']} - {contact['Phone']}" for contact in results])
            messagebox.showinfo("Search Results", contact_list)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            old_contact = self.contacts[selected_index]

            name = self.name_entry.get() or old_contact["Name"]
            phone = self.phone_entry.get() or old_contact["Phone"]
            email = self.email_entry.get() or old_contact["Email"]
            address = self.address_entry.get() or old_contact["Address"]

            new_contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts[selected_index] = new_contact
            self.update_listbox()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.contacts[selected_index]
            self.update_listbox()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Error", "Please select a contact to delete.")

    def update_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
