import java.io.*;
class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		binarySearchTree b = new binarySearchTree();
		String str = null;
		while ((str = br.readLine()) != null && str.length() != 0) {
				int i = Integer.parseInt(str); 
				b.insert(i);
			}
			br.close();
			b.postOrder(b.root);
		}
}
class Node {
	private int data;
	private Node left;
	private Node right;
	public Node(int data) {
		this.setData(data);
		setLeft(null);
		setRight(null);
	}
	public int getData() {
		return data;
	}
	public void setData(int data) {
		this.data = data;
	}
	public Node getLeft() {
		return left;
	}
	public void setLeft(Node left) {
		this.left = left;
	}
	public Node getRight() {
		return right;
	}
	public void setRight(Node right) {
		this.right = right;
	}
}
class binarySearchTree {
	public Node root;
	public binarySearchTree() {
		this.root = null;
	}
	public void insert(int id) {
		Node newNode = new Node(id);
		if (root==null) {
			root = newNode;
			return;
		}
		Node current = root;
		Node parent = null;
		while(true) {
			parent = current;
			if(id < current.getData()) {
				current = current.getLeft();
				if(current==null) {
					parent.setLeft(newNode);
					return;
				}
			} else {
				current = current.getRight();
				if(current==null) {
					parent.setRight(newNode);
					return;
				}
			}
		}
	}
	public void postOrder(Node root) {
		if(root==null) {
			return;
		}
		postOrder(root.getLeft());
		postOrder(root.getRight());
		System.out.print(root.getData() + " ");
	}
}