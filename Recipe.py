import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QItemSelectionModel

# Define the Ingredient class
class Food:
    def __init__(self, name, image_path, description, effect, adjective):
        self.name = name
        self.image_path = image_path
        self.description = description
        self.effect = effect
        self.adjective = adjective

    def get_image(self):
        return QPixmap(self.image_path)

    def __str__(self):
        return self.name

# Sample ingredients and proteins
INGREDIENTS = [
    Food("Fire Peppers", "CookingStuff/Fire Peppers.png", "Adds a spicy heat that also imparts resistance to cold when ingested.", "Grants Cold Resistance", "Hot"),
    Food("Moonleaf", "CookingStuff/Moon Leaf.png", "A silvery herb that enhances night vision when brewed into a tea.", "Grants +10 additional ft of Darkvision", ""),
    Food("Dragonsalt", "CookingStuff/Dragonsalt.png", "A crystalline spice with a strong, savory flavor; enhances strength for a short period.", "Grants +1 to strength", "Draconic"),
    Food("Umbral Corn", "CookingStuff/Umbral Corn.png", "A purple corn that makes the consumer harder to detect in shadows.", "Grants +2 to stealth checks to hide", "Shaded"),
    Food("Faerie Flower Pollen", "CookingStuff/Faerie Flower Pollen.png", "A glittering spice that induces mild euphoria and enhances creativity.", "Creatures that eat this treat must succeed a DC 12 Charisma saving throw or be charmed for 1 hour.", "Sparkly"),
    Food("Thunderseed", "CookingStuff/Thunderseed.png", "Small, round seeds that crackle with energy; temporarily increases agility.", "Increases movement speed by 5ft.", "Shocking"),
    Food("Frostmint", "CookingStuff/Frostmint.png", "A minty herb that cools the body and provides resistance to fire.", "Grants Fire Resistance", "Cooling"),
    Food("Ember Root", "CookingStuff/Ember Root.png", "A spicy root that warms the body.", "Grants resistance to cold temperatures", "Warming"),
    Food("Dreamfluff", "CookingStuff/Dreamfluff.png", "A fluffy, Cotton Candy-Like herb that induces vivid dreams and aids in prophetic visions.", "Gain +1 to your next Saving Throw", "Dreamy"),
    Food("Serpent's Kiss", "CookingStuff/Serpent's Kiss.png", "A bitter green powder that can be used as an antidote for certain poisons when mixed into tea.", "Grants Resistance to Poison damage and advantage on saving throws against being poisoned.", "Curing"),
    Food("Trollroot", "CookingStuff/Trollroot.png", "A Hearty bitter root that has restorative properties.", "Regain 3 hit point at the start of each of your turns so long as you are conscious.", "Regenerating"),
    Food("Gemberry Jelly", "CookingStuff/Gemberry Jelly.png", "A Jelly made from mashed Yellow, Green, Red and Blue Gemberries. Used to enhance a meal.", "Double the effects of other ingredients used.", "Potent")
]

PROTEINS = [
    Food("No Protein", "", "", "", ""),
    Food("Firebird Breast", "CookingStuff/Firebird Breast.png", "Tender and juicy meat from a minor Phoenix, known for its slight warmth and spicy undertone.", "", ""),
    Food("Griffon Drumsticks", "CookingStuff/Griffon Drumstick.png", "Large, meaty drumsticks from the noble griffon, with a flavor similar to a mix between chicken and lion.", "", ""),
    Food("Thunder Lizard Tail Medallions", "CookingStuff/TL_Tail Medallion.png", "Succulent and tender medallions from the tail of a Thunder Lizard known for its rich, exotic flavor.", "", ""),
    Food("Minor Phoenix Eggs", "CookingStuff/Phoenix Eggs.png", "Large, fiery eggs laid by a minor phoenix, with a rich, smoky flavor.", "", ""),
    Food("Mystic Fish Fillet", "CookingStuff/Mystic Fish Fillet.png", "Delicate fillets from a rare, luminescent fish that swims in enchanted desert oases.", "", ""),
    Food("Prime Bear Haunch", "CookingStuff/Prime Bear Haunch.png", "This meat is rich and gamey, requiring long, slow cooking to bring out its best flavors.", "", ""),
    Food("Wyvern Wings", "CookingStuff/Wyvern Wings.png", "Tough yet flavorful, these wings are often marinated in strong spices to tenderize the meat.", "", ""),
    Food("Basilisk Fillet", "CookingStuff/Basilisk Fillet.png", "This meat is prized for its tenderness and slight petrifying properties.", "", ""),
]

