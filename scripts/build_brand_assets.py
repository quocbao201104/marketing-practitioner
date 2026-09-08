"""Build repository branding from the approved vector kit (standard library only)."""

from pathlib import Path
import shutil
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "assets" / "logo-vector-20260908"
OUTPUT = ROOT / "assets" / "brand"
SVG = "http://www.w3.org/2000/svg"


def main():
    OUTPUT.mkdir(exist_ok=True)
    ET.register_namespace("", SVG)
    banner = ET.parse(KIT / "svg" / "lockup-color.svg").getroot()
    background = ET.Element(f"{{{SVG}}}rect", {
        "width": "2172", "height": "724", "fill": "#F7F3EB",
    })
    banner.insert(0, background)
    ET.ElementTree(banner).write(
        OUTPUT / "banner.svg", encoding="utf-8", xml_declaration=True,
    )
    for source, target in [
        ("symbol-color-512.png", "logo.png"),
        ("symbol-white-512.png", "logo-dark.png"),
    ]:
        shutil.copyfile(KIT / "png" / source, OUTPUT / target)
    print("Built banner.svg, logo.png, and logo-dark.png from the approved kit.")


if __name__ == "__main__":
    main()
