import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import torch.utils.data.dataloader

def get_default_sequential(input_size, hidden_size, output_size):
    return nn.Sequential(
                nn.Linear(input_size, hidden_size),
                nn.ReLU(),
                nn.Linear(hidden_size, output_size),
            )

class P1_Net(nn.Module):
    def __init__(self, sequential: nn.Sequential):
        super(P1_Net, self).__init__()
        self.linear_relu_stack = sequential

    def forward(self, x):
        return self.linear_relu_stack(x)

def do_train(network: P1_Net, train_loader: torch.utils.data.DataLoader, 
              optimizer: torch.optim.Optimizer, loss_criterion, epochs = 2):
    for k in range(epochs):
        running_loss = 0.0
        iterations = 0
        for i, data in enumerate(train_loader):
            iterations+=1
            inputs, labels = data
            
            optimizer.zero_grad()
            outputs = network(inputs)

            loss = loss_criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            loss = loss.item()
        print(f'[{k + 1}] loss: {running_loss / iterations:.3f}')


# df_x = np.random.uniform(0, 2 * np.pi, 1000)
# df = pd.DataFrame({'X' : df_x, 'Y': np.sin(df_x)})
# dataset = torch.utils.data.TensorDataset(
#     torch.from_numpy(df['X'].to_numpy().astype('float32')).unsqueeze(1), 
#     torch.from_numpy(df['Y'].to_numpy().astype('float32')).unsqueeze(1)
# )
# data_loader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=False)
# net = P1_Net(
#     nn.Sequential(
#         nn.Linear(1, 500),
#         nn.ReLU(),
#         nn.Linear(500,500),
#         nn.ReLU(),
#         nn.Linear(500,1)
#     )
# )
# print(net)

# optimizer = torch.optim.Adam(net.parameters())
# loss = nn.MSELoss()

# do_train(net, data_loader, optimizer, loss, 4)