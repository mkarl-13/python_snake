from colors import PALETTES

class PaletteManager:
    def __init__(self):
        self.current_palette_index = 0
        self.colors = list(PALETTES[self.current_palette_index])
        
    def SwitchPalette(self):
        if self.current_palette_index + 1 < len(PALETTES):
            self.current_palette_index += 1
        else:
            self.current_palette_index = 0
        self.colors = PALETTES[self.current_palette_index]