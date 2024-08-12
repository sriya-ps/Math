# Introduction
Secret sharing refers to a cryptographic method in which a secret is split between a group of people and the secret can be reconstructed only when
these people bring together their respective shares (tokens) of the secret. The individual shares (token) are of no use on their own. The secret is opened only when specific conditions are fulfilled.

# Example
## Token Generator
```math
\begin{flalign*}
&\text{Let the secret code that needs to be shared be 57.}&\\
&\text{This secret can be shared with 8 people (total tokens) and any 4 people (quorum) can retrieve the secret.}\\
&\text{However, atleast 4 people will have to work together.}\\
&\hspace{1cm} S = 57, n = 8, q = 4\\\\
&\text{We take 4 - 1 = 3 random numbers (2, 3, 1)}\\\\
&\text{Construct the expression -}\\
&\hspace{1cm} f(x) = 57 + 2x + 3x^2 + x^3\\\\
&\text{Generate tokens (shares) for the 8 people (1 - 8) -}\\
&\hspace{1cm} f(1) = 57 + 2(1) + 3(1)^2 + (1)^3 = 63\\
&\hspace{1cm} f(2) = 57 + 2(2) + 3(2)^2 + (2)^3 = 81\\
&\hspace{1cm} f(3) = 117\\
&\hspace{1cm} f(4) = 177\\
&\hspace{1cm} f(5) = 267\\
&\hspace{1cm} f(6) = 393\\
&\hspace{1cm} f(7) = 561\\
&\hspace{1cm} f(8) = 777\\\\
&\text{Share the above tokens with the respective people (1 - 8).}\\
\end{flalign*}
```

## Secret Finder
```math
\begin{flalign*}
&\text{Let persons 2, 3, 6, 5 share the tokens -}&\\
&\hspace{1cm} (2, 81) ; (3, 117) ; (6, 393) ; (5, 267) ... (x_i, y_i)\\
&\text{where } x_i \text{ refers to the person and } y_i \text{ refers to the person's token.}\\\\
&\text{In order to reconstruct the original polynomial, the Lagrange basis polynomials are used.}\\
&\hspace{1cm} l_i = \frac{x - x_0}{x_i - x_0}\times ... \times\frac{x - x_{i-1}}{x_i - x_{i-1}}\times \frac{x - x_{i+1}}{x_i - x_{i+1}}\times ... \times\frac{x - x_{q-1}}{x_i - x_{q-1}}\\
&l_0 \text{ will be for person 2.}\\
&\hspace{1cm} l_0(x) = \frac{(x-3)(x-6)(x-5)}{(2-3)(2-6)(2-5)} = \frac{(x-3)(x-6)(x-5)}{-12}\\
&l_1 \text{ will be for person 3.}\\
&\hspace{1cm} l_1(x) = \frac{(x-2)(x-6)(x-5)}{(3-2)(3-6)(3-5)} = \frac{(x-2)(x-6)(x-5)}{6}\\
&l_2 \text{ will be for person 6.}\\
&\hspace{1cm} l_2(x) = \frac{(x-2)(x-3)(x-5)}{(6-2)(6-3)(6-5)} = \frac{(x-2)(x-3)(x-5)}{12}\\
&l_3 \text{ will be for person 5.}\\
&\hspace{1cm} l_3(x) = \frac{(x-2)(x-3)(x-6)}{(5-2)(5-3)(5-6)} = \frac{(x-2)(x-3)(x-6)}{-6}\\\\
&\text{Reconstruct the generating polynomial -}\\
&\hspace{1cm} g(x) = \sum^{q-1}_{i=0} l_i(x) \cdot y_i\\
&\hspace{1cm} g(x) = \frac{(x-3)(x-6)(x-5)}{-12}\times 81 + \frac{(x-2)(x-6)(x-5)}{6}\times 117 + \frac{(x-2)(x-3)(x-5)}{12}\times 393 + \frac{(x-2)(x-3)(x-6)}{-6}\times 267\\\\
&\text{Retrieve the secret by substituting x = 0 in g(x).}\\
&\text{By computation, g(0) = 57.}\\
&\text{Hence, we find our secret 57 through this algorithm.}\\
\end{flalign*}
```

# Usage
Pre-requisite - PyQt6
```console
python "GUI.py"
```
Note - 
* "Secret Finder - GUI.py" and "Token Generator - GUI.py" are split GUI-based implementations. 
* "Secret Finder.py" and "Token Generator.py" are CUI-based implementations.

# Output
<img src="https://github.com/sriya-ps/Math/blob/main/Secret%20Sharing/Output%20-%201.jpg" width = 300>\
<img src="https://github.com/sriya-ps/Math/blob/main/Secret%20Sharing/Output%20-%202.jpg" width = 600>\
<img src="https://github.com/sriya-ps/Math/blob/main/Secret%20Sharing/Output%20-%203.jpg" width = 600>

# Reference
[Wikipedia - Secret Sharing](https://en.wikipedia.org/wiki/Secret_sharing)\
[Wikipedia - Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing)