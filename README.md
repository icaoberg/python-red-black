# python-red-black

> [!WARNING]
> This implementation is inspired by a homework assignment from [15-213](https://www.cs.cmu.edu/~213/) at Carnegie Mellon University. It is intended for educational purposes only and is not suitable for production use.

[![CI](https://github.com/icaoberg/python-red-black/actions/workflows/ci.yml/badge.svg)](https://github.com/icaoberg/python-red-black/actions/workflows/ci.yml)
[![Release Status](https://img.shields.io/badge/release-v0.1-red.svg)](https://github.com/icaoberg/python-red-black)
[![GitHub issues](https://img.shields.io/github/issues/icaoberg/python-red-black.svg)](https://github.com/icaoberg/python-red-black/issues)
[![GitHub forks](https://img.shields.io/github/forks/icaoberg/python-red-black.svg)](https://github.com/icaoberg/python-red-black/network)
[![GitHub stars](https://img.shields.io/github/stars/icaoberg/python-red-black.svg)](https://github.com/icaoberg/python-red-black/stargazers)
[![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)

A simple naive implementation of a [red-black tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree) in Python.

The purpose of this repo is to serve as an example of how to set up a GitHub Actions workflow.

## Definition

> A binary search tree where each node is colored red or black, the root is black, both children of every red node are black, and every path from a node to a leaf contains the same number of black nodes. These constraints guarantee O(log n) height and therefore O(log n) worst-case search, insert, and delete.

— Paul E. Black, *[red-black tree](https://xlinux.nist.gov/dads/HTML/redblack.html)*, Dictionary of Algorithms and Data Structures [online], NIST.

## When to Use

A red-black tree provides the same ordered operations as a BST but with guaranteed O(log n) worst-case performance due to automatic rebalancing. Choose it over a plain BST when input order is unpredictable or when worst-case latency matters:

- **Language standard libraries** — Java's `TreeMap` and `TreeSet`, and C++ STL's `std::map` and `std::set` are backed by red-black trees to guarantee O(log n) operations.
- **Linux kernel scheduler** — the completely fair scheduler (CFS) uses a red-black tree keyed on virtual runtime to efficiently select the next process to run.
- **Database indexes** — storage engines that need predictable read/write latency on sorted keys use red-black trees rather than unbalanced BSTs.
- **Interval scheduling** — computational geometry and event-driven simulations use red-black trees to maintain sorted intervals and query overlaps in O(log n).
- **Memory allocators** — allocators like `jemalloc` use red-black trees to track free memory regions by size for fast best-fit searches.

## Requirements

- Python 3.6+

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/icaoberg/python-red-black.git
cd python-red-black
pip install -r requirements.txt
```

## Usage

```python
from RedBlackTree import RedBlackTree

tree = RedBlackTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print(tree.size())      # 5
print(tree.min())       # 1
print(tree.max())       # 7
print(tree.inorder())   # [1, 3, 4, 5, 7]
print(tree.is_empty())  # False
print(len(tree))        # 5
print(tree.search(3))   # Node(3, BLACK)
```

### Methods

| Method | Description |
|--------|-------------|
| `insert(element)` | Insert an element into the tree |
| `search(element)` | Return the node with the given value, or `None` |
| `random(n)` | Populate the tree with `n` random integers |
| `min()` | Return the minimum value |
| `max()` | Return the maximum value |
| `inorder()` | Return elements in sorted order as a list |
| `is_empty()` | Return `True` if the tree has no nodes |
| `size()` | Return the number of nodes |
| `get_root()` | Return the root node |

## Testing

```bash
pytest tests.py
```

## Support

If you found this project helpful, consider buying me a coffee!

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/icaoberg)

## Copyright

Copyright © [icaoberg](https://github.com/icaoberg) at [Carnegie Mellon University](https://www.cmu.edu). All rights reserved.
