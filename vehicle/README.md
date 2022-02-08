
##### 2022-02-08  


* virtualenv
    - > source env/vehicleenv/bin/activate.csh

* worksataion @ [oracle-cloud](https://cloud.oracle.com/compute/instances?region=ap-seoul-1)
        + passphrase for ssh key: zhaowenlong
        > ssh -i ~/.ssh/keys/id_rsa_2 ubuntu@152.70.237.255
        > ssh -i ~/.ssh/keys/id_rsa_1 opc@152.70.255.176
 
        + wenlzhao@gmail.com/Aiding2001@2022


##### 2022-01-21  
* Car detection using a pre-trained model  
    - [car](/vehicle/output/predictions.jpg) 

* Vehicles detection 
    - [traffic-1](/vehicle/output/traffic-1.jpg)


* demo on vehicle videos  
    - > ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../vehicle/videos/traffic-1.webm 
   

* INFO
    - > ssh wlzhao@seis15.se.cuhk.edu.hk  - wlzhao/Aiding2022  
        + /misc/projdata11/info_fil/wlzhao/workspace

    - gpu commands  
      > sbatch ./run.sh 
      > cat slurm-1115.out 

      > squeue <- check server status 

      > nvidia-smi  <- check gpu status  
      > scancel <id> <- cancel job id 


##### reference  
* [darknet](https://pjreddie.com/darknet/yolo/)
* [Install Darknet with Cuda and Opencv for realtime object detection](https://efcomputer.net.au/blog/4-steps-to-install-darknet-with-cuda-and-opencv-for-realtime-object-detection/)
* [Save detection to video file](https://github.com/pjreddie/darknet/issues/1235)
* [YOLOv2](https://cloudxlab.com/blog/object-detection-yolo-and-python-pydarknet/) 
