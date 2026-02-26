#!/usr/bin/env python3
"""
Generate Serene Theme Wallpaper 1:
Combines Gradient Flows, Abstract Topography, and Gentle Curves
"""

from PIL import Image, ImageDraw
import math

# Serene Day Palette
SERENE_DAY = {
    'background': '#f5f2ed',      # Main background
    'surface': '#ebe6db',          # Secondary surface
    'muted': '#d4cfc4',            # Muted
    'subtle': '#b5ad9a',           # Subtle
    'text_muted': '#857c6d',       # Muted text
    'accent_green': '#657047',     # Primary green
    'accent_sage': '#5c7554',      # Sage
    'accent_olive': '#6d6555',     # Olive
    'accent_warm': '#8b6f47',      # Warm brown
    'accent_tan': '#9a6c3a',       # Tan
}

# Serene Night Palette
SERENE_NIGHT = {
    'background': '#1e1d1a',       # Main background
    'surface': '#2a2826',          # Secondary surface
    'muted': '#3d3a33',            # Muted
    'subtle': '#5a5549',           # Subtle
    'text_muted': '#857c6d',       # Muted text
    'accent_green': '#9fa883',     # Primary green
    'accent_sage': '#9aaa82',      # Sage
    'accent_olive': '#a89984',     # Olive
    'accent_warm': '#b8956d',      # Warm brown
    'accent_tan': '#d4a574',       # Tan
}


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def interpolate_color(color1, color2, factor):
    """Interpolate between two colors"""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return (r, g, b)


def create_gradient_base(width, height, palette, is_night=False):
    """Create a smooth gradient background"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Use background as solid base
    bg_color = hex_to_rgb(palette['background'])
    draw.rectangle([(0, 0), (width, height)], fill=bg_color)

    return img


def add_wave_layers(img, palette, is_night=False):
    """Add flowing wave layers using various colors from the palette"""
    width, height = img.size
    draw = ImageDraw.Draw(img, 'RGBA')

    # Define wave layers (from back to front) using various palette colors
    # Positioned to show background in top 40% (between 1/3 and 1/2)
    # Alpha values reduced by ~25% for more subtle, calming effect
    layers = [
        {
            'color': hex_to_rgb(palette['surface']),
            'alpha': 135,  # was 180
            'amplitude': height * 0.05,
            'frequency': 1.8,
            'y_base': height * 0.90,
            'phase': 0
        },
        {
            'color': hex_to_rgb(palette['muted']),
            'alpha': 120,  # was 160
            'amplitude': height * 0.06,
            'frequency': 2.2,
            'y_base': height * 0.80,
            'phase': 1.2
        },
        {
            'color': hex_to_rgb(palette['subtle']),
            'alpha': 100,  # was 140
            'amplitude': height * 0.055,
            'frequency': 1.5,
            'y_base': height * 0.68,
            'phase': 2.5
        },
        {
            'color': hex_to_rgb(palette['text_muted']),
            'alpha': 85,   # was 120
            'amplitude': height * 0.045,
            'frequency': 2.8,
            'y_base': height * 0.58,
            'phase': 0.8
        },
        {
            'color': hex_to_rgb(palette['accent_olive']),
            'alpha': 70,   # was 100
            'amplitude': height * 0.05,
            'frequency': 1.9,
            'y_base': height * 0.51,
            'phase': 3.0
        },
        {
            'color': hex_to_rgb(palette['accent_sage']),
            'alpha': 60,   # was 85
            'amplitude': height * 0.04,
            'frequency': 2.5,
            'y_base': height * 0.46,
            'phase': 1.7
        },
        {
            'color': hex_to_rgb(palette['accent_green']),
            'alpha': 50,   # was 70
            'amplitude': height * 0.035,
            'frequency': 2.0,
            'y_base': height * 0.42,
            'phase': 2.2
        },
        {
            'color': hex_to_rgb(palette['accent_warm']),
            'alpha': 42,   # was 60
            'amplitude': height * 0.03,
            'frequency': 3.2,
            'y_base': height * 0.39,
            'phase': 0.5
        },
    ]

    for layer in layers:
        # Create smooth flowing wave
        points = []
        for x in range(0, width + 1, 2):
            # Combine multiple sine waves for organic, flowing movement
            y = layer['y_base']
            y += layer['amplitude'] * math.sin(x / width * math.pi * layer['frequency'] + layer['phase'])
            y += layer['amplitude'] * 0.4 * math.sin(x / width * math.pi * layer['frequency'] * 1.6 + layer['phase'] + 1.5)
            y += layer['amplitude'] * 0.25 * math.sin(x / width * math.pi * layer['frequency'] * 2.4 + layer['phase'] + 3)
            points.append((x, int(y)))

        # Create filled polygon from curve to bottom
        polygon_points = points + [(width, height), (0, height)]
        color_with_alpha = layer['color'] + (layer['alpha'],)
        draw.polygon(polygon_points, fill=color_with_alpha)


def generate_wallpaper(width, height, theme='day', output_path='wallpaper.png'):
    """Generate complete wallpaper"""
    is_night = theme == 'night'
    palette = SERENE_NIGHT if is_night else SERENE_DAY

    # Create base
    img = create_gradient_base(width, height, palette, is_night)

    # Add wave layers
    add_wave_layers(img, palette, is_night)

    # Save
    img.save(output_path, 'PNG', optimize=True)
    print(f"Generated: {output_path}")


if __name__ == '__main__':
    # Generate all resolutions
    resolutions = [
        ('4k', 3840, 2160),
        ('qhd', 2560, 1440),
        ('fhd', 1920, 1080),
    ]

    print("Generating Wallpaper 1 in all resolutions...")

    for res_name, width, height in resolutions:
        print(f"\nGenerating {res_name.upper()} ({width}x{height})...")
        generate_wallpaper(width, height, 'day', f'serene-day-wallpaper1-{res_name}.png')
        generate_wallpaper(width, height, 'night', f'serene-night-wallpaper1-{res_name}.png')

    print("\n✓ All Wallpaper 1 variants generated successfully!")
