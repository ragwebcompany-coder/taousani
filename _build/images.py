from PIL import Image, ImageOps
import os
SRC="/Users/apostolospollalis/Downloads/wetransfer_biolab_2026-09-07_1222"
DST=SRC+"/biolab-site/assets/images"
def s(n): return f"{SRC}/biolab-mikroviologiko-serres {n}.jpg" if n else SRC+"/biolab-mikroviologiko-serres.jpg"
def sj(n): return f"{SRC}/biolab-mikroviologiko-serres ({n}).jpeg"

MAP = {
 # name            source                 max-width
 "hero":           (s("(44)"),  2000),
 "hero-mobile":    (s("(33)"),  1100),
 "about-lab":      (s("(33)"),  1500),
 "brand-wall":     (s("(15)"),  1400),
 "facility-clean": (s("(17)"),  1600),
 "facility-hood":  (s("(18)"),  1100),
 "facility-seq":   (s("(16)"),  1100),
 "facility-analyzer": (sj(2),   1400),
 "exam-room":      (sj(1),      1100),
 "cta-band":       (s("(42)"),  1900),
 "quality":        (s("(49)"),  1500),
 "tubes":          (s("(10)"),  1300),
 "plate":          (s("(24)"),  1300),
 "pipette":        (s("(45)"),  1200),
 "pcr":            (s("(12)"),  1300),
 "portrait-work":  (s("(23)"),  1000),
 "cylinders":      (s("(5)"),    900),
 "team":           (s("(51)"),  1100),
 "rack":           (s("(54)"),  1100),
 "vortex":         (s("(36)"),  1400),
 "strip":          (s("(8)"),   1300),
 "analyzer-room":  (sj(3),      1100),
 "tube-pipette":   (s("(53)"),  1400),
 "scientist-blue": (s("(50)"),  1100),
 "monitor":        (s("(3)"),   1300),
 "hands-rack":     (s("(20)"),  1200),
 "hood-blue":      (s("(14)"),  1500),
 "cabinet":        (s("(13)"),  1000),
 "gallery-1":      (s("(31)"),  1000),
 "gallery-2":      (s("(41)"),  1200),
 "gallery-3":      (s("(47)"),   900),
 "gallery-4":      (s("(7)"),    900),
 "gallery-5":      (s("(55)"),   900),
 "gallery-6":      (s("(48)"),  1200),
}
for name,(src,w) in MAP.items():
    im=Image.open(src); im=ImageOps.exif_transpose(im).convert("RGB")
    if im.width>w: im=im.resize((w,round(im.height*w/im.width)), Image.LANCZOS)
    im.save(f"{DST}/{name}.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    im.save(f"{DST}/{name}.webp","WEBP", quality=78, method=6)
    print(name, im.size, os.path.getsize(f"{DST}/{name}.jpg")//1024,"KB jpg /",os.path.getsize(f"{DST}/{name}.webp")//1024,"KB webp")
# social share image
im=Image.open(s("(44)")); im=ImageOps.exif_transpose(im).convert("RGB")
im=ImageOps.fit(im,(1200,630),Image.LANCZOS); im.save(DST+"/og-image.jpg","JPEG",quality=82,optimize=True)
print("total dir KB:", sum(os.path.getsize(os.path.join(DST,f)) for f in os.listdir(DST))//1024)
