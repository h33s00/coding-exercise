class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(val) {
    let newNode = new Node(val);
    if (this.length == 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      // connection
      this.tail.next = newNode;
      newNode.prev = this.tail;
      // tail updated
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  pop() {
    if (this.length == 0) return undefined;

    let oldTail = this.tail;

    if (this.length == 1) {
      this.head = null;
      this.tail = null;
    } else {
      // tail updated
      this.tail = oldTail.prev;
      this.tail.next = null;
      oldTail.prev = null;
    }
    this.length--;

    return oldTail;
  }

  shift() {
    if (this.length == 0) return undefined;

    let oldHead = this.head;

    if (this.length == 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = oldHead.next;
      this.head.prev = null;
      oldHead.next = null;
    }
    this.length--;

    return oldHead;
  }

  unshift(val) {
    let newHead = new Node(val);
    if (this.length == 0) {
      this.head = newHead;
      this.tail = newHead;
    } else {
      this.head.prev = newHead;
      newHead.next = this.head;
      this.head = newHead;
    }
    this.length++;
    return this;
  }

  get(index) {
    // valid index?
    if (index < 0 || index >= this.length) return null;

    let foundNode;
    let counter;

    if (index <= this.length / 2) {
      foundNode = this.head;
      counter = 0;
      while (counter != index) {
        foundNode = foundNode.next;
        counter++;
      }
    } else if (index > this.length / 2) {
      foundNode = this.tail;
      counter = this.length - 1;
      while (counter != index) {
        foundNode = foundNode.prev;
        counter--;
      }
    }

    return foundNode;
  }

  set(index, val) {
    let result = this.get(index);
    if (result == null) return false;
    else {
      result.val = val;
      return true;
    }
  }

  insert(index, val) {
    if (index < 0 || index >= this.length) return false;
    if (index == 0) return !!this.unshift(val);
    if (index == this.length) return !!this.push(val);
    else {
      let newNode = new Node(val);
      let p = this.get(index - 1);
      let c = p.next;

      p.next = newNode;
      c.prev = newNode;
      newNode.next = c;
      newNode.prev = p;
      this.length++;
      return true;
    }
  }

  remove(index) {
    if (index < 0 || index >= this.length) return undefined;
    if (index == 0) return this.shift();
    if (index == this.length - 1) return this.pop();
    else {
      let item = this.get(index);
      let pre = item.prev;
      let aft = item.next;

      pre.next = aft;
      aft.prev = pre;
      item.next = null;
      item.prev = null;
      this.length--;
      return item;
    }
  }

  reverse() {
    let currNode = this.head;
    this.head = this.tail;
    this.tail = currNode;
    let ogprev;
    let ognext;

    for (let i = 0; i < this.length; i++) {
      ogprev = currNode.prev;
      ognext = currNode.next;
      currNode.next = ogprev;
      currNode.prev = ognext;
      // console.log(currNode);
      currNode = ognext;
    }
    return this;
  }
}

dll = new DoublyLinkedList();
dll.push(1);
dll.push(2);
dll.push(3);
// dll.push(4);
// dll.insert(1, 1.5);
console.log(dll);
console.log(dll.reverse());
// console.log(dll.pop());
// console.log(dll.unshift(0));
// console.log(dll);
// dll.set(2, "CHANGED!");
