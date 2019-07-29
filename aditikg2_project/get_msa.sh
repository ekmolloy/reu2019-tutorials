
#!/bin/bash

cur="/projects/tallis/aditikg2/tutorials/aditikg2_project"
in="$cur/output/raxml_out/Scincella/*.bestTree"
control="$cur/input/indelible_in/Scincella/control.txt"
out="$cur/output/indelible_out/Scincella/"

for f in $in
do
    # Define paths and files
    rtf=${f/'.bestTree'/'.bestTree.tree'}
    base=$(basename $f)
    out_nm=${base/'.bestTree'/''}
    log=${f/'.bestTree'/'.log'}

    # Copy the sample control file
    cp $control "$cur/"
    
    # Get substitution rates & base frequenceis and write them to control file
    sub_rates=`grep -F 'Substitution rates (ML):' $log`
    sub_rates=${sub_rates/'Substitution rates (ML):'/''}
    base_freq=`grep -F 'Base frequencies (ML):' $log`
    base_freq=${base_freq/'Base frequencies (ML):'/''}
    sed -i "s/ JC /GTR$sub_rates\n[statefreq]$base_freq/g" "$cur/control.txt"

    # Root tree and write the rooted tree to the control file
    python3 root_tree.py $f $rtf
    tree=`cat $rtf`
    sed -i "s/(A:0.1,B:0.1);/${tree}/g" "$cur/control.txt"
    sed -i "s/:  0.00000000;/;/g" "$cur/control.txt"

    # Write the output file name
    sed -i "s/outputname/${out_nm}/g" "$cur/control.txt"

    # Run INDELible
    "$cur/indelible" "$cur/control.txt" 
    #rm "$cur/control.txt"

    # Move output files to the output directory
    mv "$cur/${out_nm}.fas" $out
    mv "$cur/${out_nm}_TRUE.phy" $out
done
