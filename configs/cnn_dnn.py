from models.cnn_dnn import CnnDnnClassifier

from datetime import datetime

# Model config
glove_dim = 300
conv1_filters = 32
conv1_kernel = 5
conv1_padding = 2
conv2_filters = 64
conv2_kernel = 3
conv2_padding = 1
dropout_rate = 0.2
fc_neurons = 128
num_labels = 2
model_constructor = lambda e, f, g: CnnDnnClassifier(e, embedding_dim=glove_dim, conv1_filters=conv1_filters,
                                               conv2_filters=conv2_filters, dropout_rate=dropout_rate,
                                               fc_neurons=fc_neurons, num_labels=num_labels, max_length=f,
                                               conv1_kernel=conv1_kernel, conv2_kernel=conv2_kernel,
                                               conv1_padding=conv1_padding, conv2_padding=conv2_padding, features_dim=g)

# Hyper-parameters
seed = 8008135
batch_size = 32
lr = 1e-4
weight_decay = 5e-4
epochs = 1000
early_stopping = True
early_stop_tolerance = 50

# Task configuration
test_task = 'A'
test_type = 'test'
test_emojis = True
test_irony_hashtags = True

remove_punctuation = False
use_features = True

# Save configuration
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
save_path = f"../saves/cnn_dnn_{dt_string}/"

# Test configuration
path_punctuation = "../saves/final_lstm_rnn/punct.pth"     # path to model with punctuation
path_no_punctuation = "../saves/final_lstm_rnn/no_punct.pth"    # path to model with no punctuation
path_punctuation_features = "../saves/final_lstm_rnn/punct_features.pth"     # path to model with punctuation and feat
#test_mode = "punctuation"  # can be punctuation or features
test_mode = "features"  # can be punctuation or features
exact = False
correction = True
