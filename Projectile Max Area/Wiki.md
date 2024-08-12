# Introduction
To find the angle of projection for which the maximum area swept by a projectile in a uniform vertical gravitational field with respect to the horizontal is maximum.

# Derivation
```math
\begin{flalign*}
&\text{Consider the parabola - }&\\
&\hspace{1cm} x^2 = 4ay\\
&\text{The area bounded by the parabola and the line } y = y_0 \text{ is given by - }\\
&\hspace{1cm} 2\int_{0}^{y_0} |x| \, \mathop{dy} = 2x_0 y_0 - 2\int_{0}^{x_0} y \, \mathop{dx} = \frac{4}{3} x_0 y_0\\\\
&\text{Consider the projectile motion with initial velocity, u, and angle of projection, } \theta.\\
&\text{Its horizontal range is } 2x_0 = \frac{u^2sin2\theta}{g} \text{ and its maximum height is } y_0 = \frac{u^2sin^2\theta}{2g}\\
&\text{Therefore, area bounded, } A = \frac{4}{3} \times \frac{u^2sin2\theta}{2g} \times \frac{u^2sin^2\theta}{2g} = \frac{2u^4}{3g^2} \cdot sin^3\theta cos\theta\\
&\text{For area to be maximized, } sin^3\theta cos\theta \text{ needs to be maximized}\\
&\hspace{1cm} \frac{d}{d \theta} (sin^3\theta cos\theta) = 3sin^2\theta cos^2\theta - sin^4\theta = 0 \implies \theta = 60\degree \hspace{1cm}(\theta \neq 0\degree)\\\\
&\hspace{1cm} \frac{d^2}{d \theta^2} (sin^3\theta cos\theta) = 6sin\theta cos^3\theta - 10sin^3\theta cos\theta = \frac{-3\sqrt{3}}{2}< 0 \hspace{5mm} (\theta = 60\degree)\\
&\text{Therefore, } \theta = 60\degree \text{ and the maximum area is } \frac{\sqrt{3}}{8} \frac{u^4}{g^2}\\\\
&\text{Alternatively -}&\\
&\hspace{1cm} A(\theta) = \int_{0}^{\frac{u^2sin2\theta}{g}} \bigg( xtan\theta - \frac{gx^2}{2u^2}sec^2\theta \bigg) \mathop{dx} = \frac{2u^4}{3g^2} \cdot sin^3\theta cos\theta\\\\
&\text{Or, more generally -}&\\
&\hspace{1cm} A(\theta) = \int_{g(\theta)}^{h(\theta)} y(\theta, x) \mathop{dx}\\
&\hspace{1cm} \frac{d}{d \theta} A(\theta) = y(\theta, h(\theta))\frac{d}{d \theta}h(\theta) - y(\theta, g(\theta))\frac{d}{d \theta}g(\theta) + \int_{g(\theta)}^{h(\theta)}\frac{\partial}{\partial \theta}y(\theta,x) \mathop{dx}\\
&\text{We know that, in this particular case - }&\\
&\hspace{1cm} g(\theta) = 0; \, h(\theta)=\frac{u^2sin2\theta}{g}; \, y(\theta, x)=xtan\theta - \frac{gx^2}{2u^2}sec^2\theta; \, y(\theta, h(\theta)) = 0\\
&\text{So, the derivative reduces to - }&\\
&\hspace{1cm} \frac{d}{d \theta} A(\theta) = \frac{2u^4}{3g^2}(3sin^2\theta cos^2\theta - sin^4\theta)\\
\end{flalign*}
```

# Usage
Pre-requisites - matplotlib, numpy, sympy
```console
python "Projectile.py"
```

# Output
<img src = "https://github.com/sriya-ps/Math/blob/main/Projectile%20Max%20Area/Output.jpg" width=400>