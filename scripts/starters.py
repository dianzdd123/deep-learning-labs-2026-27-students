"""Student-facing starter cells in worksheet order. Ellipses mark student work."""

SETUP = {
    "keras": """import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

seed = 42
keras.utils.set_random_seed(seed)
print(tf.__version__, tf.config.list_physical_devices("GPU"))
# TODO: record your device and choose the validation metric.
validation_metric = ...""",
    "pytorch": """import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.utils.data import DataLoader, random_split

seed = 42
torch.manual_seed(seed)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(torch.__version__, device)
# TODO: record your device and choose the validation metric.
validation_metric = ...""",
}

ORIENTATION = [
    """import platform
from importlib.metadata import version
print(platform.python_version())
package = ...  # TODO: enter "torch" or "tensorflow" and inspect available devices.
print(version(package))""",
    """from pathlib import Path
data_dir = ...  # TODO: enter the local folder from the official data instructions.
print([p.name for p in Path(data_dir).iterdir()][:5])
# Open one sample and record its shape and label.""",
    """questions = {
    "dataset": ...,  # TODO: ask about a property of the sample you inspected.
    "evaluation": ...,  # Which split or metric needs clarification?
}
print(questions)""",
]

def image_data(framework, dataset):
    if framework == "keras":
        loader = {"cnn": "fashion_mnist", "resnet": "cifar10"}[dataset]
        return f"""(x_pool, y_pool), (x_test, y_test) = keras.datasets.{loader}.load_data()
print(x_pool.shape, y_pool.shape, x_pool.min(), x_pool.max())
order = np.random.default_rng(seed).permutation(len(x_pool))
train_ids, val_ids = ...  # TODO: partition order into two disjoint index arrays.
# Scale all images consistently and add a channel axis for grayscale images.
x_train, y_train = ...
x_val, y_val = ..."""
    loader = {"cnn": "FashionMNIST", "resnet": "CIFAR10"}[dataset]
    return f"""from torchvision import datasets, transforms
transform = transforms.ToTensor()
pool = datasets.{loader}("data", train=True, download=True, transform=transform)
test = datasets.{loader}("data", train=False, download=True, transform=transform)
print(pool[0][0].shape, pool[0][1])
split_lengths = ...  # TODO: reserve validation examples from pool.
train, val = random_split(pool, split_lengths, generator=torch.Generator().manual_seed(seed))
# Build train_loader, val_loader and test_loader. Shuffle only training examples."""

FIT = {
    "keras": """epochs = 3
model.compile(optimizer="adam", loss=..., metrics=["accuracy"])  # TODO: integer labels and logits.
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=epochs)
plt.plot(history.history["val_accuracy"])
# Add a labelled training curve and inspect the gap.""",
    "pytorch": """epochs = 3
model = model.to(device)
optimizer = torch.optim.Adam(model.parameters())
criterion = ...  # TODO: choose a loss for integer labels and raw logits.
for epoch in range(epochs):
    model.train()
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        logits = model(inputs)
        loss = ...
        # TODO: backpropagate and update parameters.
    # Evaluate val_loader with model.eval() and no_grad(); record both curves.""",
}
EVAL = {
    "keras": """# TODO: choose weights using validation results, then freeze the model.
final_model = ...
logits = final_model.predict(x_test, verbose=0)
predicted = ...  # Pick one class per example.
truth = np.asarray(y_test).reshape(-1)
print(tf.math.confusion_matrix(truth, predicted))
# Locate misclassified indices and inspect examples.""",
    "pytorch": """final_model = ...  # TODO: load the weights chosen on validation data.
final_model.eval()
predicted, truth = [], []
with torch.no_grad():
    for inputs, labels in test_loader:
        logits = final_model(inputs.to(device))
        batch_classes = ...  # Pick one class index per example.
        predicted.extend(batch_classes.cpu().tolist())
        truth.extend(labels.tolist())
# Compute accuracy, build a confusion matrix and inspect mistakes.""",
}
CNN = {
    "keras": ["""sample_shape = x_train.shape[1:]
probe = layers.Conv2D(16, 3, padding="same")
features = probe(x_train[:2])
pooled = ...  # TODO: apply 2 x 2 pooling and predict the resulting dimensions.
print(sample_shape, features.shape, pooled.shape)""",
    """model = keras.Sequential([
    keras.Input(shape=sample_shape),
    layers.Conv2D(16, 3, padding="same", activation="relu"),
    ...,  # TODO: pooling and a second convolution with activation
    layers.Flatten(),
    ...,  # ten raw class scores
])
model.summary()
assert model(x_train[:2]).shape == (2, 10)"""],
    "pytorch": ["""batch, _ = next(iter(train_loader))
features = nn.Conv2d(1, 16, 3, padding=1)(batch)
pooled = ...  # TODO: apply 2 x 2 pooling.
print(batch.shape, features.shape, pooled.shape)""",
    """model = nn.Sequential(
    nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(),
    ...,  # TODO: pooling, second convolution and nonlinearity
    nn.Flatten(),
    ...,  # map flattened features to ten logits
)
assert model(batch[:2]).shape == (2, 10)
print(sum(p.numel() for p in model.parameters()))"""],
}

