# Introduction
This is an attempt to visualize the parabolic surface of a liquid in a cylindrical container at a uniform angular speed.

# Derivation
```math
\begin{flalign*}
&\text{Let the radius of the cylindrical container be } r_0 \text{, the height of the liquid initially be } h_0  \text { and the gravitational field be } -g\hat{z}. &\\
&\text{Further, let the cylinder be rotated at a uniform angular velocity } \omega\hat{z}, \text{ about an axis passing through the centre of the cylinder.}\\
&\text{At an infinitesimal volume on the surface of the rotating liquid - }\\
&\hspace{1cm}\Delta\vec{F}=\Delta F_r \cdot \hat{r} + \Delta F_z \cdot \hat{z}\\
&\hspace{1cm}\Delta F_r=\Delta mr\omega ^2, \Delta F_z=-\Delta mg\\
&\text{The resultant force should be normal to the curve of the surface - }&\\
&\hspace{1cm}\frac{\Delta z}{\Delta r}=-\frac{\Delta F_r}{\Delta F_z}=\frac{r\omega ^2}{g}\\
&\text{In the limiting case - }&\\
&\hspace{1cm}\frac{dz}{dr} = \frac{r\omega ^2}{g}\\
&\hspace{1cm}z = z_0+\frac{r^2\omega ^2}{2g}\\
&\text{The height of the liquid at the axis is computed by equating the volumes -}&\\
&\hspace{1cm}\pi r_0^2 h_0 = \int_{0}^{2 \pi} \int_{0}^{r_0} \int_{0}^{z_0+\frac{r^2\omega ^2}{2g}}r dz dr d\theta = \pi r_o^2 \bigg(z_0+\frac{r_o^2 \omega^2}{4g}\bigg)\\
&\hspace{1cm}z_0 = h_0 - \frac{r_o^2 \omega^2}{4g}\\
&\text{Equation of surface -}\\
&\hspace{1cm}z = h_0+\frac{\omega ^2}{2g} \bigg(r^2 - \frac{r_0^2}{2}\bigg)\\
&\text{Points to ponder -}\\
&\hspace{1cm}r = \frac{r_0}{\sqrt 2} \implies z=h_0\\
&\hspace{1cm}\omega > \frac{2 \sqrt{gh_0}}{r_0} \implies z_0 < 0\\

\end{flalign*}
```

# Usage
Pre-requisite - matplotlib, numpy
```console
python "Liquid Surface.py"
python "Liquid Rotation.py"
```

# Output

<img src="https://github.com/sriya-ps/Math/blob/main/Rotating%20Liquid/Output.jpg" width=400>
<img src="https://github.com/sriya-ps/Math/blob/main/Rotating%20Liquid/Output.gif" width=250>

# Reference
[MathBox](https://christopherchudzicki.github.io/MathBox-Demos/parametric_surfaces_3D.html?settings=eyJmdW5jdGlvbnMiOnsiYSI6eyJ4IjoiNCpjb3ModSkiLCJ5IjoiNCpzaW4odSkiLCJ6IjoidiIsInNhbXBsZXMiOjY0LCJvcGFjaXR5IjowLjIsImRpc3BsYXlFcXVhdGlvbiI6dHJ1ZSwidU1pbiI6MCwidU1heCI6Ni4zLCJ2TWluIjowLCJ2TWF4Ijo1LCJpZCI6ImEiLCJjb2xvciI6IiMzMDkwRkYiLCJhbmltYXRlIjp0cnVlfSwiYiI6eyJ4IjoiMip2KmNvcyh1KSIsInkiOiIyKnYqc2luKHUpIiwieiI6IjErdl4yIiwic2FtcGxlcyI6NjQsIm9wYWNpdHkiOjAuNCwiZGlzcGxheUVxdWF0aW9uIjp0cnVlLCJ1TWluIjotMiwidU1heCI6Miwidk1pbiI6LTIsInZNYXgiOjIsImlkIjoiYiIsImNvbG9yIjoib3JhbmdlIn0sImMiOnsieCI6IjIqdipjb3ModSkiLCJ5IjoiMip2KnNpbih1KSIsInoiOiIwIiwic2FtcGxlcyI6NjQsIm9wYWNpdHkiOjAuMiwiZGlzcGxheUVxdWF0aW9uIjp0cnVlLCJ1TWluIjotMiwidU1heCI6Miwidk1pbiI6LTIsInZNYXgiOjIsImlkIjoiYyIsImNvbG9yIjoiIzJkYjkyZCJ9fSwiY29udGFpbmVySWQiOiJteS1tYXRoLWJveCIsInJhbmdlIjp7InhNaW4iOi02LCJ4TWF4Ijo2LCJ5TWluIjotNiwieU1heCI6Niwiek1pbiI6LTYsInpNYXgiOjZ9LCJzY2FsZSI6WzEsMSwxXSwiY2FtZXJhIjp7InBvc2l0aW9uIjpbLTAuNTEsMS41MywtMS41OV19LCJheGVzIjp7IngiOnsidGlja3NMYWJlbCI6eyJ2aXNpYmxlIjpmYWxzZX19LCJ5Ijp7InRpY2tzTGFiZWwiOnsidmlzaWJsZSI6ZmFsc2V9fSwieiI6eyJ0aWNrc0xhYmVsIjp7InZpc2libGUiOmZhbHNlfX19LCJub1pvb20iOnRydWUsImZvY3VzIjoxLjY5NTU4MjQ5NTc4MTMxNywiZnJvbVVSTCI6dHJ1ZX0=)