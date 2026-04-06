from svgwrite import Drawing
import os

# Path to save SVG
output_file = os.path.expanduser('~/elparadisogonzalo/src/assets/elparadisogonzalo_logo.svg')

# Create SVG
dwg = Drawing(output_file, size=(100,100))
dwg.add(dwg.circle(center=(50,50), r=40, stroke='blue', stroke_width=4, fill='lightblue'))
dwg.add(dwg.text('Logo', insert=('50%','55%'), text_anchor='middle', font_size=12, fill='darkblue'))
dwg.save()

print("SVG created at:", output_file)