MEALS = [
    Food("Fiery Moonbird Delight", "Meals/Fiery Moonbird Delight.png", "A masterfully crafted dish that combines the tender, spicy meat of the firebird with a blend of exotic spices, creating a meal that is both flavorful and magically potent.", "A creature who eats this meal is always comfortably warm and is resistant to cold damage. The creature also recovers hit points equal to 1d10 + your proficency bonus at the start of each of their turns. These effects last until their next Long Rest.", ""),
    Food("Spiced Griffon Drumsticks", "Meals/Spiced Griffon Drumstick.png", "These drumsticks from the noble griffon are marinated and roasted with an array of magical spices, creating a dish that is both hearty and enchanted, favored by warriors and scouts alike.", "Grants +3 to acrobatics checks when eaten. A creature who eats this meal also gains advantage on perception checks used to spot things at far distances. These effects last until their next Long Rest.", ""),
    Food("Shadow Grilled Thunder Lizard Tail Steaks", "Meals/Shadow Grilled Thunder Lizard Tail Steaks.png", "Slices of thunder lizard tail, known for their rich and gamey flavor, are transformed into medallions and infused with powerful magical spices.", "Grants +3 to stealth checks when eaten. A creature who eats the meal also gains Immunity to lightning damage. These effects last until their next Long Rest.", ""),
    Food("Inferno Eggs", "Meals/Inferno Eggs.png", "These legendary eggs from the Minor Phoenix are prepared with a selection of magical spices, creating a dish that is not only flavorful but also grants remarkable abilities. This dish is particularly popular among spellcasters.", "A creature who eats this meals gains a +2 to their Spell Save DC for their spellcasting feature. These effects last until their next Long Rest.", ""),
    Food("Mystic Fish Sashimi", "Meals/Mystic Fish Sashimi.png", "A refined and elegant dish featuring thinly sliced fillets of the rare mystic fish, known for their delicate texture and subtle, ethereal flavor. This sashimi is carefully prepared to preserve the natural luminescence of the fish.", "A creature who eats this gains Resistance to cold damage and the effects of the Water Breathing Spell. The creature also emits bright White-Blue Light up to 10ft and dim light for another 5ft. These effects last until their next Long Rest.", ""),
    Food("Roasted Prime Bear Haunch", "Meals/Roasted Prime Bear Haunch.png", "A hearty and robust dish featuring a prime cut of dire bear haunch, expertly prepared to showcase its rich, gamey flavor. This meal is known for its ability to fortify those who consume it, providing enhanced physical strength and resilience.", "Grants advantage on Constitution saving throws and +2 to strength. A creature who eats this meal also gains 15 Temporary hit points. These effects last until their next Long Rest.", ""),
    Food("Roasted King Wyvern Wings", "Meals/Roasted King Wyvern Wings.png", "This dish features succulent wyvern wings, marinated and roasted to perfection, offering a unique and flavorful experience. Known for their slightly spicy and savory taste, this dish is popular among adventurers who need to bolster their resilience and agility.", "Grants immunity to poison damage and advantage against being poisoned. A creature who eats this meal also gains +3 to their athletics. These effects last until their next Long Rest.", ""),
    Food("Stoneskin Steaks", "Meals/Stoneskin Steaks.png", "A luxurious and potent dish featuring tender fillets from the elusive basilisk, known for their rich texture and subtly earthy flavor. This exquisite preparation is seasoned with a blend of magical spices that enhance the eater’s physical and defensive capabilities.", "A creature who eats this meal gains the effects of the stoneskin spell. Their AC is also increased by 1. These effects last until their next Long Rest.", ""),
    Food("Serpent Tea", "Meals/Serpent Tea.png", "", "Grants Resistance to Poison damage and advantage on saving throws against being poisoned.", ""),
    Food("Moonserpent Tea", "Meals/Moonserpent Tea.png", "", "Grants +10 additional ft of Darkvision\nGrants Resistance to Poison damage and advantage on saving throws against being poisoned.", ""),
    Food("Moonleaf Tea", "Meals/Moonleaf Tea.png", "", "Grants +10 additional ft of Darkvision", ""),
]

