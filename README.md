# K-Median-Graph

[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Python program to test whether a given graph is a k-median graph.

## Installation

The program requires Python 3.7 or higher.

#### Dependencies

* [NetworkX](https://networkx.github.io/)
* [NumPy](https://numpy.org/)



## Usage and description

A graph G is a <em>k-median graph</em> if there are k vertices m_1,...,m_k
such that for all vertices u,v in G it holds that |I(m_i,u)\cap I(m_i,v)\cap I(u,v)|=1$,
1 ≤ i ≤ k. Every median graph on n vertices is, thus, an n-median graph.
This programs allows to quickly test if a given graph is a k-median graph and to determine the k.

## Citation and references

If you use this prgram in your project or code from it, please consider citing:

*[1]  TBA.

Please report any bugs and questions in the [Issues](https://github.com/marc-hellmuth/K-Median-Graph/issues) section.


		

