import struct, zlib, os

def make_png(width, height, pixels):
    def chunk(name, data):
        c = zlib.crc32(name + data) & 0xffffffff
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', c)
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    raw = b''
    for row in pixels:
        raw += b'\x00'
        for r, g, b in row:
            raw += bytes([r, g, b])
    idat = zlib.compress(raw)
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr) + chunk(b'IDAT', idat) + chunk(b'IEND', b'')

BLUE   = (0, 87, 168)
YELLOW = (245, 197, 24)
GREEN  = (0, 154, 68)

def flag_pixels(w, h):
    rows = []
    for y in range(h):
        row = []
        third = h / 3
        if y < third:
            color = BLUE
        elif y < 2 * third:
            color = YELLOW
        else:
            color = GREEN
        for x in range(w):
            row.append(color)
        rows.append(row)
    return rows

script_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(script_dir, "static")
os.makedirs(static_dir, exist_ok=True)

sizes = [
    ("favicon-16x16.png",   16,  16),
    ("favicon-32x32.png",   32,  32),
    ("favicon-48x48.png",   48,  48),
    ("apple-touch-icon.png",180, 180),
]

for filename, w, h in sizes:
    path = os.path.join(static_dir, filename)
    pixels = flag_pixels(w, h)
    data = make_png(w, h, pixels)
    with open(path, 'wb') as f:
        f.write(data)
    print("Created: " + filename + " (" + str(w) + "x" + str(h) + ")")

ico_path = os.path.join(static_dir, "favicon.ico")
sizes_ico = [(16, 16), (32, 32), (48, 48)]
images = []
for w, h in sizes_ico:
    pixels = flag_pixels(w, h)
    png_data = make_png(w, h, pixels)
    images.append((w, h, png_data))

num_images = len(images)
dir_size = 6 + num_images * 16
offsets = []
offset = dir_size
for w, h, data in images:
    offsets.append(offset)
    offset += len(data)

ico = struct.pack('<HHH', 0, 1, num_images)
for i, (w, h, data) in enumerate(images):
    ico += struct.pack('<BBBBHHII',
        w if w < 256 else 0,
        h if h < 256 else 0,
        0, 0, 1, 24,
        len(data),
        offsets[i]
    )
for w, h, data in images:
    ico += data

with open(ico_path, 'wb') as f:
    f.write(ico)
print("Created: favicon.ico (16x16 + 32x32 + 48x48)")

print("\nAll favicon files written to static/")
print("Next: git add static/favicon* static/apple-touch-icon.png && git commit && git push")