RESNET = {
    "keras": ["""x = keras.Input(shape=(32, 32, 16))
branch = layers.Conv2D(16, 3, padding="same")(x)
shortcut = ...  # TODO: choose a shape-compatible identity path.
print(branch.shape, shortcut.shape)""",
    """def make_model(use_skip):
    inputs = keras.Input(shape=(32, 32, 3))
    x = layers.Conv2D(16, 3, padding="same")(inputs)
    residual = ...  # TODO: apply the same convolution branch in both models.
    merged = ...  # condition addition on use_skip
    pooled = layers.GlobalAveragePooling2D()(merged)
    return keras.Model(inputs, layers.Dense(10)(pooled))

plain, residual = make_model(False), make_model(True)
print(plain.count_params(), residual.count_params())""",
    """results = {}
for name, net in [("plain", plain), ("residual", residual)]:
    # TODO: match initial branch weights and reset batch order before each fit.
    net.compile(optimizer="adam", loss=..., metrics=["accuracy"])
    results[name] = net.fit(x_train, y_train, epochs=3, validation_data=(x_val, y_val))
# Plot both validation curves with the same axes."""],
    "pytorch": ["""x = torch.zeros(2, 16, 32, 32)
branch = nn.Conv2d(16, 16, 3, padding=1)(x)
shortcut = ...  # TODO: choose the identity tensor; predict what stride 2 changes.
assert branch.shape == shortcut.shape""",
    """class Block(nn.Module):
    def __init__(self, use_skip):
        super().__init__()
        self.use_skip = use_skip
        self.branch = ...  # TODO: shape-preserving convolution branch

    def forward(self, x):
        residual = self.branch(x)
        return ...  # condition addition on self.use_skip

def make_model(use_skip):
    return nn.Sequential(nn.Conv2d(3, 16, 3, padding=1), Block(use_skip),
                         nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(16, 10))
plain, residual = make_model(False), make_model(True)
# Compare parameter counts and run a dummy RGB batch.""",
    """results = {}
for name, net in [("plain", plain), ("residual", residual)]:
    net = net.to(device)
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
    # TODO: match initial weights and reset loader order before each run.
    results[name] = ...  # train for three epochs; store validation curves and weights
# Compare validation accuracy at matched epochs."""],
}

def lab_cells(key, framework):
    if key == "cnn":
        steps = [image_data(framework, key), *CNN[framework], FIT[framework]]
    elif key == "resnet":
        steps = [image_data(framework, key), *RESNET[framework]]
    else:
        raise ValueError(f"No student worksheet available for {key}")
    return [SETUP[framework], *steps, EVAL[framework]]
