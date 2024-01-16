import struct
import json
import os


def write_color(f, name, r, g, b):
    name_bytes = name.encode('utf-16be') + b'\x00\x00'
    name_length = len(name_bytes) // 2
    block_length = 2 + 4 + 2 + len(name_bytes) + 4 + 4 + 4 + 4 + 2

    f.write(b'\x00\x01')
    f.write(struct.pack('>i', block_length))  # i = int32
    f.write(struct.pack('>H', name_length))  # H = uint16
    f.write(name_bytes)
    f.write(b'RGB ')
    f.write(struct.pack('>f', r / 255))  # f = float32
    f.write(struct.pack('>f', g / 255))
    f.write(struct.pack('>f', b / 255))
    f.write(struct.pack('>h', 0))  # h = int16


def create_ase_file(filename, colors):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'wb') as f:
        f.write(b'ASEF')
        f.write(b'\x00\x01\x00\x00')
        f.write(struct.pack('>i', len(colors)))

        for name, r, g, b in colors:
            write_color(f, name, r, g, b)


def hex2rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))


def main():
    colors_file = os.path.join(os.path.dirname(__file__), 'colors.json')
    dist_file = os.path.join(os.path.dirname(__file__), '../dist/Tailwindcss.ase')
    colors = json.load(open(colors_file))
    swatch_colors = []

    for color in colors:
        for shade in colors[color]:
            swatch_colors.append((f'{color}-{shade}', *hex2rgb(colors[color][shade])))

    create_ase_file(dist_file, swatch_colors)


if __name__ == '__main__':
    main()
