from coldtype import *

fnt = Font.Cacheable("~/py/Fonts/ABCSocialPlusVariable-Trial.ttf")

cG = hsl(0.3333333333,1,0.36)
cB = hsl(0.6,1,0.50)
cO = hsl(0.07222222222,1,0.50)
cP = hsl(0.91388888888,1,0.50)

@animation((1920, 1080),
            timeline=60,
            render_bg=cG,
            bg=cG
            )

def scratch(f):
    def styler(g):
        return Style(fnt, 900,
                # wght=f.e("qeio", 1),wdth=f.e("seio", 2)
                # wght=f.e("eeio", 1),wdth=f.e("qeio", 2)
                # wght=f.e("seio", 2),wdth=f.e("eeio", 1)
                wdth=f.adj(-g.i*200).e("seio", 1)
                
                )
    
    # return (Glyphwise("FIELD\nTHEORY", styler)
    #     .track(30, v=1)
    #     .xalign(f.a.r, th=1)
    #     .align(f.a.r, th=1)
    #     .f(cO)
    #     )

    return (Glyphwise("YOU", styler)
        .align(f.a.r, th=1)
        .f(cP)
        )

def release(passes):
    FFMPEGExport(scratch, passes, loops=4).h264().write()

# To start
# source venv/bin/activate
# coldtype animations

# To render
# make sure preview is paused
# terminal > render_all
# in preview hit r

