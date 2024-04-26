game.exe : game.bc graphics.bc utils.bc
        tx -E -o game.exe game.bc graphics.bc utils.bc

%.bc : %.grace
        tx -C $<
