class Graph {
  constructor() {
    this.adjList = {};
  }
  addVertex(v) {
    if (!this.adjList[v]) this.adjList[v] = [];
  }

  // undirected graph
  addEdge(v1, v2) {
    this.adjList[v1].push(v2);
    this.adjList[v2].push(v1);
  }

  removeEdge(v1, v2) {
    this.adjList[v1] = this.adjList[v1].filter((v) => v !== v2);
    this.adjList[v2] = this.adjList[v2].filter((v) => v !== v1);
  }

  removeVertex(v) {
    for (let e of this.adjList[v]) {
      this.removeEdge(e, v);
    }
    delete this.adjList[v];
  }

  recursiveDFS(start) {
    let result = [];
    let visited = {};
    const adjList = this.adjList;

    // in this helper function, this refers to recursiveDFS
    function helperDFS(v) {
      if (!v) return null;
      if (!visited[v]) visited[v] = true;
      result.push(v);
      for (let adj of adjList[v]) {
        if (!visited[adj]) helperDFS(adj);
      }
    }

    helperDFS(start);
    return result;
  }

  iterativeDFS(start) {
    // stack
    let S = [start];
    let result = [];
    let visited = {};
    let currV;

    visited[start] = true;

    while (S.length > 0) {
      // console.log(S);
      currV = S.pop();
      result.push(currV);
      for (let adj of this.adjList[currV]) {
        if (!visited[adj]) {
          visited[adj] = true;
          S.push(adj);
        }
      }
    }

    return result;
  }

  iterativeBFS(start) {
    // queue
    let queue = [start];
    let result = [];
    let visited = {};
    let currV;

    visited[start] = true;

    while (queue.length > 0) {
      console.log(queue);
      currV = queue.shift();
      result.push(currV);
      for (let adj of this.adjList[currV]) {
        if (!visited[adj]) {
          visited[adj] = true;
          queue.push(adj);
        }
      }
    }
    return result;
  }
}

let g = new Graph();
let nodes = ["A", "B", "C", "D", "E", "F"];
for (let node of nodes) {
  g.addVertex(node);
}
g.addEdge("A", "B");
g.addEdge("A", "C");
g.addEdge("B", "D");
g.addEdge("D", "E");
g.addEdge("D", "F");
g.addEdge("C", "E");
g.addEdge("E", "F");

console.log(g);
console.log(g.recursiveDFS("A"));
console.log(g.iterativeDFS("A"));
console.log(g.iterativeBFS("A"));
