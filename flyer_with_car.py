import svgwrite
import os
from datetime import datetime

class CarFlyerGenerator:
    def __init__(self):
        self.output_folder = "car_flyers"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def create_simple_car(self, dwg, x=100, y=400, color="#E74C3C", scale=1.0):
        """Add a simple car to any SVG drawing - FIXED"""
        car_group = dwg.g(transform=f"translate({x}, {y}) scale({scale})")
        
        # Car body
        body_points = [(0, 20), (20, 0), (80, 0), (100, 20), (100, 40), (0, 40)]
        car_group.add(dwg.polygon(points=body_points, fill=color, stroke="#000000", stroke_width=1))
        
        # Windows - FIXED: using 'rect'
        car_group.add(dwg.rect(insert=(25, 5), size=(25, 15), fill="#87CEEB"))
        car_group.add(dwg.rect(insert=(55, 5), size=(25, 15), fill="#87CEEB"))
        
        # Wheels
        car_group.add(dwg.circle(center=(20, 40), r=8, fill="#333333"))
        car_group.add(dwg.circle(center=(80, 40), r=8, fill="#333333"))
        
        return car_group
    
    def create_car_dealership_flyer(self):
        """Create a car dealership flyer with multiple cars - FIXED"""
        width, height = 800, 1200
        dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
        
        # Background - FIXED: using 'rect'
        dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill="#2C3E50"))
        
        # Title
        dwg.add(dwg.text(
            "CAR DEALERSHIP EXPO 2024",
            insert=(width//2, 100),
            font_family="Arial",
            font_size=36,
            fill="white",
            text_anchor="middle",
            font_weight="bold"
        ))
        
        # Subtitle
        dwg.add(dwg.text(
            "Discover the Future of Automotive Technology",
            insert=(width//2, 140),
            font_family="Arial",
            font_size=20,
            fill="#ECF0F1",
            text_anchor="middle"
        ))
        
        # Add multiple cars
        car_colors = ["#E74C3C", "#3498DB", "#F39C12", "#2ECC71", "#9B59B6"]
        car_positions = [(100, 300), (300, 300), (500, 300), (200, 500), (400, 500)]
        
        for i, (x, y) in enumerate(car_positions):
            color = car_colors[i % len(car_colors)]
            car_group = self.create_simple_car(dwg, x, y, color, scale=1.5)
            dwg.add(car_group)
        
        # Event details
        details = [
            "Date: October 15-17, 2024",
            "Time: 9:00 AM - 8:00 PM",
            "Location: Convention Center",
            "Free Test Drives Available!",
            "Special Launch Discounts"
        ]
        
        y_pos = 700
        for detail in details:
            dwg.add(dwg.text(
                detail,
                insert=(width//2, y_pos),
                font_family="Arial",
                font_size=18,
                fill="white",
                text_anchor="middle"
            ))
            y_pos += 40
        
        # Save flyer
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/car_dealership_flyer_{timestamp}.svg"
        dwg.saveas(filename)
        
        return filename
    
    def create_car_showcase_flyer(self):
        """Create a modern car showcase flyer - FIXED"""
        width, height = 800, 1200
        dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
        
        # Gradient background
        gradient = dwg.defs.add(dwg.linearGradient((0, 0), (0, 1)))
        gradient.add_stop_color(0, '#1a2a6c')
        gradient.add_stop_color(50, '#b21f1f')
        gradient.add_stop_color(100, '#fdbb2d')
        
        # FIXED: using 'rect' with gradient
        dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill=gradient.get_paint_server()))
        
        # Main title
        dwg.add(dwg.text(
            "AUTOMOTIVE INNOVATION",
            insert=(width//2, 120),
            font_family="Arial",
            font_size=42,
            fill="white",
            text_anchor="middle",
            font_weight="bold"
        ))
        
        # Featured car (larger)
        featured_car = self.create_simple_car(dwg, width//2 - 60, 250, "#E74C3C", scale=2.5)
        dwg.add(featured_car)
        
        # Car specifications
        specs = [
            "⚡ Electric & Hybrid Models",
            "🚀 Advanced Safety Features", 
            "📱 Smart Connectivity",
            "🌱 Eco-Friendly Options",
            "💰 Competitive Pricing"
        ]
        
        y_pos = 500
        for spec in specs:
            dwg.add(dwg.text(
                spec,
                insert=(width//2, y_pos),
                font_family="Arial",
                font_size=20,
                fill="white",
                text_anchor="middle"
            ))
            y_pos += 45
        
        # Contact information
        contact_info = [
            "Visit our showroom today!",
            "📞 555-0123",
            "🌐 www.carshowcase.com",
            "📍 123 Automotive Avenue"
        ]
        
        y_pos = 800
        for info in contact_info:
            dwg.add(dwg.text(
                info,
                insert=(width//2, y_pos),
                font_family="Arial",
                font_size=18,
                fill="#ECF0F1",
                text_anchor="middle"
            ))
            y_pos += 35
        
        # Save flyer
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/car_showcase_flyer_{timestamp}.svg"
        dwg.saveas(filename)
        
        return filename

def main():
    generator = CarFlyerGenerator()
    
    print("🚗 Creating Car-Themed Flyers...")
    
    # Generate different car flyers
    flyer1 = generator.create_car_dealership_flyer()
    print(f"✓ Created dealership flyer: {flyer1}")
    
    flyer2 = generator.create_car_showcase_flyer()
    print(f"✓ Created showcase flyer: {flyer2}")
    
    print(f"\n✨ Car flyer generation complete!")
    print(f"📁 Location: {os.path.abspath(generator.output_folder)}")

if __name__ == "__main__":
    main()