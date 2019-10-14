to_skip=$1
to_read=$2
chunk_size=$3
in_file=$4
{ dd count=0 skip="$to_skip" bs=1
  dd count="$((to_read/(chunk_size)))" bs=$3
  dd count=1 bs="$((to_read%chunk_size))"
} < $in_file #> ./out.tmp

#cat ./out.tmp
