class Node {
  constructor(val) {
    this.value = val;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(value) {
    var newNode = new Node(value);
    if (this.root === null) {
      this.root = newNode;
      return this;
    }
    var current = this.root;
    while (true) {
      if (value === current.value) return undefined;
      if (value < current.value) {
        if (current.left === null) {
          current.left = newNode;
          return this;
        }
        current = current.left;
      } else {
        if (current.right === null) {
          current.right = newNode;
          return this;
        }
        current = current.right;
      }
    }
  }
  find(value) {
    if (this.root === null) return false;
    var current = this.root,
      found = false;
    while (current && !found) {
      if (value < current.value) {
        current = current.left;
      } else if (value > current.value) {
        current = current.right;
      } else {
        found = true;
      }
    }
    if (!found) return undefined;
    return current;
  }
}

function dfsPreOrder(bst) {
  let visited = [];
  let current = bst.root;
  function traverse(node) {
    visited.push(node.value);
    if (node.left != null) traverse(node.left);
    if (node.right != null) traverse(node.right);
  }
  traverse(current);
  return visited;
}

function dfsPostOrder(bst) {
  let visited = [];
  let current = bst.root;
  function traverse(node) {
    if (node.left != null) traverse(node.left);
    if (node.right != null) traverse(node.right);
    visited.push(node.value);
  }
  traverse(current);
  return visited;
}

function dfsInOrder(bst) {
  let visited = [];
  let current = bst.root;
  function traverse(node) {
    if (node.left != null) traverse(node.left);
    visited.push(node.value);
    if (node.right != null) traverse(node.right);
  }
  traverse(current);
  return visited;
}

// bst = new BinarySearchTree();
// numbers = [1, 1, 1, 1, 1];
// bst.insert(numbers[0]);
// for (i = 1; i < numbers.length; i++) {
//   bst.insert(numbers[i]);
//   bst.insert(numbers[i] * -1);
// }

// console.log(bst);
