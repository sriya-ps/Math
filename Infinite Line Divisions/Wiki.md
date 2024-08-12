# Introduction
To find the converging point of division between two points on the real line, that are successively divided ad infinitum in the same ratio.

# Derivation
```math
\begin{flalign*}
&\text{Consider the two points on the real line } x_0=(a) \ and \ x_1=(b),\ a < b.&\\
&\text{We successively divide the line joining the two points in the ratio } m:n \ (m,n > 0) \text{ ad infinitum.}\\
&\hspace{1cm}x_{k+2}=\frac{mx_{k+1}+nx_{k}}{m+n}, x_0=a, x_1=b, k \in \mathbb{W}\\
&\text{We need to find } \lim_{k \to \infty} x_k\\
&\text{We use Binet Forms to obtain } x_{k} \ \text{by constructing the function -}\\
&\hspace{1cm}y^2-\frac{m}{m+n}y-\frac{n}{n+m}\\
&\text{The roots of the function are -}\\
&\hspace{1cm}\alpha=1, \beta=\frac{-n}{m+n}\\
&\text{The sequence of division points can be written as -}\\
&\hspace{1cm}x_k=c\cdot\alpha^k+d\cdot\beta^k\\
&\text{Solving for c and d with initial values -}\\
&\hspace{1cm}c=\frac{(m+n)b+na}{(m+n)+n}, d=\frac{(a-b)(m+n)}{m+2n}\\
&\text{Therefore -}\\
&\hspace{1cm}\lim_{k \to \infty} x_k = \lim_{k \to \infty} c+d\cdot\beta^k = c, \ (\alpha=1, |\beta|<1)\\
&\hspace{1cm}\lim_{k \to \infty} x_k = x_{\infty} = \frac{(m+n)b+na}{(m+n)+n}\\
&\text{The final point } x_{\infty} \text{ divides } a \text{ and } b \text{ in the ratio } (m+n):n\\
\end{flalign*}
```

# Usage
Pre-requisite - matplotlib, scipy, numpy
```console
python "Divisions.py"
```

# Output
<img src="https://github.com/sriya-ps/Math/blob/main/Infinite%20Line%20Divisions/Output.jpg" width=600>

# Reference
[Wolfram MathWorld](https://mathworld.wolfram.com/BinetForms.html)
