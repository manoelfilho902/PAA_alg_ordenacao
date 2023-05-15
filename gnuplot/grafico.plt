set key fixed center Right  vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid
unset parametric
set datafile separator ','

set title "::alg _ ::smp"
set xdata time
set timefmt "%Y-%m-%dT%H:%M:%S"
set format x "%H:%M:%S"
set key autotitle columnhead
set ylabel "Uma coisa"
set xlabel "Outra coisa"

set style line 101 lw 3 lt rgb "#f62aa0" # style for targetValue (1) (pink)
set style line 102 lw 3 lt rgb "#26dfd0" # style for measuredValue (2) (light blue)
set style line 103 lw 4 lt rgb "#b8ee30" # style for secondYAxisValue (3) (limegreen)

NO_ANIMATION = 1
save_encoding = "utf8"
plot './test.csv' using 1:2 with lines ls 101, '' using 1:3 with lines ls 102, '' using 1:4 with lines ls 103 axis x1y2