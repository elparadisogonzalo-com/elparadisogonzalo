import svgwrite

def create_svg(output_file="logo.svg"):
    dwg = svgwrite.Drawing(output_file, size=(100, 100))
    dwg.add(dwg.circle(center=(50, 50), r=40, 
                       stroke='blue', stroke_width=4, 
                       fill='lightblue'))
    dwg.add(dwg.text('Logo', insert=('50%', '55%'), 
                     text_anchor='middle', font_size=12, 
                     fill='darkblue'))
    dwg.save()
    print(f"SVG created at: {output_file}")

if __name__ == "__main__":
    create_svg()
