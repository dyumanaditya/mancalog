module load anaconda/py3
source activate MANCALOG
for i in {1..10000}
do
    bash ./run_on_agave.sh $i
done