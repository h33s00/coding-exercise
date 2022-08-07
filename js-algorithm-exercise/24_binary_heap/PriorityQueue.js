class Node {
  constructor(val, p) {
    this.value = val;
    this.priority = p;
  }
}
class PriorityQueue {
  constructor() {
    this.queue = [];
  }
  enqueue(val, p) {
    let newNode = new Node(val, p);
    this.queue.push(newNode);
    this.bubbleUp();
  }
  bubbleUp() {
    let idx = this.queue.length - 1;
    const newNode = this.queue[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.queue[parentIdx];
      if (newNode.priority > parent.priority) break;
      this.queue[parentIdx] = newNode;
      this.queue[idx] = parent;
      idx = parentIdx;
    }
  }
  dequeue() {
    // edge case
    if (this.queue.length == 0) {
      return undefined;
    }
    if (this.queue.length == 1) {
      return this.queue.pop();
    }
    // swap the first value with the last one
    let newRoot = this.queue.pop();
    this.queue.push(this.queue[0]);
    this.queue[0] = newRoot;
    // pop the minimum priority's node (ex-root)
    const exRoot = this.queue.pop();
    this.sinkDown();
    return exRoot;
  }
  sinkDown() {
    let idx = 0;
    const length = this.queue.length;
    const newRoot = this.queue[0];
    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let left, right;
      let swap = null;

      if (leftIdx < length) {
        left = this.queue[leftIdx];
        if (left.priority < newRoot.priority) {
          swap = leftIdx;
        }
      }
      if (rightIdx < length) {
        right = this.queue[rightIdx];
        if (
          (right.priority < newRoot.priority && swap == null) ||
          (right.priority < newRoot && right.priority < left.priority)
        ) {
          swap = rightIdx;
        }
      }
      if (swap == null) break;

      this.queue[idx] = this.queue[swap];
      this.queue[swap] = newRoot;
      idx = swap;
    }
  }
}

pqueue = new PriorityQueue();
pqueue.enqueue("eat snack", 3);
pqueue.enqueue("go to work", 1);
pqueue.enqueue("tease my bro", 6);
pqueue.enqueue("text my bf", 2);
console.log(pqueue);
pqueue.dequeue();
console.log(pqueue);
pqueue.dequeue();
console.log(pqueue);
pqueue.dequeue();
console.log(pqueue);
