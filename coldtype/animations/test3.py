from coldtype import *

fnt = Font.Cacheable("~/py/Fonts/OldschoolGroteskVarTrial.ttf")

cG = hsl(0.3333333333,1,0.36)
cB = hsl(0.66666666666,1,0.50)
cC = hsl(0.5,1,0.50)
cO = hsl(0.07222222222,1,0.50)
# cP = hsl(0.91388888888,1,0.50)
cP = hsl(0.83333333333,1,0.50)

@animation((1920, 1080),
            timeline=60,
            render_bg=cG,
            bg=cP
            )

def scratch(f):
    def styler(g):
        return Style(fnt, 400,
                # wght=f.e("qeio", 1),wdth=f.e("seio", 2)
                # wght=f.e("eeio", 1),wdth=f.e("qeio", 1)
                # wght=f.e("seio", 1),wdth=f.e("eeio", 1)
                wght=f.adj(-g.i*50).e("seio", 1)
                # wdth=f.adj(-g.i*100).e("qeio", 2)
                
                )
    
    return (Glyphwise("Eike", styler)
        .track(30, v=1)
        .xalign(f.a.r, th=1)
        .align(f.a.r, th=1)
        .f(cB)
        )

    # return (Glyphwise("The Rest Is", styler)
    #     .align(f.a.r, th=1)
    #     .f(cO)
    #     )

def release(passes):
    FFMPEGExport(scratch, passes, loops=4).h264().write()


# To start
# source . venv/bin/activate
# coldtype animations

# To render
# make sure preview is paused
# terminal > render_all
# in preview hit r
