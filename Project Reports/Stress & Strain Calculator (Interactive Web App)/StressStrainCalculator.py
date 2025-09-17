# Install ipywidgets if not already installed
!pip install ipywidgets matplotlib

import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt

# Material library (Young's modulus in Pa)
materials = {
    "Steel": 2e11,
    "Stainless Steel": 1.9e11,
    "Aluminum": 7e10,
    "Copper": 1.1e11,
    "Brass": 1e11,
    "Titanium": 1.1e11,
    "Cast Iron": 1e11,
    "Rubber": 1e7,
    "Nylon": 2e9,
    "Polycarbonate": 2.4e9,
    "GFRP": 2e10,
    "CFRP": 7e10,
    "Concrete": 3e10,
    "Reinforced Concrete": 2.5e10
}

# Define interactive widgets
material_widget = widgets.Dropdown(
    options=list(materials.keys()),
    value='Steel',
    description='Material:'
)

force_widget = widgets.FloatSlider(
    value=10000,
    min=0,
    max=100000,
    step=1000,
    description='Force (N):'
)

area_widget = widgets.FloatText(
    value=0.0001,
    description='Area (m²):'
)

original_length_widget = widgets.FloatText(
    value=2.0,
    description='Original Length (m):'
)

delta_length_widget = widgets.FloatText(
    value=0.001,
    description='Change in Length (m):'
)

output = widgets.Output()

# Function to calculate and update plot
def update_calculations(change=None):
    with output:
        output.clear_output()
        material = material_widget.value
        E_material = materials[material]
        force = force_widget.value
        area = area_widget.value
        L0 = original_length_widget.value
        delta_L = delta_length_widget.value

        stress = force / area
        strain = delta_L / L0
        youngs_modulus = stress / strain if strain != 0 else None

        # Display results
        print(f"Material: {material}")
        print(f"Stress: {stress:.2e} Pa")
        print(f"Strain: {strain:.6f}")
        if youngs_modulus:
            print(f"Young's Modulus: {youngs_modulus:.2e} Pa")
        else:
            print("Young's Modulus: Cannot compute (strain is zero)")



# Link widget changes to update function
material_widget.observe(update_calculations, names='value')
force_widget.observe(update_calculations, names='value')
area_widget.observe(update_calculations, names='value')
original_length_widget.observe(update_calculations, names='value')
delta_length_widget.observe(update_calculations, names='value')

# Display widgets
display(material_widget, force_widget, area_widget, original_length_widget, delta_length_widget, output)

# Initial calculation
update_calculations()
