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

let bst = new BinarySearchTree();
bst.insert(10);
bst.insert(5);
bst.insert(13);
bst.insert(10);
console.log(bst.find(10), bst.find(2));
