set key fixed top Right  vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid
unset parametric
set datafile separator ','

set title "::alg _ ::smp"

set key autotitle columnhead
set xlabel "Tamanho do vetor"
set ylabel "Trocas"

scale = 1063.0/420.0

set terminal pngcairo size 1024*scale,768*scale fontscale scale linewidth scale pointscale scale
set output 'output.png'


NO_ANIMATION = 1
save_encoding = "utf8"

plot './vetor_ordenado_asc_trocas_por_entrada.csv' using 1:3 with lines linewidth 1.2, '' using 1:5 with lines linewidth 1.2,'' using 1:6 with lines linewidth 1.2,'' using 1:7 with lines linewidth 1.2,'' using 1:9 with lines linewidth 1.2, '' using 1:10 with lines linewidth 1.2
set terminal pngcairo size 1024*scale,768*scale fontscale scale linewidth scale pointscale scale
set output 'output2.png'
plot './vetor_ordenado_asc_trocas_por_entrada.csv' using 1:2 with lines linewidth 1.2, '' using 1:4 with lines linewidth 1.2,'' using 1:8 with lines linewidth 1.2