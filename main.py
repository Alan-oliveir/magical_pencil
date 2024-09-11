import os
import logging
from tkinter import filedialog as fd, messagebox

import cv2
from PIL import Image, ImageTk
import customtkinter as ctk

# Constants
PATH = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = os.path.join(PATH, "output")

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.image_path = None
        self.scale_value = 256  # Default scale value
        self.geometry("380x424")
        self.title("Magical Pencil")

        # Define fonts
        font_title = ctk.CTkFont(family="Verdana", size=30, weight='bold')
        font_subtitle = ctk.CTkFont(family="Verdana", size=26, weight='bold')
        font_frame = ctk.CTkFont(family="Verdana", size=12, weight='bold')

        # Load default image
        default_image = ctk.CTkImage(light_image=Image.open(PATH + "/images/image.jpg"),
                                     dark_image=Image.open(PATH + "/images/image.jpg"),
                                     size=(225, 225))

        # Add widgets
        self.label_title = ctk.CTkLabel(self, text="Transformando", fg_color="transparent", width=360, height=20,
                                        font=font_title)
        self.label_title.grid(row=0, column=0, padx=10, pady=(10, 5))

        self.label_subtitle = ctk.CTkLabel(self, text="Foto em Desenho", fg_color="transparent", width=360, height=20,
                                           font=font_subtitle)
        self.label_subtitle.grid(row=1, column=0, padx=10, pady=(0, 5))

        self.image_label = ctk.CTkLabel(self, image=default_image, text="")
        self.image_label.grid(row=2, column=0, padx=10, pady=(10, 20))

        frame_configure = ctk.CTkFrame(self)
        frame_configure.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")

        self.label_config = ctk.CTkLabel(master=frame_configure, text="Configurações:", font=font_frame, height=25)
        self.label_config.grid(row=0, column=0, padx=10, pady=(5, 0), sticky="nw")

        self.slider = ctk.CTkSlider(master=frame_configure, from_=120, to=560, width=160, command=self.slider_event)
        self.slider.grid(row=1, column=0, padx=(5, 0), pady=(5, 15))

        self.button_image = ctk.CTkButton(master=frame_configure, command=self.select_image, text="Selecionar",
                                          width=85, height=30)
        self.button_image.grid(row=1, column=1, padx=(15, 15), pady=(5, 15))

        self.button_confirm = ctk.CTkButton(master=frame_configure, command=self.transform_image, text="Salvar",
                                            width=85, height=30)
        self.button_confirm.grid(row=1, column=2, padx=(0, 5), pady=(5, 15))

    def select_image(self):
        """Method to select an image from the file system."""
        self.image_path = fd.askopenfilename(filetypes=[('JPEG Files', '.jpg .jpeg'), ('PNG Files', '.png')])
        if self.image_path:
            self.display_image(self.image_path)
        else:
            logging.warning('Nenhuma imagem foi selecionada.')

    def slider_event(self, value):
        """Update scale value from slider."""
        self.scale_value = value
        logging.info(f"Slider value: {value}")

    def transform_image(self):
        """Apply sketch effect to the selected image and save the output."""
        if not self.image_path:
            messagebox.showerror('Erro', 'Nenhuma imagem selecionada.')
            return

        try:
            # Read and process image
            image = cv2.imread(self.image_path)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            inverted_image = cv2.bitwise_not(gray_image)
            blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
            inverted_blurred = cv2.bitwise_not(blurred_image)
            sketch_image = cv2.divide(gray_image, inverted_blurred, scale=self.scale_value)

            # Save processed image
            output_file = os.path.join(OUTPUT_DIR, os.path.basename(self.image_path))
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            cv2.imwrite(output_file, sketch_image)

            # Display the processed image on screen
            self.display_image(output_file)
            messagebox.showinfo('Sucesso', f'Imagem salva em: {output_file}.')
        except Exception as e:
            logging.error(f'Erro ao transformar a imagem: {e}')
            messagebox.showerror('Erro', f'Erro ao transformar a imagem: {e}')

    def display_image(self, image_path):
        """Display the image in the GUI."""
        try:
            image = Image.open(image_path)
            image = image.resize((225, 225))
            image_tk = ImageTk.PhotoImage(image)
            self.image_label.configure(image=image_tk)
            self.image_label.image = image_tk  # Keep a reference to avoid garbage collection
        except FileNotFoundError as e:
            logging.error(f"Arquivo não encontrado: {e}")
            messagebox.showerror('Erro', 'Imagem não encontrada.')
        except Exception as e:
            logging.error(f"Erro ao exibir a imagem: {e}")
            messagebox.showerror('Erro', f'Erro ao exibir a imagem: {e}')


app = App()
app.mainloop()
