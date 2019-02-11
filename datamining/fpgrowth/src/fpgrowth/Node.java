package fpgrowth;

import java.util.*;

class Node {

    String itemname;
    int count;

    ArrayList<Node> children;

    public Node(String itemname) {
        this.itemname = itemname;
        count = 1;
        children = new ArrayList<Node>();
    }

    public Node(String itemname, int counter) {
        this(itemname);
        count = counter;
    }

    public Node insertChild(String name) {
        int index = findIndex(name);
        if (index == -1) {
            Node newChild = new Node(name);
            children.add(newChild);
            return newChild;
        } else {
            children.get(index).count += 1;
            return children.get(index);
        }
    }

    private int findIndex(String name) {
        for (int i = 0; i < children.size(); i++) {
            Node currentChild = children.get(i);
            if (name.equals(currentChild.itemname)) {
                return i;
            }
        }
        return -1;
    }

    public void print() {
        Queue<Node> queue = new LinkedList<Node>();

        System.out.println("Item Count");
        Node newnod = new Node("@");
        queue.add(this);
	queue.add(newnod);
        while (queue.peek() != null) {
            Node currentNode = queue.remove();
		if(currentNode.itemname != "@"){
	            System.out.print(currentNode.itemname + " " + currentNode.count+"\t");
         	   for (Node child : currentNode.children) {
         	       queue.add(child);
         	   }
		}
		else{	
			if(queue.peek() != null){
				Node newnode = new Node("@");
				queue.add(newnode);
			}
			System.out.println("");
		}
        }
    }
}

