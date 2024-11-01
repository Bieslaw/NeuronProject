import numpy as np
from functools import reduce
from operator import mul
from matplotlib.pyplot import subplots


def read_int_data(path) -> np.ndarray:
    with open(path, "rb") as f:
        # 4 bytes of magic number
        magic_number = f.read(4)
        dimensions = magic_number[3]
        print(f"Dimensionality {dimensions}")
        dimenstion_sizes = [
            int.from_bytes(f.read(4), byteorder="big") for _ in range(dimensions)
        ]
        for i, dim in enumerate(dimenstion_sizes):
            print(f"Dimension {i} size {dim}")
        data_size = reduce(mul, dimenstion_sizes)
        data = f.read(data_size)
        array = np.frombuffer(data, dtype=np.uint8)
        return np.reshape(array, tuple(dimenstion_sizes))


def read_mnist_data(img_path, labels_path) -> tuple[np.ndarray, np.ndarray]:
    labels = read_int_data(labels_path)
    images = read_int_data(img_path)
    return images, labels

def plot_img(img):
    fig, ax = subplots()
    ax.imshow(img)
    fig.show()
