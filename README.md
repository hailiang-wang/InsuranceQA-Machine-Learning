# InsuranceQA-Machine-Learning

Question and Answer Experimentals with Machine Learning Technologies for [insuranceqa-corpus-zh](https://github.com/Samurais/insuranceqa-corpus-zh).

![](https://camo.githubusercontent.com/ae91a5698ad80d3fe8e0eb5a4c6ee7170e088a7d/687474703a2f2f37786b6571692e636f6d312e7a302e676c622e636c6f7564646e2e636f6d2f61692f53637265656e25323053686f74253230323031372d30342d30342532306174253230382e32302e3437253230504d2e706e67)

# Welcome

Apply different models with [insuranceqa-corpus-zh](https://github.com/Samurais/insuranceqa-corpus-zh).


## Deps
Python3+

```
pip install -r Requirements.txt
```

## deep\_qa_1
A very simple network
```
python3 deep_qa_1/network.py
python3 visual/accuracy.py
python3 visual/loss.py
```

Baseline: hidden_layers = [100, 50], lr = 0.0001.

![](./deep_qa_1/baseline_acc.png)

![](./deep_qa_1/baseline_loss.png)

# LICENSE
[Apache2.0](./LICENSE)