mkdir data/wsc
cd data/wsc
wget https://dl.fbaipublicfiles.com/glue/superglue/data/v2/WSC.zip
unzip WSC.zip
cp WSC/val.jsonl dev.jsonl
