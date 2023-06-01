set key fixed top Right  vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid
unset parametric
set datafile separator ','

set title "::alg _ ::smp"

set key autotitle columnhead
set xlabel "Tamanho do vetor"
set ylabel "Tempo (H:M)"
set ydata time
set timefmt "%s.%s"
# set format y "%H:%M:%.4S"
# set format x "%.s*10^{%T}"
set format x "%2.0t*10^{%L}"
# set terminal png size 1920,1080 enhanced font "Helvetica,20"
# set output 'output.png'
# set multiplot layout 2,1 size 1024*scale,768*scale fontscale scale linewidth scale pointscale scale

scale = 1063.0/420.0

set terminal pngcairo size 1024*scale,768*scale fontscale scale linewidth scale pointscale scale
set output 'output.png'


NO_ANIMATION = 1
save_encoding = "utf8"
# plot './vetor_ordenado_asc_tempo_por_entrada.csv' using 2:1 with lines, '' using 3:1 with lines, '' using 4:1 with lines, '' using 5:1 with lines,'' using 6:1 with lines
# plot './vetor_ordenado_asc_tempo_por_entrada.csv' using 1:2 with lines linewidth 1.2, '' using 1:3 with lines linewidth 1.2, '' using 1:4 with lines linewidth 1.2, '' using 1:5 with lines linewidth 1.2,'' using 1:6 with lines linewidth 1.2,'' using 1:7 with lines linewidth 1.2,'' using 1:8 with lines linewidth 1.2,'' using 1:9 with lines linewidth 1.2 '' using 1:10 with lines linewidth 1.2
# set size 1.,1.
# set origin  0,.8
plot './vetor_ordenado_asc_tempo_por_entrada.csv' using 1:2 with lines linewidth 1.2, '' using 1:3 with lines linewidth 1.2, '' using 1:4 with lines linewidth 1.2,'' using 1:8 with lines linewidth 1.2

# set size 1.,1.
# set origin 0,0
set ylabel "Tempo (M:S)"
set terminal pngcairo size 1024*scale,768*scale fontscale scale linewidth scale pointscale scale
set output 'output2.png'
plot './vetor_ordenado_asc_tempo_por_entrada.csv' using 1:5 with lines linewidth 1.2,'' using 1:6 with lines linewidth 1.2,'' using 1:7 with lines linewidth 1.2,'' using 1:9 with lines linewidth 1.2 #, '' using 1:10 with lines linewidth 1.2
