path="/projects/tallis/qikaiy2/reu2019-tutorials/qikaiy2_project_1/input_data/aligns/paper_data"
files=$(ls $path)
for f in $files
do
	echo "h"
	python3 seqtools.py -f p -i $path/$f -o /projects/tallis/qikaiy2/reu2019-tutorials/qikaiy2_project_1/input_data/aligns/phy_data/$f.phy
done
