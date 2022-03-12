
##### 2022-03-09 
* vehicle analysis report  
    - vehicle-ID, vehicle-type, appear-video-coordinate, appear-time, disappear-video-coordinate, disappear-time  

* Finish the coding 

##### 2022-02-25  
* finish the deployment on server  
    - > ssh wlzhao@seis15.se.cuhk.edu.hk  - wlzhao/Aiding2022  
        + /misc/projdata11/info_fil/wlzhao/workspace/yolo3 

    - virtualenv
        + > source /misc/projdata11/info_fil/wlzhao/workspace/env/vehicleenv/bin/activate.csh

    - run 
        + > python yolo_video.py --input videos/traffic-4.webm --output output/output-traffic-4.avi --yolo yolo-coco 

* TODO  
    - finish the [YOLO object detection with OpenCV](https://pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/) 
    - the meeting  

##### 2022-02-18 
* finish yolo.py and yolo_video.py 
    - can label the video output  
    - > python yolo_video.py --input videos/traffic-1.webm --output output/labbled-traffic-1.avi --yolo yolo-coco  

##### 2022-02-15
* errors  
    - /usr/local/lib64/pkgconfig/opencv4.pc  
    - set PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib64/pkgconfig/

##### 2022-02-08  

* virtualenv
    - > source /misc/projdata11/info_fil/wlzhao/workspace/env/vehicleenv/bin/activate.csh

* worksataion @ [oracle-cloud](https://cloud.oracle.com/compute/instances?region=ap-seoul-1)
    - passphrase for ssh key: zhaowenlong
        + > ssh -i ~/.ssh/keys/id_rsa_2 ubuntu@152.70.237.255  
        + > ssh -i ~/.ssh/keys/id_rsa_1 opc@152.70.255.176
 
    - wenlzhao@gmail.com/Aiding2001@2022


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
* [YOLO object detection with OpenCV](https://pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/)
* [How to Perform Object Detection With YOLOv3 in Keras](https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/)
* [TFYOLOv3](https://github.com/YunYang1994/tensorflow-yolov3)
* [darknet](https://pjreddie.com/darknet/yolo/)
* [Install Darknet with Cuda and Opencv for realtime object detection](https://efcomputer.net.au/blog/4-steps-to-install-darknet-with-cuda-and-opencv-for-realtime-object-detection/)
* [Ubuntu18.04 + Yolov3 + OpenCV](https://codeantenna.com/a/NvKbBkdBPg)
* [Save detection to video file](https://github.com/pjreddie/darknet/issues/1235)
* [YOLOv2](https://cloudxlab.com/blog/object-detection-yolo-and-python-pydarknet/) 
