#### note  

##### 2021-12  
* camera model 
* camera calibration  

##### 2021-09-16  

* TODO  
    - update the QA lecture notes 

##### 2021-08-24  

* TODO  
    - think about your future 
    - analyze the current working, and give the answer today  


* advantages  
    - more free time  
        + build your relationship, and learn the bible  
        + do more learning  

    - a bit guarantee and stable  
        + salary monthly  
        + show her that she can **trust you to do your part in providing for a household**  
        + go to work each day and **try hard to do your best**  
        + show her that you are dependable 
        

* disadvantages  
    - your goal is to do in the industry  
    - be confident to know your disadvantages, and know how to fix it  
        + care about your progress, and tials-error  


* SUMMRAY  
    - receive the contract 
    - **do your best**  
    - 你对工作有些三心二意  


##### 2021-07-15 

* TODO  
    - update json directly  
    - add matching rules to find more cases  

##### 2021-07-13  
* TODO  
    - finish the code on 'DEFINITIONS'  

* info
    - the new json: cuad_new_test.json, cuad_new_train.json
    - /misc/projdata11/info_fil/wlzhao/workspace/data

##### 2021-07-06 
* TODO  
    - clean, and format the CUAD data  
    - the experiment on longformer paper  
    - check more global information apart from the 'DEFINITIONS'  

* info
    - /misc/projdata11/info_fil/wwxu/WorkSpace/cuad-bak

##### 2021-07-05  
* write the code to scrape the DEFINITIONS forms  

##### 2021-07-02  
* TODO
    - think about your goal  
    - co-work with the law? 

