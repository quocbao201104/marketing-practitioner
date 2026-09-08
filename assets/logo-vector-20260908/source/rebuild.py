"""Rebuild the vector kit from master.json and the bundled, unmodified OFL font.
Python 3.13; fonttools, uharfbuzz, resvg-py, svglib, reportlab, Pillow, numpy, pypdf.
Optional --deps PATH loads an isolated Python dependency directory.
"""
import sys, argparse, json, hashlib, io, copy
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument("--deps")
args=parser.parse_args()
if args.deps: sys.path.insert(0,args.deps)
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.svgLib.path import parse_path
import uharfbuzz as hb
import resvg_py
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from pypdf import PdfReader
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/"source"
REF=ROOT.parent/"logo-20260908"
M=json.loads((SOURCE/"master.json").read_text(encoding="utf-8"))
for d in ("svg","png","favicon","pdf","qa"): (ROOT/d).mkdir(exist_ok=True)
reference_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in REF.glob("*") if p.is_file()}
font_path=SOURCE/M["lockup"]["font"]["file"]
font_bytes=font_path.read_bytes()
font=instantiateVariableFont(TTFont(font_path),{"wght":M["lockup"]["font"]["weight"]},inplace=False)
glyphs=font.getGlyphSet()
order=font.getGlyphOrder()
upem=font["head"].unitsPerEm
hf=hb.Font(hb.Face(font_bytes))
hf.scale=(upem,upem)
hf.set_variations({"wght":M["lockup"]["font"]["weight"]})
hb.ot_font_set_funcs(hf)
size=M["lockup"]["font"]["size"]
tracking=M["lockup"]["font"]["tracking"]

def polygon(points):
    return "M"+" L".join(f"{x:g} {y:g}" for x,y in points)+" Z"

def word_path(text,x,y):
    buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties()
    hb.shape(hf,buf,{"kern":True,"liga":False})
    pen=SVGPathPen(glyphs)
    offset=0
    for info,pos in zip(buf.glyph_infos,buf.glyph_positions):
        matrix=(size/upem,0,0,-size/upem,x+offset+pos.x_offset*size/upem,y-pos.y_offset*size/upem)
        glyphs[order[info.codepoint]].draw(TransformPen(pen,matrix))
        offset+=pos.x_advance*size/upem+tracking
    return pen.getCommands(),offset-tracking

def fitted_word(line):
    path,width=word_path(line["text"],0,0)
    bp=BoundsPen(None);parse_path(path,bp)
    x0,y0,x1,y1=bp.bounds
    a,b,c,d=line["targetInkBox"]
    sx=(c-a)/(x1-x0);sy=(d-b)/(y1-y0)
    matrix=(sx,0,0,sy,a-sx*x0,b-sy*y0)
    pen=SVGPathPen(None);parse_path(path,TransformPen(pen,matrix))
    return pen.getCommands(),width*sx,matrix

word_geometry=[fitted_word(l) for l in M["lockup"]["lines"]]
def symbol_content(spec,pal,transform=None):
    t=f' transform="{transform}"' if transform else ""
    return f'<g id="symbol"{t}><path id="frame" fill="{pal["frame"]}" d="{polygon(spec["frame"])}"/><path id="evidence-tab" fill="{pal["tab"]}" d="{polygon(spec["tab"])}"/></g>'
def document(kind,variant,editable=False):
    pal=M["palette"][variant]
    spec=M["symbol"] if kind=="symbol" else M["lockup"] if kind=="lockup" else M["favicon"]
    vb=" ".join(map(str,spec["viewBox"]))
    width,height=spec["viewBox"][2:]
    content=""
    if kind=="lockup":
        t=spec["symbol"]
        content=symbol_content(M["symbol"],pal,f'translate({t["x"]} {t["y"]}) scale({t["scale"]})')
        for i,l in enumerate(spec["lines"]):
            if editable:
                mt=" ".join(f"{n:.9f}" for n in word_geometry[i][2])
                content+=f'<text x="0" y="0" transform="matrix({mt})" font-family="Montserrat" font-weight="800" font-size="{size}" letter-spacing="{tracking}" fill="{pal["text"]}">{l["text"]}</text>'
            else:
                content+=f'<path id="word-{i+1}" fill="{pal["text"]}" d="{word_geometry[i][0]}"/>'
    else: content=symbol_content(spec,pal)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{vb}" role="img" aria-label="Marketing Practitioner"><title>Marketing Practitioner</title><desc>Open field symbol. {"Editable Montserrat 800 text; font required." if editable else "True vector paths; no raster images, fonts or external resources."}</desc>{content}</svg>'

def raster(svg,width=None,height=None):
    return Image.open(io.BytesIO(resvg_py.svg_to_bytes(svg_string=svg,width=width,height=height,skip_system_fonts=True))).convert("RGBA")
