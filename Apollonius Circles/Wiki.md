# Introduction
Apollonius' problem is to construct circles that are tangent to three given circles in a plane.

# Derivation
```math
\begin{flalign*}
&\text{Consider three circles with centers and radii -}&\\
&\hspace{1cm}\textbf{C} = \{((x_1, y_1),r_1),((x_2,y_2),r_2),((x_3,y_3),r_3)\}\\\\
&\text{Define the variables -}\\
&\hspace{1cm} i, j, k \in \{1, -1\}\\\\
&\hspace{1cm} a_1 = 2(x_1 - x_2)\\
&\hspace{1cm} b_1 = 2(y_1 - y_2)\\
&\hspace{1cm} c_1 = 2(\textbf{i} \cdot r_1 - \textbf{j} \cdot r_2)\\
&\hspace{1cm} d_1 = (x_1^2 + y_1^2 - r_1^2) - (x_2^2 + y_2^2 - r_2^2)\\\\
&\hspace{1cm} a_2 = 2(x_1 - x_3)\\
&\hspace{1cm} b_2 = 2(y_1 - y_3)\\
&\hspace{1cm} c_2 = 2(\textbf{i} \cdot r_1 - \textbf{k} \cdot r_3)\\
&\hspace{1cm} d_2 = (x_1^2 + y_1^2 - r_1^2) - (x_3^2 + y_3^2 - r_3^2)\\\\
&\hspace{1cm} e_1 = \frac{d_1 b_2 - d_2 b_1}{a_1 b_2 - a_2 b_1}\\
&\hspace{1cm} f_1 = \frac{c_1 b_2 - c_2 b_1}{a_1 b_2 - a_2 b_1}\\
&\hspace{1cm} e_2 = \frac{a_1 d_2 - a_2 d_1}{a_1 b_2 - a_2 b_1}\\
&\hspace{1cm} f_2 = \frac{a_1 c_2 - a_2 c_1}{a_1 b_2 - a_2 b_1}\\\\
&\text{Construct the quadratic -}\\
&\hspace{1cm} Ar^2 + Br + C = 0\\
&\text{where - }\\
&\hspace{1cm} A = f_1^2+f_2^2-1\\
&\hspace{1cm} B = -2(f_1(e_1 - x_1) + f_2(e_2-y_1) + \textbf{i} \cdot r_1)\\
&\hspace{1cm} C = (e_1 - x_1)^2 + (e_2 - y_1)^2 - r_1^2\\\\
&\text{Solve the quadratic for - }\\
&\hspace{1cm} r \in \mathbb{R}^+\\\\
&\text{Substitute for \textit{r} to obtain (\textit{x, y})}\\
&\hspace{1cm} x = e_1 - rf_1\\
&\hspace{1cm} y = e_2 - rf_2\\
&\hspace{1cm} ((x, y),r) \not\in \textbf{C}\\
\end{flalign*}
```

# Usage
Pre-requisite - matplotlib
```console
python "Apollonius Circles.py"
```
Refer to files named 0 to 8 for examples of input data.

# Output
```console
  Center x-coordinate    Center y-coordinate    Radius    i    j    k
---------------------  ---------------------  --------  ---  ---  ---
                0                     0.5         1.5     1    1    1
                0                    -0.665       2.33    1    1   -1
               -1.135                 1.0675      2.27    1   -1    1
               -1.68                 -0.34        3.36    1   -1   -1
                1.135                 1.0675      2.27   -1    1    1
                1.68                 -0.34        3.36   -1    1   -1
                0                     2           3      -1   -1    1
                0                     0.5         3.5    -1   -1   -1
```
<img src="https://github.com/sriya-ps/Math/blob/main/Apollonius%20Circles/Output.jpg" width=400>

# Reference
[Wikipedia](https://en.wikipedia.org/wiki/Problem_of_Apollonius)\
[Wolfram MathWorld](https://mathworld.wolfram.com/ApolloniusProblem.html)