##### 2021-06-25  
* TODO  
    - scrape the DEFINITIONS forms from [CUDA](https://zenodo.org/record/4595826#.YNU88BMzbUI)  
    - for example: 
     "CUSTOMERS" means all users who access Co-Branded Site. 
     

##### 2021-06-24  
* TODO  
    -  read the 'contract discovery' paper again  
    -  combine and formalize the ideas  ?

##### 2021-06-23  
* TODO  
    - paper reading  
    - the  CUDA paper 
        + how well NLP language models generalize to specialized domains  
            - **model design**, model size   
            - Data: **high-quality domain-specific annotated data**  than more unlabeled domain-specific data  

        + CUDA dataset  
            - large legal (specialized) **annotated** data 
        
        + method
            - models learn to highlight important clauses to that label  

    - Contract Discovery  
        + **semantic retrieval of relevant clauses or their retrieval**  from legal texts  => more annotated data


* more focus  

##### 2021-06-22  
* think about the papers  

* so tired  

##### 2021-06-21  
* think about the opinions and papers  
    - how?    

##### 2021-06-17  
* read the paper lexNLP 

*  Blackstone in Hong Kong 
    - **other legal texts** not only on commercial applications  
    - such as judgments, skeleton arguments, scholarly articles, law commission reports, pleadings etc.  

    - **understaning of the meaning of the text and how it might fit into 
a larger corpus of text**   
        + reference, quote, submission  
        + re-use of that content for other useful purposes  

    - **automatically extract information from long, unstructured legal texts** 
    - [Blackstone](https://research.iclr.co.uk/blog/blackstone-goes-live)
 

##### 2021-06-16  
* submit the running result  

* read the paper LEDGAR, and try to run it on  the server  

* some programming  


##### 2021-06-15  

* run on the server to get the optimized parameters   
    - check the result on slurm-11345.out 

* read paper "LEDGAR"

* note on text classificaton 
    - **standardized by tags from unstructured text**  
    - Tagging functions  

* TODO 
    - read some on deeplearning  
    - config vscode to ssh remote servers

##### 2021-06-11 

* run on the server with the parameters 
    - tocheck the result on  slurm-11159.out  

* gpu commands  
    > sbatch ./run.sh 
    > cat slurm-1115.out 

    > squeue <- check server status 

    > nvidia-smi  <- check gpu status  
    > scancel <id> <- cancel job id 


#### 2021-06-10  
* TODO  
    - use the server to run  
    > ssh wlzhao@sepc429.se.cuhk.edu.hk  
        + 6 24G GPU - submit tasks 
        + /misc/projdata11/info_fil/wlzhao/workspace
    > source env/nllpenv/bin/activate.csh  
        + [run_legalbert.py](https://github.com/muyun/dev.nllp/blob/master/experiment/ledgar-code/run_legalbert.py)
        + use subprocess to package the args


    - read the papers  

    - do some programming  

#### 2021-06-08  
* TODO  
    - try to use the server  
    - nllpenv env 
    > virtualenv /misc/projdata17/infofil/wlzhao/.env/nllpenv 
    > source /misc/projdata17/infofil/wlzhao/.env/nllpenv/bin/activate.csh  

* try to use another server  
    - update the cache config
    - add bash script to submit gpu task  
    >#!/bin/bash
    #SBATCH --nodes=1
    #SBATCH --gres=gpu:1
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=10000M
    #SBATCH --partition=infofil01

##### 2021-06-04  

* TODO  
    - try to use the server  

##### 2021-06-03  

* update the legalbert_baseline.py  
    - learn more about deeplearning, especially on parameters  
    - it works, and a bit excited actually, but boring  

* TODO  
    - check the server  
    - [自學粵語 (一)](https://www.ilc.cuhk.edu.hk/EN/workshops.aspx)

##### 2021-06-02  

* log:
$ python classification/legalbert_baseline.py --data ../data/LEDGAR_2016-2019_clean_freq100.jsonl --mode train
2021-06-02 17:40:48.799092: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cuda
rt64_110.dll'; dlerror: cudart64_110.dll not found
2021-06-02 17:40:48.799283: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have
a GPU set up on your machine.
Some weights of the model checkpoint at C:\Users\wlzhao\proj\goal2021\experiment\legal-bert-small were not used when initializin
g BertModel: ['cls.predictions.transform. LayerNorm.weight', 'cls.predictions.transform.dense.weight', 'cls.predictions.decoder.b
ias', 'cls.seq_relationship.weight', 'cls.predictions.transform.dense.bias', 'cls.predictions.bias', 'cls.predictions.transform.
LayerNorm.bias', 'cls.seq_relationship.bias', 'cls.predictions.decoder.weight']
* This IS expected if you are initializing BertModel from the checkpoint of a model trained on another task or with another arch
itecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
* This IS NOT expected if you are initializing BertModel from the checkpoint of a model that you expect to be exactly identical
(initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
construct training data tensor
start training
Iteration:   0%|                                                                                     | 0/56297 [00:00<?, ?it/s]
Epoch:   0%|                                                                                     | 0/1 [00:00<?, ?it/s]

##### 2021-06-01  

* TODO  
    - read the paper <legal bert>  

    - check how to use LEGAL-BERT to train  
        + adjust the code  
    

##### 2021-05-31  

* TODO  
    - read Brendan Eich part from <coders at work>  

    - some programming  
    
    - read the paper <legal bert>  

* SUMMARY  
    - feel so tired 

##### 2021-05-28  

* TODO  
    - read the paper <legal bert>  

    - read Brendan Eich part from <coders at work> 

* SUMMARY  

    - exercise more, like getting up earlier, and running in the moring  

##### 2021-05-27  

* TODO  
    - setup and run the experiment on windows  
        + DONE with INFO  

    - read the articles  
        + actually not, a bit tired  

    - some programming  
        + Actually not, a bit tired  

* INFO  
    - setup virtualenv on windows  
    > virtualenv nllpenv  
    > source ~/nllpenv/Scripts/activate  
    > deactivate  

* SELF  
    - learn and practice listening skills  
        + **use feelings**, not words to express  
        + your tone of voice    
        + notice your language in the meetup  
    

##### 2021-05-26

* TODO
    - read the paper <Ledgar>
        + CHECK the data format 
        + think about the related experiement 
        + [code](https://github.com/dtuggener/LEDGAR_provision_classification)

    - read the paper on legal-bert

    - some programming

* insight
    - clearly thinking: if you wanna think better, **giving more time to think**, and hone your understanding of the problem

* research:
    - **mindset**: **learning from failure to continue exploring the unknown*** is a brodadly useful mindset
        + science proceeds because researchers do all they can to **disprove their hypotheses** rathe than prove them right

    - look for **important problems**, meaning ones with **answers that matter to humankind**

    - **getting started**
        + it's **unnecessary** for scientists to spend an enormous amount of time learning techniques and supporting disciplines before beginning research

        + the best way to learn what we need to know is **by getting started**, then **picking up new knowledge as it proves itself necessary**.
        the great incentive to learning a new skill or supporting discipline is **needing to use it**
        when there's an urgent need, we learn faster and avoid unnecessary learning

        +  build confidence **by doing something concrete and seeing a visible manifestation of our labors**.
        the best scientists **begin with the understanding** that they can never know anything and, besides, **learning needs to be a lifelong process**        "**psychologically most important to get results**, even if they are not original"

    - effective collaboration
        + advocate for being open about ideas and doing away with secrecy
        +  **tell everyone everything you know**

    - never to fool yourself

    - the best creative environment
        + creativity rises from **tranquility**
        + creativity is upported by **a safe environement**,
        one in which you can **share and question openly**, and be heard
        with **compassion and a desire to understand**

##### 2021-05-25

* TODO
    - read the paper <Ledgar>
        + set the worksation env

    - finish the ch5
        + DONE

    - programming
        + Some python ebook from cuhk

* INFO
    - workstation @cuhk 
       > ssh wlzhao@seis01.se.cuhk.edu.hk  
           + 3 11G GPU - debug 
           + /misc/projdata17/infofil/wlzhao/data
       > ssh wlzhao@sepc429.se.cuhk.edu.hk  
           + 6 24G GPU - submit tasks 
           + /misc/projdata11/info_fil/wlzhao
       > ssh wlzhao@137.189.56.6
       > ssh wlzhao@137.189.59.36

    - worksataion @ [oracle-cloud](https://cloud.oracle.com/compute/instances?region=ap-seoul-1)
        + passphrase for ssh key: zhaowenlong
        > ssh -i ~/.ssh/keys/id_rsa_2 ubuntu@152.70.237.255
        > ssh -i ~/.ssh/keys/id_rsa_1 opc@152.70.255.176
 

        + wenlzhao@gmail.com/Aiding2001@2022

    - push into the master branch not main branch

##### 2021-05-24

* TODO
    - read the paper <Ledgar>

    - read ch5 in <coders at work>
        + interesting, let me know how the programmer does his work

    - do some programming
        + should code more, and find the funny on coding

* SELF
    - feel a bit tired

* SUMMARY
    - get up too late, around 10:30;  get up at 8:00

##### 2021-05-21

* check LEDGAR dataset, and try to use legal-bert model as a baseline

* check more dataset on 'sentence classification'

* idea
    - more features from cases + items

##### 2021-05-20

* TODO
    - update the issues on the research topics

    - Think about what you wanna in this job
        + improve my research, and writing skills ?
        + explore the research ideas

    - and how does this job help u with your purpose

* TOIMPROVE
    - more effort on the current work
    - don't do other things in your working time

##### 2021-05-17

*  Staff card
    - profile -> The CU Link Card Centre, located in Room 804, 8/F,  Wu Ho Man Yuen (WMY) Building R804

##### 2021-05-13

* TODO
    - finish the PPT  on method part

    - check more papers

    - think about your directions

##### 2021-05-12

* TODO
    - read one paper

    - write the PPT

    - don't spend on the others when you are working

* reference
    - [legartis](https://legartis.ai/)

* Summary
    - DONE

##### 2021-05-11

* TODO
    - read one paper

    - write the PPT

    - some programming

    - write on the proj "from idea to business"

* Summary
    - Don't do anything
    - didn't sleep good

##### 2021-05-10

* TODO
    - finish one paper according to the skills

    - begin to write the PPT

##### 2021-05-06

* TODO
    - read the article 'how to read papers'
        + DONE

    - read one paper

    - some programming
        + JS

##### 2021-05-05

* TODO
    - [Git knowledge](https://jwiegley.github.io/git-from-the-bottom-up/)
        + DONE

##### 2021-05-04

* NLP in legal domain
    - IP field ?

* switch my blog into heroku
    - rss papers ?

* how to read papers

##### 2021-05-03  - target

* join a group for a research paper
    - paper reading

* improve my programming
    - scheme
    - js/typescript
    - python

* improve my skills
    - writing
    - publich speaking

* try to be responsible
    - work at least 8h each day on the project
    - a bit more active

* try to improve your energy and efficiency
    - more priorities and focus

#### info

*  wlzhao/Wenlong001
