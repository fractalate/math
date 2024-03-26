# Polynomial Roots Iteration

What happens when you use the roots of a polynomial for the coefficients of a new polynomial? What happens when you keep doing that?

In this research, we'll be working with quadratic polynomials with leading coefficient 1, that is

$$
x^2 + bx + c
$$

where $b, c \in \mathbb{C}$ and $x$ is a complex variable. An equation of the form $x^2 + bx + c = 0$ has solutions $x = r_1$ and $x = r_2$ found with the familiar quadratic formulas

$$
r_1 = \frac{-b + \sqrt{b^2 - 4c}}{2}
$$

$$
r_2 = \frac{-b - \sqrt{b^2 - 4c}}{2}
$$

Define a function $F:\mathbb{C}\times\mathbb{C} \rightarrow X$ where $X \subset \mathcal{P}(\mathbb{C})$ and each element of $X$ has size 1 or 2 as

$$
F(b, c) = \\{ r_1, r_2 \\}
$$

The set $r = F(b, c)$ has size 1 when $r_1 = r_2$ and size 2 when $r_1 \ne r_2$. Define a function $G:X \rightarrow Y$ where $Y \subset \mathcal{P}(X)$ and each element of $Y$ has size 1 or 2 as

$$
G(r) = \\{ F(r_1, r_2), F(r_2, r_1) \\}
$$

The set $\rho = G(r)$ has size 1 when $F(r_1, r_2) = F(r_2, r_1)$ and size 2 otherwise. Define a function $H: \mathcal{P}(X) \rightarrow \mathcal{P}(X)$ as

$$
H(P) = \bigcup_{r \in P} G(r)
$$

or in less rigorous words, $H$ maps a set root pairs (or set of coefficient pairs) to a new set of root pairs; each resulting root pair being the set of roots of polynomials made from the input root pairs. For example $H(\\{ \\{r_1, r_2\\}, \\{r_3, r_4\\} \\}) = \\{F(r_1, r_2), F(r_2, r_1), F(r_3, r_4), F(r_4, r_3)\\}$

Define $H_1 = \\{ F(b, c) \\}$ and $H_n = H_{n-1} \cup H(H_{n-1})$, the set of all root pairs of all polynomials found after $n$ steps.

<!-- S mnemonic is "swarm". "C" for point "cloud" could be confused with \mathbb{C} -->
Define a function $S: \mathcal{P}(X) \rightarrow \mathcal{P}(\mathbb{C})$ as

$$
S(P) = \bigcup_{\rho \in P} \rho
$$

which is the set of roots from all the root pairs in $P$. We are concerned with the behavior of $S(H_n)$ for particular values of $b$ and $c$ as $n$ tends toward $\infty$.

<!-- TODO: Generate a GIF of several steps of iteration from x^2 + x + 1 -->

## Open Questions

* Is the point cloud generated via this process bounded?
* What is the cause of the 12-cycle in some paths in the iteration?
