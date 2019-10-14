   { dd count=0 skip=$h bs=1
     dd count=4 bs=2
   #  dd count=1 bs=1
   } <./in.tmp>./out.tmp
echo $i
