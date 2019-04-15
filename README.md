# gradient-decent
A (simple) python implementation of gradient descent I made to help me understand gradient descent. 
main.py will (by deauault) find the minimum of the function x^2+3x (x squared + 3x) but it is trivial to make it descend any function that you know the derivative and formula of and I have added a few examples of different functions to this repo

## Copyright
Copyright © 2019  Rory Sharp All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with this program.  If you have not received this, see <http://www.gnu.org/licenses/gpl-3.0.html>.

For a summary of the licence go to https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)

## Usage
1\. Modify [function()](https://github.com/qwertpi/gradient-decent/blob/b5cae38163f2476ce5515fbebab849bded75d3a3/main.py#L11) to caluclate the function you are decending
2\. Modify [derivative()](https://github.com/qwertpi/gradient-decent/blob/b5cae38163f2476ce5515fbebab849bded75d3a3/main.py#L11) to caluculate the derivative of the function you are decending
3\. Run the code and reduce the learning rate if it divergies off to infinity instead of converging on the minimum point
