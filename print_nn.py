import numpy as np
import matplotlib.pyplot as plt

def plot_neural_network(nn):
    fig, ax = plt.subplots(figsize=(12, 8))
    layer_sizes = [len(layer) for layer in nn.layers]

    # Input layer position
    input_dim = len(nn.layers[0][0].weights)  # Get the number of inputs
    input_y_positions = np.linspace(-0.5, 0.5, input_dim)

    # Plot input neurons
    for i in range(input_dim):
        ax.plot(0, input_y_positions[i], 'o', markersize=12, color='orange', fillstyle='none', 
                markeredgecolor='black')  # Input neurons styled as empty circles
        ax.text(-0.2, input_y_positions[i], f"X{i + 1}", fontsize=10, ha='right')  # Label inputs

    # Plot hidden and output neurons
    for layer_idx, layer in enumerate(nn.layers):
        x_pos = layer_idx + 1  # Shift x position for hidden/output layers
        y_positions = np.linspace(-0.5, 0.5, layer_sizes[layer_idx])  # Center neurons around the X-axis

        for neuron_idx, neuron in enumerate(layer):
            y_pos = y_positions[neuron_idx]
            ax.plot(x_pos, y_pos, 'o', markersize=12, color='white', fillstyle='none', 
                    markeredgecolor='black')  # Neurons styled as empty circles

            # Display bias as a gray label near each neuron
            ax.text(x_pos + 0.1, y_pos, f"b={neuron.b:.2f}", color="gray", fontsize=8, ha='left')

            # Draw edges (weights) from the previous layer to this neuron
            if layer_idx == 0:  # First hidden layer from input layer
                for input_idx in range(input_dim):
                    input_y_pos = input_y_positions[input_idx]
                    weight = neuron.weights[input_idx]

                    # Plot line representing weight
                    ax.plot([0, x_pos], [input_y_pos, y_pos], 'k-', lw=1)

                    # Show weight values closer to the receiving neuron
                    weight_label_x = x_pos - 0.1  # Move weight label slightly left
                    weight_label_y = y_pos * 0.8 + input_y_pos * 0.2  # Average between input and neuron
                    ax.text(weight_label_x, weight_label_y, f"{weight:.2f}", color="red", fontsize=8, ha='center')
            else:  # For hidden layers to next layer
                prev_layer = nn.layers[layer_idx - 1]
                for prev_neuron_idx, prev_neuron in enumerate(prev_layer):
                    prev_y_pos = np.linspace(-0.5, 0.5, len(prev_layer))[prev_neuron_idx]
                    weight = neuron.weights[prev_neuron_idx]

                    # Plot line representing weight
                    ax.plot([x_pos - 1, x_pos], [prev_y_pos, y_pos], 'k-', lw=1)

                    # Show weight values closer to the receiving neuron
                    weight_label_x = x_pos - 0.1  # Move weight label slightly left
                    weight_label_y = y_pos * 0.8 + prev_y_pos * 0.2  # Average between prev neuron and current neuron
                    ax.text(weight_label_x, weight_label_y, f"{weight:.2f}", color="red", fontsize=8, ha='center')

    # Output neuron label
    if len(nn.layers) > 1 and layer_sizes[-1] == 1:
        output_y_pos = np.linspace(-0.5, 0.5, len(nn.layers[-1]))[0]
        ax.text(x_pos, output_y_pos + 0.15, "OUT", color="black", fontsize=10, ha="center")

    # Set plot limits and hide axes
    ax.set_xlim(-0.5, len(nn.layers))
    ax.set_ylim(-1, 1)
    ax.axis('off')
    plt.title("Neural Network Structure with Weights and Biases")
    plt.show()

def print_neural_network_parameters(nn):
    for layer_idx, layer in enumerate(nn.layers):
        print(f"Layer {layer_idx + 1}:")
        for neuron_idx, neuron in enumerate(layer):
            print(f"  Neuron {neuron_idx + 1}:")
            print(f"    Bias (b): {neuron.b:.4f}")
            print(f"    Weights (w): {', '.join(f'{w:.4f}' for w in neuron.weights)}")
        print("")