def save_text(p,s): p.write_text(s,encoding="utf-8",newline="\n")

for kind in ("symbol","lockup"):
    for variant in M["palette"]:
        s=document(kind,variant)
        save_text(ROOT/"svg"/f"{kind}-{variant}.svg",s)
        raster(s).save(ROOT/"qa"/f"{kind}-{variant}-render.png")
        if kind=="symbol":
            for n in (32,64,128,256,512,1024):
                raster(s,n,n).save(ROOT/"png"/f"symbol-{variant}-{n}.png")
save_text(SOURCE/"lockup-editable.svg",document("lockup","color",editable=True))
for variant in M["palette"]:
    save_text(ROOT/"favicon"/f"favicon-optical-{variant}.svg",document("favicon",variant))
favimgs=[raster(document("favicon","color"),n,n) for n in (16,32,48)]
favimgs[-1].save(ROOT/"favicon"/"favicon.ico",format="ICO",sizes=[(16,16),(32,32),(48,48)],append_images=favimgs[:-1])

pdf_path=ROOT/"pdf"/"marketing-practitioner-vector.pdf"
c=canvas.Canvas(str(pdf_path))
c.setTitle("Marketing Practitioner — Vector logo kit")
c.setAuthor("Marketing Practitioner")
for variant in M["palette"]:
    for kind in ("symbol","lockup"):
        s=document(kind,variant)
        drawing=svg2rlg(io.BytesIO(s.encode()))
        target_width=288 if kind=="symbol" else 576
        scale=target_width/drawing.width
        w,h=target_width,drawing.height*scale
        c.setPageSize((w,h))
        if variant=="white":
            c.setFillColorRGB(9/255,45/255,53/255)
            c.rect(0,0,w,h,fill=1,stroke=0)
        c.saveState(); c.scale(scale,scale)
        renderPDF.draw(drawing,c,0,0)
        c.restoreState();c.showPage()
c.save()

# QA composition; all delivered artwork comes from the SVG paths above.
ui_font=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",18)
small_font=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",14)
def background(image,color):
    out=Image.new("RGBA",image.size,color);out.alpha_composite(image);return out.convert("RGB")
board=Image.new("RGB",(1200,690),"#F7F3EB");draw=ImageDraw.Draw(board)
for i,v in enumerate(M["palette"]):
    bg="#092D35" if v=="white" else "#F7F3EB"
    draw.rectangle((0,i*230,1200,(i+1)*230),fill=bg)
    draw.text((22,i*230+16),v,font=ui_font,fill="white" if v=="white" else "#092D35")
    icon=background(raster(document("symbol",v),190,190),bg)
    lock=background(raster(document("lockup",v),660,220),bg)
    board.paste(icon,(140,i*230+20));board.paste(lock,(420,i*230+5))
board.save(ROOT/"qa"/"vector-overview.png")

small=Image.new("RGB",(1100,710),"white");d=ImageDraw.Draw(small)
for row,v in enumerate(M["palette"]):
    d.text((16,20+row*160),v,font=ui_font,fill="black")
    for col,n in enumerate((16,32,64,128)):
        bg="#092D35" if v=="white" else "#F7F3EB"
        im=background(raster(document("symbol",v),n,n),bg)
        x=210+col*190;y=20+row*160
        small.paste(im,(x,y));d.text((x,y+134),str(n)+" px",font=small_font,fill="black")
d.text((16,525),"Favicon optical",font=ui_font,fill="black")
for col,n in enumerate((16,32,48)):
    im=background(favimgs[col],"#F7F3EB");x=210+col*190
    small.paste(im,(x,525));d.text((x,590),str(n)+" px",font=small_font,fill="black")
d.text((16,652),"Normal symbol geometry is unchanged. Favicon uses a separate pixel-aligned aperture.",font=small_font,fill="black")
small.save(ROOT/"qa"/"small-size-check.png")

# Comparison and deterministic checks.
ref_symbol=Image.open(REF/"symbol-color-light.png").convert("RGB")
ref_lock=Image.open(REF/"lockup-color-light.png").convert("RGB")
render_symbol=raster(document("symbol","color"))
render_lock=raster(document("lockup","color"))
def foreground(im):
    a=np.array(im)
    return (a[:,:,0]<100)&(a[:,:,1]<190)&((a[:,:,1].astype(int)-a[:,:,0].astype(int))>5)
refmask=foreground(ref_symbol)
vmask=np.array(render_symbol)[:,:,3]>127
iou=float((refmask&vmask).sum()/(refmask|vmask).sum())
intersection=np.zeros((1254,1254,3),np.uint8)+245
intersection[refmask]=[228,80,120]
intersection[vmask]=[30,135,185]
intersection[refmask&vmask]=[9,45,53]
Image.fromarray(intersection).save(ROOT/"qa"/"symbol-overlay.png")
comparison=Image.new("RGB",(1200,780),"#F7F3EB");d=ImageDraw.Draw(comparison)
d.text((20,18),"PNG reference",font=ui_font,fill="black");d.text((620,18),"Vector reconstruction / Montserrat 800",font=ui_font,fill="black")
comparison.paste(ref_symbol.resize((260,260)),(150,60))
comparison.paste(background(render_symbol.resize((260,260)),"#F7F3EB"),(750,60))
comparison.paste(ref_lock.resize((580,193)),(10,390))
comparison.paste(background(render_lock.resize((580,193)),"#F7F3EB"),(610,390))
d.text((20,640),"Symbol overlay IoU: "+f"{iou:.4f}"+". Typography is an identified replacement, not a claimed font match.",font=small_font,fill="black")
d.text((20,675),"Lockup symbol is a uniform 0.59x instance of the master; no independent retracing.",font=small_font,fill="black")
comparison.save(ROOT/"qa"/"reference-comparison.png")

checks={}
ns={"s":"http://www.w3.org/2000/svg"}
for kind in ("symbol","lockup"):
    signatures=[]
    alphas=[]
    for v in M["palette"]:
        root=ET.parse(ROOT/"svg"/f"{kind}-{v}.svg").getroot()
        assert not root.findall(".//s:image",ns)
        assert not root.findall(".//s:text",ns)
        assert all("href" not in k for e in root.iter() for k in e.attrib)
        signatures.append([(e.tag,e.get("d"),e.get("transform")) for e in root.iter() if e.tag.endswith(("path","g"))])
        im=raster(document(kind,v))
        assert im.getchannel("A").getextrema()==(0,255)
        alphas.append(np.array(im)[:,:,3])
    assert signatures[0]==signatures[1]==signatures[2]
    assert np.array_equal(alphas[0],alphas[1]) and np.array_equal(alphas[1],alphas[2])
    checks[kind+"_geometry_and_alpha_identical"]=True
for n in (32,64,128,256,512,1024):
    alpha=[]
    for v in M["palette"]:
        im=Image.open(ROOT/"png"/f"symbol-{v}-{n}.png")
        assert im.mode=="RGBA" and im.size==(n,n)
        assert im.getchannel("A").getextrema()==(0,255)
        assert im.getpixel((0,0))[3]==0
        alpha.append(np.array(im)[:,:,3])
    assert all(np.array_equal(alpha[0],a) for a in alpha[1:])
ico=Image.open(ROOT/"favicon"/"favicon.ico")
assert ico.ico.sizes()=={(16,16),(32,32),(48,48)}
for s in ico.ico.sizes():
    im=ico.ico.getimage(s)
    assert im.convert("RGBA").getchannel("A").getextrema()==(0,255)
    assert np.array_equal(np.array(im.convert("RGBA")),np.array(raster(document("favicon","color"),*s)))
reader=PdfReader(pdf_path)
assert len(reader.pages)==6
for page in reader.pages:
    assert len(page.images)==0
    data=page.get_contents().get_data()
    assert b" m" in data and b" l" in data
    assert b"Tj" not in data and b"TJ" not in data
editable_bytes=resvg_py.svg_to_bytes(svg_path=str(SOURCE/"lockup-editable.svg"),font_files=[str(font_path)],skip_system_fonts=True)
(ROOT/"qa"/"editable-render.png").write_bytes(editable_bytes)
editable_mask=np.array(Image.open(io.BytesIO(editable_bytes)).convert("RGBA"))[:,:,3]>127
outlined_mask=np.array(render_lock)[:,:,3]>127
editable_iou=float((editable_mask&outlined_mask).sum()/(editable_mask|outlined_mask).sum())
assert editable_iou>0.995
assert reference_hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in REF.glob("*") if p.is_file()}
checks.update(svg_distribution_files=6,svg_image_elements=0,svg_text_elements=0,
 png_rgba_files=18,png_sizes=[32,64,128,256,512,1024],ico_sizes=[16,32,48],
 pdf_pages=6,pdf_raster_images=0,pdf_text_drawing_operators=0,symbol_threshold_mask_iou=iou,editable_vs_outlined_mask_iou=editable_iou,
 reference_files_unchanged=True,font_sha256=hashlib.sha256(font_bytes).hexdigest(),
 font_version=font["name"].getDebugName(5),word_advance_widths=[v[1] for v in word_geometry],word_optical_transforms=[v[2] for v in word_geometry])
save_text(ROOT/"qa"/"verification.json",json.dumps(checks,indent=2))
save_text(SOURCE/"reference-sha256.json",json.dumps(reference_hashes,indent=2))
print(json.dumps(checks,indent=2))
