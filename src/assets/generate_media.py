from svgwrite import Drawing
import os

# Output folder
output_dir = os.path.expanduser('~/elparadisogonzalo/src/assets')
os.makedirs(output_dir, exist_ok=True)

# Variations for media
colors = ['lightblue', 'lightgreen', 'lightpink']
strokes = ['blue', 'green', 'red']
sizes = [100, 150, 200]

for i, (fill, stroke) in enumerate(zip(colors, strokes), 1):
    for size in sizes:
        filename = f"elparadisogonzalo_logo_{i}_{size}.svg"
        filepath = os.path.join(output_dir, filename)
        dwg = Drawing(filepath, size=(size, size))
        dwg.add(dwg.circle(center=(size/2, size/2), r=size/2 - 10, stroke=stroke, stroke_width=4, fill=fill))
        dwg.add(dwg.text('Logo', insert=('50%','55%'), text_anchor='middle', font_size=12, fill=stroke))
        dwg.save()
        print("Created:", filename)
