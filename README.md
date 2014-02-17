Print-Function-Plots-in-Python
==============================

Prints function plots as text to console. Use it in your script to plot functions as strings. 

Example
```python
import math
from plot_fun import plot_fun
plot_fun(lambda x: math.sin(x),begin=0,end=2*math.pi,width=80,height=10)
```
outputs:
```
0;1.0                                                           6.28318530718;1.0
            -----------------                                                   
        ----                 ----                                               
     ---                         ---                                            
  ---                               ---                                         
--                                     ---                                     -
                                          ---                               --- 
                                             ---                         ---    
                                                ----                 ----       
                                                    -------- --------           
                                                            -                   
0;-1.0                                                         6.28318530718;-1.0
```