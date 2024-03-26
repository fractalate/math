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
F(b, c) = \left\{ r_1, r_2 \right\}
$$

The set $r = F(b, c)$ has size 1 when $r_1 = r_2$ and size 2 when $r_1 \ne r_2$. Define a function $G:X \rightarrow Y$ where $Y \subset \mathcal{P}(X)$ and each element of $Y$ has size 1 or 2 as

$$
G(r) = \left\{ F(r_1, r_2), F(r_2, r_1) \right\}
$$

The set of $\rho = G(r)$ has size 1 when $F(r_1, r_2) = F(r_2, r_1)$ and size 2 otherwise. Define a function $H: \mathcal{P}(X) \rightarrow \mathcal{P}(X)$ as

$$
H(\Rho) = \bigcup_{r \in \Rho} G(r)
$$

or in less rigorous words, $H$ maps a set root pairs (or set of coefficient pairs) to a new set of root pairs; each resulting root pair being the set of roots of polynomials made from the input root pairs. For example $H(\left\{\left\{r_1, r_2\right\}, \left\{r_3, r_4\right\} \right\}) = \left\{F(r_1, r_2), F(r_2, r_1), F(r_3, r_4), F(r_4, r_3)\right\}$

Define $H_0 = \left\{ F(b, c) \right\}$ and $H_n = H_{n-1} \cup H(H_{n-1})$.

<!-- S mnemonic is "swarm". "C" for point "cloud" could be confused with \mathbb{C} -->
Define a function $S: \mathcal{P}(\mathbb{X}) \rightarrow \mathcal{P}(\mathbb{C})$ as

$$
S(\Rho) = \bigcup_{\rho \in \Rho} \rho
$$

We are concerned with the behavior of

$$
\lim_{n \rightarrow \infty} S(H_n)
$$

the set of roots of polynomials found by iterating the root taking process.

## Open Questions

* Is the point cloud generated via this process bounded?
* What is the cause of the 12-cycle in some paths in the iteration?
