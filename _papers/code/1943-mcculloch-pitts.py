NINF = -float("inf") # veto value


class FormalNeuron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def output(self, inputs):
        total = 0
        for name, w in self.weights.items():
            v = inputs.get(name)
            if w == NINF:               # inhibitory line
                if v == 1:              # veto active → immediate silence
                    return 0
                else:                   # veto line silent → skip
                    continue
            total += w * v              # regular excitatory weight

        return 1 if total >= self.threshold else 0


# Three‑neuron XOR network
n1  = FormalNeuron({'x': 1, 'y': NINF}, threshold=1)  # x AND (NOT y)
n2  = FormalNeuron({'x': NINF, 'y': 1}, threshold=1)  # (NOT x) AND y
xor = FormalNeuron({'n1': 1, 'n2': 1}, threshold=1)   # OR of hidden nodes

# Truth‑table 
print("x y | n1 n2 | xor")
print("-" * 17)
for x in (0, 1):
    for y in (0, 1):
        inputs = {'x': x, 'y': y}
        inputs['n1'] = n1.output(inputs)
        inputs['n2'] = n2.output(inputs)
        inputs['xor'] = xor.output(inputs)
        print(f"{x} {y} |  {inputs['n1']}  {inputs['n2']} |  {inputs['xor']}")