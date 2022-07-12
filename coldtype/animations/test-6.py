from coldtype import *

fnt = Font.Cacheable("~/py/Fonts/OldschoolGroteskVarTrial.ttf")

cG = hsl(0.3333333333,1,0.36)
cB = hsl(0.66666666666,1,0.50)
cC = hsl(0.5,1,0.50)
cO = hsl(0.07222222222,1,0.50)
# cP = hsl(0.91388888888,1,0.50) magenta pink
cP = hsl(0.83333333333,1,0.50)
cR = hsl(0,1,0.50)
cL = hsl(0.333333333,1,0.50)
cBrown = hsl(0.133333333, 0.757, 0.5)
cLg = hsl(0.34722222222, 0.36, 0.6)
cLav = hsl(0.666666667, 1, 0.861)

@animation((1920, 1080),
            timeline=90,
            render_bg=cG,
            bg=cG
            )

def scratch(f):
    
    def styler(g):
        return Style(fnt, 800,
                # wght=f.e("qeio", 1),wdth=f.e("seio", 2)
                # wght=f.e("eeio", 1),wdth=f.e("qeio", 1)
                # wght=f.e("seio", 1),wdth=f.e("eeio", 1)
                # wght=f.adj(-g.i*10).e("seio", 1)
                wdth=f.adj(-g.i*20).e("eeio", 1)
                
                )

    def styler2(g):
        return Style(fnt, 100,
                # wght=f.e("qeio", 1),wdth=f.e("seio", 2)
                # wght=f.e("eeio", 1),wdth=f.e("qeio", 1)
                # wght=f.e("seio", 1),wdth=f.e("eeio", 1)
                wght=(0.8)
                # wght=f.adj(-g.i*10).e("seio", 1)
                # wdth=f.adj(-g.i*100).e("qeio", 2)
                
                )                
    
    txt = (
        # Glyphwise("The Rest\nIs Up\nTo You", styler)
        # .track(30, v=1)
        # .xalign(f.a.r, th=1)
        # .align(f.a.r, th=1)
        # .f(cO)

        Glyphwise("2042", styler)
        .align(f.a.r, th=1)
        .f(cLav)
        )

    txt2 = (Glyphwise("Melbourne Fringe Festival 1982-2062", styler2)
        .align(f.a.r, th=1)
        .f(0)
        ) 
    # return (
    #     Glyphwise("The Rest Is", styler)
    #     .align(f.a.r, th=1)
    #     .f(cO)
    #     )

    return (
        txt,
        # txt2.translate(0, 0),
    )

def release(passes):
    FFMPEGExport(scratch, passes, loops=4).h264().write().open()


# To start
# source . venv/bin/activate
# coldtype animations

# To render
# make sure preview is paused
# terminal > render_all
# in preview hit r
