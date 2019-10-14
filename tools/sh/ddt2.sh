to_skip=$1
to_read=$2
chunk_size=$3
echo "Skipping [$to_skip] byte"
echo "Reading [$to_read] bytes"
echo "Chunk size [$3] bytes"
echo "Num of chunks: $(($2/($3)))"
echo "Offset: $(($2%$3))"

{ dd count=0 skip="$to_skip" bs=1
  dd count="$((to_read/(chunk_size)))" bs=$3
  dd count=1 bs="$((to_read%chunk_size))"
} < $4 > ./out.tmp

echo "
"
cat ./out.tmp
echo "
"
