from coldtype import *

fnt = Font.Cacheable("~/py/Fonts/OldschoolGroteskVarTrial.ttf")

# Green
cG = hsl(0.3333333333,1,0.36)
# Dark green
dG = hsl(0.166666667, 1, 0.345)
# Lime
cL = hsl(0.3333333333,1,0.50)

cB = hsl(0.66666666666,1,0.50)
cC = hsl(0.5,1,0.50)
cO = hsl(0.07222222222,1,0.50)
# Dark Yellow
dY = hsl(0.113888889,1,0.559)
# Light Yellow
lY = hsl(0.166666667,0.753,0.841)

# Pink or Magenta
cP = hsl(0.83333333333,1,0.50)
# Light Pink
lP = hsl(0.025,1,0.875)
# Purple
cPu = hsl(0.666666667,1,0.861)

# Red
cR = hsl(0,1,0.50)

@animation((1920, 1080),
            timeline=90,
            render_bg=cB,
            bg=cB
            )

def scratch(f):
    def styler(g):
        # Font size 650-single
        # Font size 500-double
        # Font size 390-triple
        # Font size 800-big
        return Style(fnt, 350,
                # wght=f.e("qeio", 1),wdth=f.e("seio", 2)
                # wght=f.e("eeio", 1),wdth=f.e("qeio", 1)
                # wght=f.e("seio", 2),wdth=f.e("eeio", 1)
                # wght=f.adj(-g.i*50).e("seio", 1),     
                wght=f.adj(-g.i*100).e("eeio", 1),
                # wdth=f.adj(-g.i*100).e("eeio", 1)
                
                )
    
    # return (Glyphwise("The Rest\nIs Up\nTo You", styler)
    #     .track(50, v=1)
    #     .xalign(f.a.r, th=1)
    #     .align(f.a.r, th=1)
    #     .f(cL)
    #     )

    return (Glyphwise("The Rest\nIs Up\nTo You", styler)
        .track(90, v=1)
        .xalign(f.a.r, th=1)
        .align(f.a.r, th=1)
        .f(cL)
        )    

    # return (Glyphwise("1982-2042", styler)
    #     .align(f.a.r, th=1)
    #     .f(cPu)
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
