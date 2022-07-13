from this import d
from coldtype import *

fnt = Font.Cacheable("~/py/Fonts/OldschoolGroteskVarTrial.ttf")

# Bright colours

# Red
cR = hsl(0,1,0.50)
# Lime
cL = hsl(0.3333333333,1,0.50)
# Blue
cB = hsl(0.66666666666,1,0.50)
# Cyan
cC = hsl(0.5,1,0.50)
# Yellow
cY = hsl(0.166666667, 1, 0.5)
# Magenta
cP = hsl(0.83333333333,1,0.50)

# Midtone colours

# Dark green
dG = hsl(0.2, 0.25, 0.392)
# Dark red
dR = hsl(0, 0.708, 0.529)
# Dark red
dR2 = hsl(0.0194, 0.647, 0.50)
# Dark brown1
dB1 = hsl(0.0583333333, 0.437, 0.687)
# Dark brown2
dB2 = hsl(0.0444444444, 0.451, 0.50)
# Dark brown3
dB3 = hsl(0.0694444444, 1, 0.373)
# Dark pink
dP = hsl(0.894444444, 1, 0.461)
# Dark Yellow
dY = hsl(0.113888889,1,0.559)
# Dark Khaki
dK = hsl(0.166666667,1,0.343)
# Purple
dPu = hsl(0.722222222,0.882,0.667)
# Purple 2
dPu2 = hsl(0.916666667,0.2,0.608)
# Purple 3
dPu3 = hsl(0.666666667, 1, 0.863)

# Light colours

# Light Pink 1
lP1 = hsl(1.02564103,0.28,0.755)
# Light Pink 2
lP2 = hsl(0.025,1,0.873)
# Light Pink 3 update
lP3 = hsl(0,1,0.873)

# Light Yellow 1
lY1 = hsl(0.125,0.571,0.863)
# Light Yellow 2 update
lY2 = hsl(0.125,0.571,0.863)
# Light Yellow 3
lY3 = hsl(0.166666667,0.231,0.873)

# 900, 600, 500/105, 420/97, 400, 350/90, 450, 290/70, 250/80, 180

# Social small
# 140 / 50

# Social medium
# 165 / 50

# Social larger
# 365 / 50

bgC = dPu3
fgC = cR
fSize = 165
fTrack = 50
words = "slv.vic.gov.au"
words2 = "MELBOURNE\nFRINGE\nFESTIVAL"


@animation((1080, 1080),
            timeline=90,
            render_bg=bgC, 
            bg=bgC
            )

def scratch(f):
    def styler(g):
        return Style(fnt, fSize,
                wght=f.adj(-g.i*100).e("eeio", 1),  
        )

    return (Glyphwise(words2, styler)
        .track(fTrack, v=1)
        .xalign(f.a.r, th=1)
        .align(f.a.r, th=1)
        .f(fgC)
        )    

    # return (Glyphwise(words, styler)
    #     .align(f.a.r, th=1)
    #     .f(fgC)
    #     )

def release(passes):
    FFMPEGExport(scratch, passes, loops=4).h264().write().open()


# To start
# source ./venv/bin/activate
# coldtype animations

# To render
# make sure preview is paused
# terminal > render_all
# in preview hit r
