#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=10000M
#SBATCH --partition=infofil01

#DIR=/misc/projdata11/info_fil/wlzhao/workspace
#echo -n "I'm on host: "
#hostname
CUDA_VISIBLE_DEVICES=0 
/misc/projdata11/info_fil/wlzhao/workspace/env/nllpenv/bin/python3 run_legalbert.py

for i in {06,}
do

CUDA_VISIBLE_DEVICES=0 /misc/projdata11/info_fil/wlzhao/workspace/env/nllpenv/bin/python3 \
/misc/projdata11/info_fil/wlzhao/workspace/ledgar-code/classification/legalbert_baseline.py \
--data /misc/projdata11/info_fil/wlzhao/workspace/data/LEDGAR_2016-2019_clean_freq100.jsonl --mode train


./RoBERTa_finetune/finetune.py \
  --task_name obqa --model_name roberta-large --retriever_name sentence-transformers/bert-base-nli-cls-token --post _global+pi \
  --max_len 256 --do_train --do_eval --do_test --learning_rate 9e-6 --warmup_ratio 0.$i\
  --num_train_epochs 4 --per_gpu_train_batch_size 4 --per_gpu_eval_batch_size 1  --gradient_accumulation_steps 1 \
  --kfact 10 --hop 2 --fp16

done
