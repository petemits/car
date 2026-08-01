import svgwrite
import random
import os
from datetime import datetime

class SVGCarGenerator:
    def __init__(self):
        self.output_folder = "svg_cars"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def create_sports_car(self, color="#FF0000", width=400, height=200):
        """Create a sports car SVG"""
        dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
        
        # Car body
        body_points = [
            (50, 120), (80, 80), (180, 80), (220, 100), 
            (280, 100), (320, 120), (320, 160), (50, 160)
        ]
        
        dwg.add(dwg.polygon(
            points=body_points,
            fill=color,
            stroke="#000000",
            stroke_width=2
        ))
        
        # Windows
        dwg.add(dwg.polygon(
            points=[(90, 85), (130, 85), (130, 115), (90, 115)],
            fill="#87CEEB",
            stroke="#000000",
            stroke_width=1
        ))
        
        dwg.add(dwg.polygon(
            points=[(140, 85), (210, 85), (210, 115), (140, 115)],
            fill="#87CEEB",
            stroke="#000000",
            stroke_width=1
        ))
        
        # Wheels
        dwg.add(dwg.circle(
            center=(120, 160),
            r=20,
            fill="#333333",
            stroke="#000000",
            stroke_width=2
        ))
        
        dwg.add(dwg.circle(
            center=(120, 160),
            r=8,
            fill="#FFFFFF",
            stroke="#000000",
            stroke_width=1
        ))
        
        dwg.add(dwg.circle(
            center=(260, 160),
            r=20,
            fill="#333333",
            stroke="#000000",
            stroke_width=2
        ))
        
        dwg.add(dwg.circle(
            center=(260, 160),
            r=8,
            fill="#FFFFFF",
            stroke="#000000",
            stroke_width=1
        ))
        
        # Headlights
        dwg.add(dwg.ellipse(
            center=(60, 130),
            r=(8, 5),
            fill="#FFFF00",
            stroke="#000000",
            stroke_width=1
        ))
        
        # Taillights
        dwg.add(dwg.ellipse(
            center=(310, 130),
            r=(8, 5),
            fill="#FF4444",
            stroke="#000000",
            stroke_width=1
        ))
        
        return dwg
    
    def create_sedan_car(self, color="#3498DB", width=400, height=200):
        """Create a sedan car SVG - FIXED"""
        dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
        
        # Car body
        body_points = [
            (60, 140), (80, 100), (160, 100), (200, 120),
            (280, 120), (300, 140), (300, 160), (60, 160)
        ]
        
        dwg.add(dwg.polygon(
            points=body_points,
            fill=color,
            stroke="#000000",
            stroke_width=2
        ))
        
        # Windows
        dwg.add(dwg.polygon(
            points=[(90, 105), (130, 105), (130, 130), (90, 130)],
            fill="#87CEEB",
            stroke="#000000",
            stroke_width=1
        ))
        
        dwg.add(dwg.polygon(
            points=[(140, 105), (190, 105), (190, 130), (140, 130)],
            fill="#87CEEB",
            stroke="#000000",
            stroke_width=1
        ))
        
        # Wheels
        wheel_positions = [(110, 160), (250, 160)]
        for x, y in wheel_positions:
            dwg.add(dwg.circle(
                center=(x, y),
                r=18,
                fill="#333333",
                stroke="#000000",
                stroke_width=2
            ))
            
            dwg.add(dwg.circle(
                center=(x, y),
                r=6,
                fill="#FFFFFF",
                stroke="#000000",
                stroke_width=1
            ))
        
        # Details - FIXED: using 'rect' instead of 'rectangle'
        dwg.add(dwg.rect(
            insert=(200, 125),
            size=(80, 15),
            fill="#E74C3C",
            stroke="#000000",
            stroke_width=1
        ))
        
        return dwg
    
    def create_racing_car(self, color="#E74C3C", width=400, height=180):
        """Create a racing car SVG - FIXED"""
        dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
        
        # Low, sleek body
        body_points = [
            (40, 120), (60, 80), (150, 80), (180, 100),
            (300, 100), (330, 120), (330, 140), (40, 140)
        ]
        
        dwg.add(dwg.polygon(
            points=body_points,
            fill=color,
            stroke="#000000",
            stroke_width=2
        ))
        
        # Spoiler
        dwg.add(dwg.polygon(
            points=[(300, 80), (320, 80), (330, 100), (300, 100)],
            fill="#2C3E50",
            stroke="#000000",
            stroke_width=1
        ))
        
        # Racing stripes - FIXED: using 'rect'
        stripe_y = 90
        for i in range(3):
            dwg.add(dwg.rect(
                insert=(80, stripe_y + i * 20),
                size=(200, 10),
                fill="#FFFFFF",
                stroke="none"
            ))
        
        # Wheels (larger for racing)
        dwg.add(dwg.circle(
            center=(120, 140),
            r=22,
            fill="#111111",
            stroke="#000000",
            stroke_width=2
        ))
        
        dwg.add(dwg.circle(
            center=(120, 140),
            r=10,
            fill="#FFFFFF",
            stroke="#000000",
            stroke_width=1
        ))
        
        dwg.add(dwg.circle(
            center=(280, 140),
            r=22,
            fill="#111111",
            stroke="#000000",
            stroke_width=2
        ))
        
        dwg.add(dwg.circle(
            center=(280, 140),
            r=10,
            fill="#FFFFFF",
            stroke="#000000",
            stroke_width=1
        ))
        
        return dwg
    
    def create_minimal_car(self, color="#27AE60", width=300, height=150):
        """Create a minimal/flat design car - FIXED"""
        dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
        
        # Simple rectangular body - FIXED: using 'rect'
        dwg.add(dwg.rect(
            insert=(50, 80),
            size=(200, 40),
            fill=color,
            stroke="#000000",
            stroke_width=2
        ))
        
        # Top part - FIXED: using 'rect'
        dwg.add(dwg.rect(
            insert=(70, 60),
            size=(160, 20),
            fill=color,
            stroke="#000000",
            stroke_width=2
        ))
        
        # Windows - FIXED: using 'rect'
        dwg.add(dwg.rect(
            insert=(80, 65),
            size=(60, 15),
            fill="#87CEEB"
        ))
        
        dwg.add(dwg.rect(
            insert=(150, 65),
            size=(60, 15),
            fill="#87CEEB"
        ))
        
        # Simple wheels
        dwg.add(dwg.circle(
            center=(100, 120),
            r=15,
            fill="#333333"
        ))
        
        dwg.add(dwg.circle(
            center=(200, 120),
            r=15,
            fill="#333333"
        ))
        
        return dwg
    
    def create_car_with_road(self, car_type="sports", color=None, width=500, height=300):
        """Create a car with road background - FIXED"""
        if color is None:
            colors = ["#FF0000", "#3498DB", "#E74C3C", "#27AE60", "#9B59B6"]
            color = random.choice(colors)
        
        dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
        
        # Sky background - FIXED: using 'rect'
        dwg.add(dwg.rect(
            insert=(0, 0),
            size=(width, height//2),
            fill="#87CEEB"
        ))
        
        # Road - FIXED: using 'rect'
        dwg.add(dwg.rect(
            insert=(0, height//2),
            size=(width, height//2),
            fill="#34495E"
        ))
        
        # Road markings - FIXED: using 'rect'
        for x in range(0, width, 40):
            dwg.add(dwg.rect(
                insert=(x, height//2 + 20),
                size=(20, 5),
                fill="#F1C40F"
            ))
        
        # Create car based on type
        if car_type == "sports":
            car_dwg = self.create_sports_car(color, 300, 150)
        elif car_type == "sedan":
            car_dwg = self.create_sedan_car(color, 300, 150)
        elif car_type == "racing":
            car_dwg = self.create_racing_car(color, 300, 150)
        else:
            car_dwg = self.create_minimal_car(color, 250, 120)
        
        # Extract car elements and position on road
        car_group = dwg.g(transform=f"translate(100, {height//2 - 80})")
        
        # For simplicity, let's create the car directly in this drawing
        if car_type == "sports":
            body_points = [(50, 120), (80, 80), (180, 80), (220, 100), (280, 100), (320, 120), (320, 160), (50, 160)]
            car_group.add(dwg.polygon(points=body_points, fill=color, stroke="#000000", stroke_width=2))
            
            # Add windows
            car_group.add(dwg.polygon(points=[(90, 85), (130, 85), (130, 115), (90, 115)], fill="#87CEEB", stroke="#000000", stroke_width=1))
            car_group.add(dwg.polygon(points=[(140, 85), (210, 85), (210, 115), (140, 115)], fill="#87CEEB", stroke="#000000", stroke_width=1))
            
            # Add wheels
            car_group.add(dwg.circle(center=(120, 160), r=20, fill="#333333", stroke="#000000", stroke_width=2))
            car_group.add(dwg.circle(center=(120, 160), r=8, fill="#FFFFFF", stroke="#000000", stroke_width=1))
            car_group.add(dwg.circle(center=(260, 160), r=20, fill="#333333", stroke="#000000", stroke_width=2))
            car_group.add(dwg.circle(center=(260, 160), r=8, fill="#FFFFFF", stroke="#000000", stroke_width=1))
        
        dwg.add(car_group)
        
        return dwg
    
    def generate_all_cars(self):
        """Generate all car types"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        cars = [
            ("sports_car", self.create_sports_car()),
            ("sedan_car", self.create_sedan_car()),
            ("racing_car", self.create_racing_car()),
            ("minimal_car", self.create_minimal_car()),
        ]
        
        generated_files = []
        
        for car_name, car_dwg in cars:
            filename = f"{self.output_folder}/{car_name}_{timestamp}.svg"
            car_dwg.saveas(filename)
            generated_files.append(filename)
            print(f"✓ Created: {filename}")
        
        # Create a car with road scene
        road_car = self.create_car_with_road("sports")
        road_filename = f"{self.output_folder}/car_with_road_{timestamp}.svg"
        road_car.saveas(road_filename)
        generated_files.append(road_filename)
        print(f"✓ Created: {road_filename}")
        
        return generated_files

def main():
    generator = SVGCarGenerator()
    
    print("🚗 Generating SVG Cars...")
    print("🎨 Creating multiple car designs...")
    print("📁 Saving vector car files...")
    
    files = generator.generate_all_cars()
    
    print(f"\n✨ Successfully created {len(files)} car designs!")
    print(f"📁 Location: {os.path.abspath(generator.output_folder)}")
    print(f"\n💡 You can:")
    print(f"   - Open SVG files in browsers")
    print(f"   - Edit in vector software (Inkscape, Illustrator)")
    print(f"   - Use in your flyer designs")
    print(f"   - Scale to any size without quality loss")

if __name__ == "__main__":
    main()