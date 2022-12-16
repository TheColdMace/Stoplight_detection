# Stoplight_detection
Machine learning final project for the Nvidia Jetson Nano machine learning course.

takes use of imagenet.py to test accuracy
example command:
  imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 
    --labels=$DATASET/labels.txt $DATASET/test/red_light/01.jpg red.jpg
