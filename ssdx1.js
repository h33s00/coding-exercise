class Graph {
  constructor() {
    this.adjList = {};
  }
  addVertex(v) {
    if (!this.adjList[v]) this.adjList[v] = [];
  }

  // directed graph
  addEdge(v1, v2) {
    this.adjList[v1].push(v2);
  }

  removeEdge(v1, v2) {
    this.adjList[v1] = this.adjList[v1].filter((v) => v != v2);
    this.adjList[v2] = this.adjList[v2].filter((v) => v != v1);
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

    // in this helper function, 'this' refers to recursiveDFS
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
}

function mainDFS(G) {
  let visit = [];
  let area = 0;
  for (let node of Object.keys(G.adjList)) {
    if (!visit.includes(node)) {
      visit = visit.concat(G.iterativeDFS(node));
      area++;
    }
  }
  return area;
}

function solution(land, N) {
  let answer;
  let g = new Graph();

  // turn land to a graph
  for (let i = 0; i < N; i++) {
    for (let k = 0; k < N; k++) {
      let vertex = [i, k].toString();
      g.addVertex(vertex);

      if (i - 1 >= 0) {
        left = [i - 1, k].toString();
        g.addEdge(vertex, left);
      }
      if (k - 1 >= 0) {
        up = [i, k - 1].toString();
        g.addEdge(vertex, up);
      }
      if (i + 1 < N) {
        right = [i + 1, k].toString();
        g.addEdge(vertex, right);
      }
      if (k + 1 < N) {
        down = [i, k + 1].toString();
        g.addEdge(vertex, down);
      }
    }
  }

  console.log("Initial \n", g.adjList);

  // start sinking
  let x = 1;
  while (Object.keys(g.adjList).length > 0) {
    for (let i = 0; i < N; i++) {
      for (let k = 0; k < N; k++) {
        if (land[i][k] == x) {
          g.removeVertex([i, k].toString());
        }
      }
    }
    console.log("At", x, "\n", g.adjList);
    a = mainDFS(g);
    if (!answer || answer < a) answer = a;
    x++;
  }
  return answer;
}

let land = [
  [6, 8, 2, 6, 2],
  [3, 2, 3, 4, 6],
  [6, 7, 3, 3, 2],
  [7, 2, 5, 3, 6],
  [8, 9, 5, 2, 7],
];
let N = 5;
console.log(solution(land, N));
