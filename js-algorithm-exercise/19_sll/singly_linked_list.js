class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  push(val) {
    let node = new Node(val);
    if (this.head == null) {
      this.head = node;
      this.tail = this.head;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.length++;
    return this;
  }

  pop() {
    if (this.length == 0) {
      return undefined;
    } else {
      let curr = this.head;
      let pre = curr;
      while (curr.next != null) {
        pre = curr;
        curr = curr.next;
      }
      //   console.log(pre, curr);
      this.tail = pre;
      this.tail.next = null;
      this.length--;
      if (this.length == 0) {
        this.head = null;
        this.tail = null;
      }
      return curr;
    }
  }

  shift() {
    if (this.length == 0) {
      return undefined;
    } else {
      let temp = this.head;
      this.head = temp.next;
      this.length--;
      if (this.length == 0) {
        this.tail = null;
      }
      return temp;
    }
  }

  unshift(val) {
    let node = new Node(val);
    if (this.head == null) {
      this.head = node;
      this.tail = node;
    } else {
      node.next = this.head;
      this.head = node;
    }
    this.length++;
    return this;
  }

  get(index) {
    if (index < 0 || index >= this.length) {
      return null;
    }
    let counter = 0;
    let curr = this.head;
    while (counter != index) {
      curr = curr.next;
      counter++;
    }
    return curr;
  }

  set(index, val) {
    let currVal = this.get(index);
    if (currVal == null) {
      return false;
    } else {
      currVal.val = val;
      return true;
    }
  }

  insert(index, val) {
    if (index < 0 || index > this.length) {
      return false;
    } else if (index == this.length) {
      return this.push(val) ? true : false;
    } else if (index == 0) {
      return this.unshift(val) ? true : false;
    } else {
      let node = new Node(val);
      let pre = this.get(index - 1);
      node.next = pre.next;
      pre.next = node;
      this.length++;
      return true;
    }
  }

  remove(index) {
    if (index < 0 || index > this.length) {
      return undefined;
    } else if (index == this.length - 1) {
      return this.pop();
    } else if (index == 0) {
      return this.shift();
    } else {
      let pre = this.get(index - 1);
      let temp = pre.next;
      pre.next = temp.next;
      this.length--;
      return temp;
    }
  }

  reverse() {
    let node = this.head;
    this.head = this.tail;
    this.tail = node;
    let prev = null;
    let aft;
    for (let i = 0; i < this.length; i++) {
      aft = node.next;
      node.next = prev;
      prev = node;
      node = aft;
    }
    return this;
  }
}

let list = new SinglyLinkedList();
console.log(list.push("HELLO!"));
console.log(list.push("GOODBYE!"));
console.log(list.push("!"));
console.log(list.insert(0, "HEHEHE!"));
console.log(list.reverse());
console.log(list.head);
// console.log(list.remove(0));

// console.log(list.pop());
// console.log(list.pop());
// console.log(list.pop());
// console.log(list.shift());
// console.log(list.shift());
// console.log(list.unshift("Huh?"));
// console.log(list);

// console.log(list.get(1));
// console.log(list.set(1, "NO!"));
// console.log(list.get(1));
