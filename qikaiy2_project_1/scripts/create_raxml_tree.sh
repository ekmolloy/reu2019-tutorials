path=../input_data/aligns/tackle_data
files=$(ls $path)
for f in $files
do
	./raxmlHPC-PTHREADS-SSE3 -T 4 -s $path/$f -w /home/qikaiy2/Downloads/qikaiy2_project_1/output_data/trees/GTRGAMMA -m GTRGAMMA -p 12345 -n $f
done
