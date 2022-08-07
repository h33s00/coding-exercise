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
  insert(val) {
    let newNode = new Node(val);
    if (this.root == null) {
      this.root = newNode;
      return this;
    } else {
      let currNode = this.root;
      while (true) {
        if (val == currNode.value) return undefined;
        else if (val > currNode.value) {
          if (currNode.right == null) {
            currNode.right = newNode;
            return this;
          }
          currNode = currNode.right;
        } else if (val < currNode.value) {
          if (currNode.left == null) {
            currNode.left = newNode;
            return this;
          }
          currNode = currNode.left;
        }
      }
    }
  }
  find(val) {
    if (this.root == null) return false;
    let currNode = this.root;
    while (true) {
      if (val == currNode.value) return true;
      if (val < currNode.value) {
        if (currNode.left == null) return false;
        currNode = currNode.left;
      }
      if (val > currNode.value) {
        if (currNode.right == null) return false;
        currNode = currNode.right;
      }
    }
  }
}

function bfs(bst) {
  let queue = [];
  let visited = [];
  queue.push(bst.root);
  while (queue.length > 0) {
    console.log(queue);
    console.log(visited);
    let curr = queue.pop(0);
    if (curr.left != null) {
      queue.push(curr.left);
    }
    if (curr.right != null) {
      queue.push(curr.right);
    }
    visited.push(curr.value);
  }
  return visited;
}
let bst = new BinarySearchTree();
bst.insert(5);
bst.insert(2);
bst.insert(3);
bst.insert(4);
bst.insert(10);
bst.insert(6);
bst.insert(7);
bst.insert(8);

console.log(bfs(bst));
