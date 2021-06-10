#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=10000M
#SBATCH --partition=infofil01

#tasks
/misc/projdata11/info_fil/wlzhao/workspace/env/nllpenv/bin/python3 run_legalbert.py