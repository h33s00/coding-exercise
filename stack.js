class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}
class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  push(val) {
    let newItem = new Node(val);
    if (this.size == 0) {
      this.first = newItem;
      this.last = newItem;
    } else {
      let currFirst = this.first;
      this.first = newItem;
      this.first.next = currFirst;
    }
    return ++this.size;
  }

  pop() {
    if (this.size == 0) return null;
    let currFirst = this.first;
    if (this.size == 1) {
      this.last = null;
    }
    this.first = this.first.next;
    this.size--;
    return currFirst.val;
  }
}

stack = new Stack();
stack.push("Instagram");
stack.push("Programmers");
stack.push("Youtube");

console.log(stack, typeof stack);

console.log(stack.pop());

console.log(stack);
