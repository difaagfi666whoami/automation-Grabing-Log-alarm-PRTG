import xml.etree.ElementTree as ET
import os

# Mendefinisikan direktori yang berisi file XML
directory = "C:/Users/LENOVO/Downloads/data desember 24"

# Membuat elemen root untuk file XML gabungan
root = ET.Element("root")

# Loop melalui setiap file XML dalam direktori
for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        # Membaca file XML
        filepath = os.path.join(directory, filename)
        tree = ET.parse(filepath)
        xml_root = tree.getroot()

        # Menambahkan elemen-elemen dari file XML ke elemen root gabungan
        for child in xml_root:
            root.append(child)

# Membuat objek tree dari elemen root gabungan
combined_tree = ET.ElementTree(root)

# Menulis file XML gabungan
combined_tree.write("combinedDecember.xml", encoding="utf-8", xml_declaration=True)