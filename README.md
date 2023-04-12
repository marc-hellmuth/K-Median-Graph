# K-Median-Graph

[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Python program to test whether a given graph is a $k$-median graph.

## Installation

The program requires Python 3.7 or higher.

#### Dependencies

* [NetworkX](https://networkx.github.io/)
* [NumPy](https://numpy.org/)



## Usage and description

For a graph $G$ and vertices $x$ and $y$, denote with $I(x,y)$ the set of all vertices that lie on shortest paths connecting $x$ and $y$.
A graph $G$ is a <em>k-median graph</em> if there are $k$ vertices $\mu_1,\dots,\mu_k\in V(G)$
such that, for all
          $u,v\in V(G)$, it holds that $|I(\mu_i,u)\cap I(\mu_i,v)\cap I(u,v)|=1$. Every median graph on $n$ vertices is, thus, an $n$-median graph.
This programs allows to quickly test if a given graph is a $k$-median graph and to determine the integer $k$.

## Citation and references

If you use this program in your project or code from it, please consider citing:

*[1]  TBA.

Please report any bugs and questions in the [Issues](https://github.com/marc-hellmuth/K-Median-Graph/issues) section.


		

