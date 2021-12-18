mkdir data/wic
cd data/wic
wget https://dl.fbaipublicfiles.com/glue/superglue/data/v2/WiC.zip
unzip WiC.zip
cp WiC/val.jsonl dev.jsonl
