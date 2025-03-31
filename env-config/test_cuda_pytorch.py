import torch

def test_cuda():
    # 检查 CUDA 是否可用
    cuda_available = torch.cuda.is_available()
    print(f"CUDA Available: {cuda_available}")

    if not cuda_available:
        print("CUDA 不可用，无法使用 GPU")
        return

    # 打印当前使用的 GPU 设备
    device = torch.device("cuda")
    print(f"Using device: {torch.cuda.get_device_name(0)}")

    # 创建两个张量，并将它们移动到 GPU
    a = torch.rand(3, 3).to(device)
    b = torch.rand(3, 3).to(device)

    print("Tensor A (on GPU):")
    print(a)
    print("Tensor B (on GPU):")
    print(b)

    # 执行矩阵加法和乘法
    c = a + b
    d = torch.mm(a, b)

    print("A + B (on GPU):")
    print(c)

    print("A * B (Matrix Multiply on GPU):")
    print(d)

if __name__ == "__main__":
    test_cuda()
