# Small glossary for the labs

[Student home](../README.md) · [Reading guide](READING_GUIDE.md)

| Term | Meaning in these labs |
|---|---|
| Sample | One image or sequence and its target |
| Feature | A measured or learned quantity used to represent a sample |
| Target / label | The value the task asks the model to predict |
| Class ID | An integer naming a category; its numeric order does not imply distance between categories |
| Tensor | A multidimensional array; shape, dtype and device all matter |
| Shape | The size of each tensor axis, such as `(batch, channels, height, width)` |
| Dtype | The kind of stored values, such as floating-point inputs or integer class IDs |
| Batch | A group of samples processed together |
| Epoch | One pass through the training samples used by the experiment |
| Parameter / weight | A model value adjusted during training |
| Hyperparameter | An experiment choice, such as learning rate or hidden width |
| Logit | An unnormalised class score; not itself a probability |
| Loss | The differentiable objective used to train the model |
| Metric | A quantity used to assess behaviour, such as accuracy; it need not be the training objective |
| Gradient | A derivative describing how a small parameter change affects the loss locally |
| Backpropagation | Applying the chain rule through the computation to obtain gradients |
| Optimiser | The rule that uses gradients to update parameters |
| Training split | Data used to fit model parameters |
| Validation split | Data used for model or hyperparameter selection |
| Test split | Held-out data used after development choices are fixed |
| Leakage | Information that improperly crosses the intended training/evaluation boundary |
| Seed | A starting value for a random-number generator; it does not guarantee identical results on every platform |
| Overfitting | Learning patterns that fit training data but do not generalise adequately |
| Baseline | A simple reference against which a proposed change is compared |
| Checkpoint | Saved model state; exact training resumption may require more than weights |
| Convolution | Applying shared local filters across an input; library image layers usually implement cross-correlation |
| Pooling | Combining values over positions, for example using a maximum or mean |
| Residual connection | Adding a branch's output to a compatible shortcut representation |
| Hidden state | A recurrent model's evolving representation of a sequence |
| Gate | A learned control of information flow in a recurrent unit such as an LSTM |
| Token | A unit processed by attention; in the image lab, an embedded image patch |
| Attention | A weighted combination of values determined by query–key compatibility |
| Kernel / runtime | The running Python process that executes notebook cells |

These are concise teaching explanations. For formal definitions and framework
behaviour, follow the [suggested readings](READING_GUIDE.md) and official API docs.
