#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gres=gpu:0
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=10000M
#SBATCH --partition=infofil01

#DIR=/misc/projdata11/info_fil/wlzhao/workspace
#echo -n "I'm on host: "
#hostname

for seq_len in 128 256 384 512
do
    for epoch in 2 3 4
    do
        for rate in 1e-4 5e-4
        do
CUDA_VISIBLE_DEVICES=0 /misc/projdata11/info_fil/wlzhao/workspace/env/nllpenv/bin/python3 \
/misc/projdata11/info_fil/wlzhao/workspace/ledgar-code/classification/legalbert_baseline.py \
--data /misc/projdata11/info_fil/wlzhao/workspace/data/LEDGAR_2016-2019_clean_freq100.jsonl \
--mode train \
--max_seq_len  $seq_len \
--epochs $epoch \
--learning_rate $rate
        done 
    done
done
