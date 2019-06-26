path=../input_data/aligns/tackle_data
files=$(ls $path)
for f in $files
do
	./raxmlHPC-PTHREADS-SSE3 -T 4 -s $path/$f -w /home/qikaiy2/Downloads/reu2019-tutorials/qikaiy2_project_1/output_data/trees/GTRCAT -m GTRCAT -V -p 12345 -n $f
done
