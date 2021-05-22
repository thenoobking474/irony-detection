from torch.nn.utils.rnn import pack_padded_sequence

import torch.nn as nn
import torch


class RNNClassifier(nn.Module):
    def __init__(self, embedding, embed_dim=300, hidden_dim=300, num_labels=2, num_layers=2, dropout=0.2):
        super(RNNClassifier, self).__init__()
        self.embedding = embedding
        self.n_layers = num_layers
        self.hidden_dim = hidden_dim
        self.encoder = nn.LSTM(
            input_size=embed_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            bidirectional=True,
            dropout=dropout,
            batch_first=True
        )
        self.decoder = nn.Sequential(
            nn.Linear(2*hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, num_labels)
        )

    def init_hidden(self, batch_size, device):
        weight = next(self.parameters()).data
        hidden = (weight.new(self.n_layers*2, batch_size, self.hidden_dim).zero_().to(device),
                  weight.new(self.n_layers*2, batch_size, self.hidden_dim).zero_().to(device))
        return hidden

    def forward(self, x, lengths):
        e = self.embedding(x)
        packed_e = pack_padded_sequence(e, lengths, batch_first=True, enforce_sorted=False)
        outputs, (hidden, cell) = self.encoder(packed_e)
        hidden = torch.cat((hidden[-2, :, :], hidden[-1, :, :]), dim=1)
        return self.decoder(hidden)
