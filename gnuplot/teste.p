#!/usr/local/bin/gnuplot -persist
# set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
# set output 'cerf.1.png'
set format y "%.2f" 
unset parametric
set samples 200, 200
set style data lines
set mxtics
set mytics
set xtics border out scale 1,0.5 nomirror norotate  autojustify
set title "Voigt Profile VP(x,Ïƒ,Î³)" 
set xrange [ -10.0000 : 10.0000 ] noreverse nowriteback
set x2range [ * : * ] noreverse writeback
set yrange [ 0.00000 : 0.300000 ] noreverse nowriteback
set y2range [ * : * ] noreverse writeback
set zrange [ * : * ] noreverse writeback
set cbrange [ * : * ] noreverse writeback
set rrange [ * : * ] noreverse writeback
set colorbox vertical origin screen 0.9, 0.2 size screen 0.05, 0.6 front  noinvert bdefault
NO_ANIMATION = 1
save_encoding = "utf8"
plot VP(x,1.53,0.0) title "Ïƒ=1.53 Î³=0.00",      VP(x,1.30,0.5) title "Ïƒ=1.30 Î³=0.50",      VP(x,1.00,1.0) title "Ïƒ=1.00 Î³=1.00",      VP(x,0.00,1.8) title "Ïƒ=0.00 Î³=1.80"

# to run gnuplot -pc ./gnuplot/teste.p