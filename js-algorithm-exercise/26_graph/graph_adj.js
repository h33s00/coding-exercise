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
}

let g = new Graph();
g.addVertex("Tokyo");
g.addVertex("Seoul");
g.addVertex("Osaka");
console.log(g);
g.addEdge("Tokyo", "Seoul");
console.log(g);
// g.removeEdge("Seoul", "Tokyo");
console.log(g);
g.removeVertex("Seoul");
console.log(g);
