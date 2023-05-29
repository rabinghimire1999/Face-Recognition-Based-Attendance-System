import os

from skimage import io
import UI

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

root = Tk()
root.geometry("700x500")
root.minsize(300,100)
root.maxsize(1200,1000)
root.title("PADDY DISEASE DIAGNOSIS AND FERTILIZER CALCULATION SYSTEM")

label = Label(root, text ="                                 ").pack()
label = Label(root, text ="PADDY DISEASE DIAGNOSIS AND FERTILIZER CALCULATION SYSTEM").pack()
label = Label(root, text ="                                 ").pack()

image_file = Image.open("1.jpeg")
tk_image = ImageTk.PhotoImage(image_file)
image_label = Label(image=tk_image).pack()
label = Label(root, text ="                                 ").pack()

label = Label(root, text ="CHOOSE OPTION FROM BELOW").pack()
label = Label(root, text ="                                 ").pack()

#disease diagnosis section

def open_disease_window():
    new_window = Toplevel()
    new_window.geometry("700x500")
    new_window.minsize(300,100)
    new_window.maxsize(1200,1000)
    label = Label(new_window, text ="                                 ").pack()
    
    def load_image():
        # Get the file path from the user
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(),title="select image")

    # Load the image using PIL
        image = Image.open(file_path,'r')
        
        image = image.resize((224,224))
        
        
        

    # Create a Label widget to display the image
        image_file = ImageTk.PhotoImage(image)
       
        image_label = Label(new_window, image=image_file).pack()
        
        label = Label(new_window, text = "Uploaded Successfully").pack()
        
        b1 = Button(new_window, text = "Diagnosis Disease",command=lambda:process_image(image) )
        b1.pack()
    def process_image(image_data):
        
        model = load_model("model.h5", compile=False)
        class_names = open("labels.txt", "r").readlines()
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        
        
        image = image_data
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized_image_array
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        
        if index==0:
            message=("Given plant is Healthy Plant ")
        elif index==1:
            message=("Given plant is suffering from Tungro"+"\nRecommneded pesticide:Fenthion 100 EC (40 ml/ha)")
        elif index==2:
            message=("Given plant is suffering from Hispa"+"\nRecommneded pesticide: Malathion 50 EC")
        elif index==3:
            message=("Given plant is suffering from Bacterial leaf Blight"+"\nRecommneded pesticide:Copper oxychloride 50 WP (copper oxychloride), Nativo 75 WDG (Tebuconazole+trifloxystrobin), Gem Star Super 325 SC (azoxystrobin+difenconazole) and Bordeaux mixture")
        elif index==4:
            message=("Given plant is suffering from Bacterial leaf Streak"+"\nRecommneded pesticide: Terramycin 17, Brestanol, Agrimycin 500 and a combination of Agrimycin 100 + Fytolan")
        elif index==5:
            message=("Given plant is suffering from Bacterail panicle blight"+"\nRecommneded pesticide: Quinolone antibiotic oxolinic acid")
        elif index==6:
            message=("Given plant is suffering from Blast"+"\nRecommneded pesticide: Tricyclazole 22% + Hexaconazole 3% SC fungicide")
        elif index==7:
            message=("Given plant is suffering from Brown spot"+"\nRecommneded pesticide: Iprodione, Propiconazole, Azoxystrobin, Trifloxystrobin, and carbendazim")
        elif index==8:
            message=("Given plant is suffering from Dead heart"+"\nRecommneded pesticide: Azadirachtin 0.03% 400 ml/ac")
        elif index==9:
            message=("Given plant is suffering from Downy Mildew"+"\nRecommneded pesticide: Chlorothalonil and Mancozeb")
        else:
            message=("INVALID INPUT")
            
        T = Text(new_window, height = 5, width = 52)
        T.pack()
        T.insert(END, message)
        
        
        

  
    
    label = Label(new_window, text = "DISEASE DIAGNOSIS SYSTEM").pack()
    button = Button( new_window,text="Upload Image", command=load_image).pack()
    label = Label(new_window, text ="                                 ").pack()
    
    
    new_window.mainloop()
    
def open_fertilizer_window():
    new_window = Toplevel()
    new_window.geometry("700x500")
    new_window.minsize(300,100)
    new_window.maxsize(1200,1000)
    label = Label(new_window, text ="                                 ").pack()
    
    options = ["Irrigated Land", "Rain-fed Field"]
    selected_option = StringVar()
    selected_option.set(options[0])
    area_label = Label(new_window, text="Enter the area of the land(in HECTARE):")
    area_label.pack()
    area_entry = Entry(new_window)
    area_entry.pack()
    
    def calculate_fertilizer():
        area = float(area_entry.get()) # Get the area entered by the user
        selected = selected_option.get() # Get the selected option from the option menu
        if selected == "Irrigated Land":
            dap_fertilizer = area * 86.96# Calculate the required fertilizer for irrigated land
            urea_fertilizer= area *226.84
            mop_fertilizer = area * 66.67
        elif selected == "Rain-fed Field":
            dap_fertilizer = area * 65.2# Calculate the required fertilizer for irrigated land
            urea_fertilizer= area * 126.7
            mop_fertilizer = area * 50.0
    # Create a Label widget to display the calculated fertilizer
        fertilizer_label = Label(new_window, text=f"Required fertilizer: {dap_fertilizer} DAP + {urea_fertilizer} UREA + {mop_fertilizer} MOP")
        fertilizer_label.pack()
    
    calculate_button = Button(new_window, text="Calculate", command=calculate_fertilizer)
    calculate_button.pack()
    
    option_menu = OptionMenu(new_window, selected_option, *options)
    option_menu.pack()



    
    
    new_window.mainloop()
    
    
    
    
button = Button( text="DISEASE DIAGNOSIS", command=open_disease_window).pack()
label = Label(root, text ="                                 ").pack()
button = Button( text="FERTILIZER CALCULATION", command=open_fertilizer_window).pack()
label = Label( text = "                                         ").pack()
label = Label( text = "                                         ").pack()
label = Label( text = "                                         ").pack()
label = Label( text = "                                         ").pack()

#label = Label( text = "RABIN GHIMIRE || SANGAM POUDEL || SHREEYUB GHIMIRE || SHUBHAM NEUPANE").pack()





    

    


root.mainloop()