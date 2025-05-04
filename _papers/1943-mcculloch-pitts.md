---
layout: paper
title: "A Logical Calculus of the Ideas Immanent in Nervous Activity"
authors: "Warren McCulloch & Walter Pitts"
year: 1943
excerpt: "Established the mathematical basis for neural networks, proposing that neurons can be modeled as logical gates and that networks of neurons can perform any computable function."
pdf_url: https://github.com/rbarbadillo/rbarbadillo.github.io/blob/master/_papers/og/1943-mcculloch-pitts.pdf
---

## Why?

McCulloch & Pitts built the first rigorous bridge between neuro-physiology and mathematical logic.

They idealised a biological neuron as a binary device that either fires (`1`) or stays silent (`0`) once every small time-step. Showing that suitably interconnected neurons can realise every formula of propositional logic—and in fact any computable function.

## What?

The paper opens with five axioms. Re-phrased with symbols I can understand better:

1. Activity for a neuron is either $1$ or $0$: $x_i(t)\in\{0,1\}$.
2. If total excitation $\geq$ fixed threshold ($\theta$) the neuron fires in the _next_ instant:  
   $x_i(t+1)=H\left(\sum_j w_{ij}\,x_j(t)-\theta_i\right)$  
   where $H$ is the [unit step function](https://en.wikipedia.org/wiki/Heaviside_step_function) (MP treat inhibition as a veto; I’m modelling that as $-\infty$ for convenience).
3. Delay is negligible and identical for every synapse.
4. Synapses are either **excitatory** (positive weight) or **inhibitory** (sufficient to block firing regardless of excitation), i.e. an inhibitory input sets the argument of $H$ to $-\infty$.
5. The network structure (weights, connections) is fixed. No learning considered; this is a logic circuit.

With this, we can easily build [logic gates](https://en.wikipedia.org/wiki/Logic_gate) with a single neuron:

| Connective | Weights $w_x,w_y$ | Threshold $θ$ | Fires when | Logic equation |
| ---------- | ----------------- | ------------- | ---------- | -------------- |
| **AND**    | 1, 1              | 2             | both 1     | $x \land y$    |
| **OR**     | 1, 1              | 1             | ≥ one 1    | $x \lor y$     |
| **NOT**    | **inhibitory** −∞ | 0             | x = 0      | $\lnot x$      |

Because **AND** and **NOT** form a [functionally complete](https://en.wikipedia.org/wiki/Functional_completeness) set, any propositional formula can be implemented by a finite network. 

They prove that every finite truth-table can be translated into a finite MP-net whose output reproduces the table row-by-row in one tick:

1. **Disjunctive normal form** – Any Boolean function $f(x_1,\dots,x_n)$ can be written
   $f=\bigvee_k (l_{k1}\land l_{k2}\land\dots)$ where each $l_{kj}$ is a literal $x_i$ or ¬$x_i$.
2. **One neuron per term** – Implement each parenthesised AND term with a neuron whose threshold equals the number of positive literals and which receives an inhibitory input for every negated literal.
3. **Final OR neuron** – Collect excitatory links from every term-neuron and set threshold = 1.

(I was _very_ confused by just reading this but the code made it a lot clearer, see below)

## Code

```python
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
```

Which gets you:

```
x y | n1 n2 | xor
-----------------
0 0 |  0  0 |  0
0 1 |  0  1 |  1
1 0 |  1  0 |  1
1 1 |  0  0 |  0
```

## Random thoughts

- I've used o3 **extensively** to actually understand what I was reading. I did expect this. It is actually delightful and way faster to learn something. I've spent Sunday morning on this, I think without AI help it would've taken me at least three times that, or I just wouldn't have done it.
- Coding has been the most fun part, also the easiest. I've tried to avoid using AI there for a change.
- Even if reading the paper and trying to understand has been painful, it's also fun in other ways. I do wish sometimes I had stayed in Uni and done a PhD.
- Biology concepts are _very_ far back on my brain.
- I did not expect math notation to have changed so much since the 40s? At least the notation that I was taught in school, which admittedly was Engineering and not Mathematics. I find modern notation way easier to understand. 
- {AND, NOT} is already functionally complete—OR can be written ¬(¬x ∧ ¬y) but I still use an explicit OR neuron in examples for clarity.