RECIPES = {
    frozenset(["Firebird Breast", "Fire Peppers", "Moonleaf", "Dragonsalt", "Thunderseed"]): "Fiery Moonbird Delight",
    frozenset(["Griffon Drumsticks", "Dragonsalt", "Ember Root", "Faerie Flower Pollen", "Frostmint"]): "Spiced Griffon Drumsticks",
    frozenset(["Thunder Lizard Tail Medallions", "Umbral Corn", "Frostmint", "Gemberry Jelly", "Fire Peppers"]): "Shadow Grilled Thunder Lizard Tail Steaks",
    frozenset(["Minor Phoenix Eggs", "Dragonsalt", "Trollroot", "Faerie Flower Pollen", "Serpent's Kiss"]): "Inferno Eggs",
    frozenset(["Mystic Fish Fillet", "Frostmint", "Dreamfluff", "Faerie Flower Pollen", "Gemberry Jelly"]): "Mystic Fish Sashimi",
    frozenset(["Prime Bear Haunch", "Dragonsalt", "Fire Peppers", "Trollroot", "Ember Root"]): "Roasted Prime Bear Haunch",
    frozenset(["Wyvern Wings", "Thunderseed", "Ember Root", "Serpent's Kiss", "Umbral Corn"]): "Roasted King Wyvern Wings",
    frozenset(["Basilisk Fillet", "Serpent's Kiss", "Gemberry Jelly", "Trollroot", "Fire Peppers"]): "Stoneskin Steaks",
    frozenset(["Serpent's Kiss"]): "Serpent Tea",
    frozenset(["Serpent's Kiss", "Moonleaf"]): "Moonserpent Tea",
    frozenset(["Moonleaf"]): "Moonleaf Tea",
}

class SnackApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.snack_effect = ""
        self.snack_message = ""
        self.setWindowTitle("Snack Maker")
        self.setFixedSize(940, 700)
        
        # Background image
        self.setAutoFillBackground(True)
        palette = QPalette()
        pixmap = QPixmap("Cooking.jpg")  # Replace with your image path
        if pixmap.isNull():
            print("Error: Unable to load the background image. Check the file path.")
        else:
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            brush = QBrush(scaled_pixmap)
            palette.setBrush(QPalette.Window, brush)
            self.setPalette(palette)
        
        self.selected_ingredients = []
        self.selected_protein = None

        # Main horizontal layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        
        left_layout = QVBoxLayout()
        left_layout.addStretch()
        
        # Lists Layout (ingredients and proteins)
        lists_layout = QHBoxLayout()
        
        # Ingredients List with translucent and rounded corners
        ingredients_layout = QVBoxLayout()
        ingredients_layout.addStretch()
        ingredients_label = QLabel()
        ingredients_label.setPixmap(QPixmap("Labels/Ingredients.png").scaledToWidth(250, Qt.SmoothTransformation))  # Replace with your image path
        self.ingredients_list = IngredientListWidget()
        self.ingredients_list.setFixedSize(230, 350)
        self.ingredients_list.addItems([str(ingredient) for ingredient in INGREDIENTS])
        self.ingredients_list.setStyleSheet("""
            @font-face {
                font-family: 'JupiterPro'; 
                src: 'Fontspring-DEMO-jupiter_pro_bold.otf'; 
            }
            
            QListWidget {
                background-color: rgba(30, 30, 30, 180);
                border-radius: 10px;
                padding: 5px;
                font-size: 18px;
                font-weight: bold;
                font-family: 'JupiterPro';
                color: black;
                border-style: solid;
                border-width: 2px;
                border-color: black;
            }
            
            QListWidget::item {
                margin: 2px;
                background-color: rgba(200, 200, 200, 0.8);
                border-radius: 10px;
            }
            
            QListWidget::item:selected {
                color: white;
            }
        """)
        self.ingredients_list.setSelectionMode(QListWidget.MultiSelection)
        self.ingredients_list.itemSelectionChanged.connect(self.update_grid)
        self.ingredients_list.setMouseTracking(True)
        ingredients_layout.addWidget(ingredients_label, alignment=Qt.AlignCenter)
        ingredients_layout.addWidget(self.ingredients_list, alignment=Qt.AlignCenter)
        ingredients_layout.addStretch()
        
        self.ingredients_list.itemEntered.connect(self.show_ingredient_description)
        
        # Protein List with translucent and rounded corners
        proteins_layout = QVBoxLayout()
        proteins_layout.addStretch()
        proteins_label = QLabel()
        proteins_label.setPixmap(QPixmap("Labels/Proteins.png").scaledToWidth(150, Qt.SmoothTransformation))  # Replace with your image path
        self.protein_list = QListWidget()
        self.protein_list.setFixedSize(200, 295)
        self.protein_list.addItems([str(protein) for protein in PROTEINS])
        self.protein_list.setStyleSheet("""
            @font-face {
                font-family: 'JupiterPro'; 
                src: 'Fontspring-DEMO-jupiter_pro_bold.otf'; 
            }
                                        
            QListWidget {
                background-color: rgba(30, 30, 30, 180);
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
                font-weight: bold;
                font-family: 'JupiterPro';
                color: black;
                border-style: solid;
                border-width: 2px;
                border-color: black;
            }
            
            QListWidget::item {
                margin: 2px 0px 2px;
                padding: 2px;
                background-color: rgba(200, 200, 200, 0.8);
                border-radius: 10px;
            }
            
            QListWidget::item:selected {
                color: white;
            }
        """)
        self.protein_list.setSelectionMode(QListWidget.SingleSelection)
        self.protein_list.itemSelectionChanged.connect(self.update_protein)
        self.protein_list.setWordWrap(True)
        self.protein_list.setMouseTracking(True)
        proteins_layout.addWidget(proteins_label, alignment=Qt.AlignCenter)
        proteins_layout.addWidget(self.protein_list, alignment=Qt.AlignCenter)
        proteins_layout.addStretch()
        
        self.protein_list.itemEntered.connect(self.show_protein_description)
        
        lists_layout.addLayout(ingredients_layout)
        lists_layout.addSpacing(20)  # Add spacing between lists
        lists_layout.addLayout(proteins_layout)
        
        self.ingredient_description = QLabel("")
        self.ingredient_description.setFixedSize(450, 250)
        self.ingredient_description.setWordWrap(True)
        self.ingredient_description.setStyleSheet("""
            @font-face {
                font-family: 'JupiterPro'; 
                src: 'Fontspring-DEMO-jupiter_pro_bold.otf'; 
            }
                                        
            QLabel {
                background-color: rgba(30, 30, 30, 180);
                border-radius: 10px;
                padding: 5px;
                font-size: 20px;
                font-weight: bold;
                font-family: 'JupiterPro';
                color: white;
                border-style: solid;
                border-width: 2px;
                border-color: black;
            }
        """)
        left_layout.addLayout(lists_layout)
        left_layout.addStretch()
        left_layout.addWidget(self.ingredient_description, alignment=Qt.AlignCenter)
        left_layout.addStretch()
        
        # Button Layout
        button_layout = QVBoxLayout()
        button_layout.addStretch()
        button_label = QLabel()
        button_label.setPixmap(QPixmap("Labels/Go.png").scaledToWidth(60, Qt.SmoothTransformation))  # Replace with your image path
        self.generate_button = QPushButton("", self)
        self.generate_button.setFixedSize(80, 80)
        self.generate_button.setStyleSheet("""
            QPushButton {
                background-image: url('CookingStuff/GoButton.png');
                background-repeat: no-repeat;
                background-position: center;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 100);
            }
        """)
        self.generate_button.clicked.connect(self.generate_snack)
        button_layout.addWidget(button_label, alignment=Qt.AlignCenter)
        button_layout.addWidget(self.generate_button, alignment=Qt.AlignCenter)
        button_layout.addStretch()  # Added to center the button

        # Grid and protein display
        right_layout = QVBoxLayout()
        right_layout.addStretch()
        
        # Protein display box centered
        protein_box_layout = QVBoxLayout()
        protein_label = QLabel()
        protein_label.setPixmap(QPixmap("Labels/Protein.png").scaledToWidth(200, Qt.SmoothTransformation))  # Replace with your image path
        self.protein_label = QLabel(self)
        self.protein_label.setFixedSize(80, 80)  # Make the protein box square
        self.protein_label.setStyleSheet("""
            QLabel {
                background-color: rgba(30, 30, 30, 180);
                border: 1px solid black;
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.protein_label.setAlignment(Qt.AlignCenter)
        protein_box_layout.addWidget(protein_label, alignment=Qt.AlignCenter)
        protein_box_layout.addWidget(self.protein_label, alignment=Qt.AlignCenter)
        right_layout.addLayout(protein_box_layout)
        
        right_layout.addStretch()
        
        # Cooking grid display
        grid_box_layout = QVBoxLayout()
        grid_label = QLabel()
        grid_label.setPixmap(QPixmap("Labels/Cooking.png").scaledToWidth(200, Qt.SmoothTransformation))  # Replace with your image path
        grid_layout = QGridLayout()
        self.ingredient_labels = []
        for i in range(2):
            for j in range(2):
                label = QLabel(self)
                label.setFixedSize(80, 80)  # Make each grid box square
                label.setStyleSheet("""
                    QLabel {
                        background-color: rgba(30, 30, 30, 180);
                        border: 1px solid black;
                        border-radius: 10px;
                        padding: 5px;
                    }
                """)
                label.setAlignment(Qt.AlignCenter)
                grid_layout.addWidget(label, i, j)
                self.ingredient_labels.append(label)
        self.grid_widget = QWidget()
        self.grid_widget.setLayout(grid_layout)
        self.grid_widget.setFixedWidth(190)
        grid_box_layout.addWidget(grid_label, alignment=Qt.AlignCenter)
        grid_box_layout.addWidget(self.grid_widget, alignment=Qt.AlignCenter)
        
        middle_right_layout = QHBoxLayout()
        middle_right_layout.addLayout(button_layout)
        middle_right_layout.addLayout(grid_box_layout)
        middle_right_layout.addWidget(QWidget())
        
        right_layout.addLayout(middle_right_layout)
        
        # Snack Result Label
        snack_result_layout = QVBoxLayout()
        snack_result_label = QLabel()
        snack_result_label.setPixmap(QPixmap("Labels/Snack_Results.png").scaledToWidth(350, Qt.SmoothTransformation))  # Replace with your image path
        self.snack_label = QLabel("", self)
        self.snack_label.setAlignment(Qt.AlignCenter)
        self.snack_label_image = SnackQLabel(self)
        self.snack_label_image.setFixedSize(80, 80)  # Make the protein box square
        self.snack_label_image.setStyleSheet("""
            QLabel {
                background-color: rgba(30, 30, 30, 180);
                border: 1px solid black;
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.snack_label_image.setAlignment(Qt.AlignCenter)
        snack_result_layout.addWidget(snack_result_label, alignment=Qt.AlignCenter)
        snack_result_layout.addWidget(self.snack_label, alignment=Qt.AlignCenter)
        snack_result_layout.addWidget(self.snack_label_image, alignment=Qt.AlignCenter)
        right_layout.addLayout(snack_result_layout)
        
        right_layout.addStretch()

        # Add widgets to the main layout
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        right_layout.setContentsMargins(20, 0, 0, 0)

    def update_grid(self):
        # Update selected ingredients
        self.selected_ingredients = [INGREDIENTS[i.row()] for i in self.ingredients_list.selectedIndexes()]
        
        # Update grid based on selected ingredients
        for i in range(4):
            if i < len(self.selected_ingredients):
                pixmap = self.selected_ingredients[i].get_image()
                if not pixmap.isNull():
                    self.ingredient_labels[i].setPixmap(pixmap.scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                else:
                    self.ingredient_labels[i].clear()
            else:
                self.ingredient_labels[i].clear()

    def update_protein(self):
        # Get selected protein item
        selected_items = self.protein_list.selectedItems()
        if selected_items:
            selected_protein = PROTEINS[self.protein_list.row(selected_items[0])]
            self.selected_protein = selected_protein
            pixmap = selected_protein.get_image()
            if not pixmap.isNull():
                self.protein_label.setPixmap(pixmap.scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                self.protein_label.clear()
        else:
            self.selected_protein = None
            self.protein_label.clear()

    def generate_snack(self):
        snack_set = [ingredient.name for ingredient in self.selected_ingredients]
        if self.selected_protein and self.selected_protein.name != "No Protein":
            snack_set.append(self.selected_protein.name)
        snack_key = frozenset(snack_set)
        snack = RECIPES.get(snack_key, "Unknown Snack")
        self.snack_message = f"{snack}"
        
        if(self.snack_message == "Unknown Snack"):
            self.snack_message = ""
            self.snack_effect = ""
            for ingredient in self.selected_ingredients:
                if(ingredient.name != "Moonleaf" and ingredient.name != "Serpent's Kiss"):
                    if len(ingredient.adjective) > 0:
                        self.snack_message += ingredient.adjective + " "
                        self.snack_effect += ingredient.effect + "<br/>"
            self.snack_message += "Snack"
            pixmap = QPixmap("CookingStuff/Snack.png")
        else:
            for meal in MEALS:
                if meal.name == snack:
                    pixmap = meal.get_image()
                    self.snack_effect = meal.effect
                    break
        
        if not pixmap.isNull():
            self.snack_label_image.setPixmap(pixmap.scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.snack_label_image.clear()
            
        self.snack_label.setText(self.snack_message)
        self.snack_label.setStyleSheet("""
            @font-face {
                font-family: 'JupiterPro'; 
                src: 'Fontspring-DEMO-jupiter_pro_bold.otf'; 
            }
            
            QLabel {
                background-color: rgba(200, 200, 200, 0.8);
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
                font-weight: bold;
                font-family: 'JupiterPro';
                color: black;
                border-style: solid;
                border-width: 2px;
                border-color: black;
            }
        """)
        self.show_snack_description()
        
    def show_ingredient_description(self, item):
        ingredient_name = item.text()
        for ingredient in INGREDIENTS:
            if ingredient.name == ingredient_name:
                self.ingredient_description.setText("<div style='font-weight: bold;'>" + ingredient.name + ":</div> <body><font color=grey>" + ingredient.description + "</font></body>")
                break
    
    def show_protein_description(self, item):
        protein_name = item.text()
        for protein in PROTEINS:
            if protein.name == protein_name:
                if protein_name != "No Protein":
                    self.ingredient_description.setText("<div style='font-weight: bold;'>" + protein.name + ":</div> <body><font color=grey>" + protein.description + "</font></body>")
                else:
                    self.ingredient_description.setText("")
                break
    
    def show_snack_description(self):
        self.ingredient_description.setText("<div style='font-weight: bold;'>" + self.snack_message + ":</div> <body><font color=grey>" + self.snack_effect + "</font></body>")
        self.ingredient_description.adjustSize()
        
    def reset_recipe(self):
        self.ingredient_description.setText("")
        self.protein_list.clearSelection()
        self.ingredients_list.clearSelection()
        self.snack_label_image.clear()
        self.snack_effect = ""
        self.snack_label.setText("")
        self.snack_label.setStyleSheet("")
        self.snack_message = ""
        
    
class SnackQLabel(QLabel):
    def __init__(self, snack_app, parent=None):
        super(SnackQLabel, self).__init__(parent)
        self.snack_app = snack_app
    
    def enterEvent(self, event):
        self.snack_app.show_snack_description()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.snack_app.reset_recipe()
        super().mousePressEvent(event)
        

class IngredientListWidget(QListWidget):
    def __init__(self, parent=None, max_selected = 4):
        super().__init__(parent)
        self.max_selected = max_selected

    def selectionCommand(self, index, event):
        if len(self.selectedItems()) >= self.max_selected:
            return QItemSelectionModel.Deselect
        else:
            return super().selectionCommand(index, event)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SnackApp()
    window.show()
    sys.exit(app.exec_())