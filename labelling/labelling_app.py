import os
import random
import tkinter as tk

import yaml
from PIL import Image, ImageTk

output_file = "labels.yaml"


def get_files(file_path: str):
    files = []
    for root, dirs, filenames in os.walk(file_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    print(f"Found {len(files)} files.")
    return files


def get_random_from_list(lst):
    return lst[random.randint(0, len(lst) - 1)]


def save_label(file_name, label):
    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            data = yaml.safe_load(f)
            if data is None:
                data = {"labels": []}
            elif "labels" not in data:
                data["labels"] = []
    else:
        data = {"labels": []}

    data["labels"].append({"file": file_name, "label": label})

    with open(output_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False)

    print(
        f"Total images: {len(data['labels'])}\nSaved label '{label}' for file '{file_name}'."
    )


class LabelingApp:
    def __init__(self, master, file_path):
        self.master = master
        self.master.title("File Labeling App")
        self.image_directory = file_path

        # vaildate the path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Path '{file_path}' does not exist.")

        self.current_file = None
        self.current_index = 0
        files = [
            os.path.basename(f) for f in get_files(file_path) if f.endswith(".png")
        ]
        self.file_list = files

        # Label showing current file
        self.file_label = tk.Label(master, text="", font=("Arial", 16))
        self.file_label.pack(pady=20)

        # Image display area (self.image_label defined here)
        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        # Buttons for labeling
        self.button_0 = tk.Button(
            master,
            text="Horizontal Polarisation",
            command=self.label_0,
            bg="red",
            font=("Arial", 14),
        )
        self.button_0.pack(side=tk.LEFT, padx=20, pady=20)

        self.button_1 = tk.Button(
            master,
            text="Vertical Polarisation",
            command=self.label_1,
            bg="green",
            font=("Arial", 14),
        )
        self.button_1.pack(side=tk.RIGHT, padx=20, pady=20)

        self.button_2 = tk.Button(
            master,
            text="No Observable Polarisation",
            command=self.label_2,
            bg="green",
            font=("Arial", 14),
        )
        self.button_2.pack(side=tk.RIGHT, padx=20, pady=20)

        self.button_3 = tk.Button(
            master,
            text="Mixed H/V",
            command=self.label_3,
            bg="blue",
            font=("Arial", 14),
        )
        self.button_3.pack(side=tk.BOTTOM, padx=20, pady=20)

        # Load first file
        self.load_file()

    def __len__(self):
        return len(self.file_list)

    def load_file(self):
        if os.path.exists(output_file):
            with open(output_file, "r") as f:
                data = yaml.safe_load(f) or {"labels": []}
        else:
            data = {"labels": []}

        # Ensure that 'labels' is always a list
        if "labels" not in data or not isinstance(data["labels"], list):
            data["labels"] = []

        # Get the set of already labeled files
        labeled_files = {entry["file"] for entry in data["labels"]}

        unlabeled_files = [f for f in self.file_list if f not in labeled_files]

        if unlabeled_files:
            selected_file = random.choice(unlabeled_files)
            self.current_file = selected_file

            self.file_label.config(text=f"Current file: {selected_file}")

            # Load and display the image
            img_path = os.path.join(self.image_directory, selected_file)
            img = Image.open(img_path).convert("L")
            photo = ImageTk.PhotoImage(img)

            self.image_label.config(image=photo)  # type: ignore
            self.image_label.image = photo  # type: ignore

        else:
            self.file_label.config(text="All files labeled!")
            self.image_label.config(image="")
            self.button_0.config(state=tk.DISABLED)
            self.button_1.config(state=tk.DISABLED)
            self.button_2.config(state=tk.DISABLED)
            self.button_3.config(state=tk.DISABLED)
            # shut down app
            print("All files labeled. Shutting down.")
            self.master.quit()

    def label_0(self):
        if self.current_file:
            save_label(self.current_file, "horizontal")
            self.load_file()

    def label_1(self):
        if self.current_file:
            save_label(self.current_file, "vertical")
            self.load_file()

    def label_2(self):
        if self.current_file:
            save_label(self.current_file, "na")
            self.load_file()

    def label_3(self):
        if self.current_file:
            save_label(self.current_file, "mixed_hv")
            self.load_file()


if __name__ == "__main__":
    # Create the GUI
    root = tk.Tk()
    app = LabelingApp(
        root,
        r"../../../../../../../../Volumes/T7\ Shield/Diffraction_SI_averaged_images",
    )
    print(f"Loaded {len(app)} files.")
    root.mainloop()
