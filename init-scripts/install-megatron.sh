docker pull nvcr.io/nvidia/pytorch:22.12-py3 
docker run --gpus all -it --rm  nvcr.io/nvidia/pytorch:22.12-py3
# docker run --gpus all -it --rm -v /path/to/megatron:/workspace/megatron -v /path/to/dataset:/workspace/dataset -v /path/to/checkpoints:/workspace/checkpoints nvcr.io/nvidia/pytorch:22.12-py3
