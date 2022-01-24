
##### notes  
* Car detection using a pre-trained model  
    - [car](/vehicle/output/predictions.jpg) 

* Vehicles detection 
    - [traffic-1](/vehicle/output/traffic-1.jpg)


* demo on vehicle videos  
    - > ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../vehicle/videos/traffic-1.webm 
   

* INFO
    - > ssh wlzhao@seis15.se.cuhk.edu.hk  
        + wlzhao/Aiding2022  
        + /misc/gds/wlzhao/workspace  

    - gpu commands  
      > sbatch ./run.sh 
      > cat slurm-1115.out 

      > squeue <- check server status 

      > nvidia-smi  <- check gpu status  
      > scancel <id> <- cancel job id 


##### reference  
* [darknet](https://pjreddie.com/darknet/yolo/)
* [Install Darknet with Cuda and Opencv for realtime object detection](https://efcomputer.net.au/blog/4-steps-to-install-darknet-with-cuda-and-opencv-for-realtime-object-detection/)
* [YOLOv2](https://cloudxlab.com/blog/object-detection-yolo-and-python-pydarknet/) 