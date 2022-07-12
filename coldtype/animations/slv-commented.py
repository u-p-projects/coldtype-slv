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

# Light colours

# Light Pink 1
lP1 = hsl(1.02564103,0.28,0.755)
# Light Pink 2
lP2 = hsl(0.025,1,0.873)
# Light Pink 3 update
lP3 = hsl(0,1,0.873)

# Light Yellow 1
lP1 = hsl(0.125,0.571,0.863)
# Light Yellow 2 update
lP1 = hsl(0.125,0.571,0.863)
# Light Yellow 3
lP3 = hsl(0.166666667,0.231,0.873)

bgC = dG
fgC = cP
fSize = 600
words = "HOST"



@animation((1920, 1080),
            timeline=90,
            render_bg=bgC, 
            bg=bgC
            )

def scratch(f):
    def styler(g):
        # Font size 650-single
        # Font size 500-double
        # Font size 390-triple
        # Font size 750-big
        return Style(fnt, fSize,
                # wght=f.e("qeio", 1),wdth=f.e("seio", 2)
                # wght=f.e("eeio", 1),wdth=f.e("qeio", 1)
                # wght=f.e("seio", 2),wdth=f.e("eeio", 1)
                wght=f.adj(-g.i*100).e("eeio", 1),  
                # wght=0.05,     
                # wght=f.adj(-g.i*100).e("eeio", 1),
                # wdth=f.adj(-g.i*100).e("eeio", 1)
                
                )
    
    # return (Glyphwise("FIELD\nTHEORY", styler)
    #     .track(50, v=1)
    #     .xalign(f.a.r, th=1)
    #     .align(f.a.r, th=1)
    #     .fill(cC)
    #     )

    # return (Glyphwise("Oct 06 2022\nJul 25 2023", styler)
    #     .track(60, v=1)
    #     .xalign(f.a.r, th=1)
    #     .align(f.a.r, th=1)
    #     .f(cB)
    #     )    

    return (Glyphwise(words, styler)
        .align(f.a.r, th=1)
        .f(fgC)
        )

def release(passes):
    FFMPEGExport(scratch, passes, loops=4).h264().write().open()


# To start
# source ./venv/bin/activate
# coldtype animations

# To render
# make sure preview is paused
# terminal > render_all
# in preview hit r
