import numpy as np
import matplotlib.pyplot as plt

def print_neural_network_parameters(nn):
    for layer_idx, layer in enumerate(nn.layers):
        print(f"Layer {layer_idx + 1}:")
        for neuron_idx, neuron in enumerate(layer):
            print(f"  Neuron {neuron_idx + 1}:")
            print(f"    Bias (b): {neuron.b:.4f}")
            print(f"    Weights (w): {', '.join(f'{w:.4f}' for w in neuron.weights)}")
        print("")