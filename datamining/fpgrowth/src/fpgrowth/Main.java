package fpgrowth;

import java.util.*;
import java.io.*;

class Main {

    ArrayList<ArrayList<String>> db = new ArrayList<ArrayList<String>>();
    HashMap<String, Integer> linkedlist = new HashMap<String, Integer>();
    Node fpTree;

    int minSupp = 3; 

    private ArrayList<ArrayList<String>> patternBase 
        = new ArrayList<ArrayList<String>>();
    private ArrayList<Integer> patternBaseCounter
        = new ArrayList<Integer>();

    private ArrayList<Pair<ArrayList<String>, Integer>> frequentItems
        = new ArrayList<Pair<ArrayList<String>, Integer>>();

    void run() {
        getInput("/home/placements2019/Documents/Parth/datamining/fpgrowth/src/fpgrowth/Data.txt");
        calculateFrequency();

        sortDatabase();

        fpTree = createTree(db);
        findFrequentItemsets(fpTree);

        display();
    }

    void display() {
        //System.out.println("ITEMS");
        System.out.println(linkedlist);
        System.out.println("");

       // System.out.println("TRANSACTIONS");
        System.out.println(db);
        System.out.println("");

       // System.out.println("FP TREE");
        fpTree.print();
        System.out.println("");
    }

    Node createTree(ArrayList<ArrayList<String>> data) {
        ArrayList<Integer> counter = new ArrayList<Integer>();
        for (int i = 0; i < data.size(); i++) {
            counter.add(1);
        }
        return createTree(data, counter);
    }

    Node createTree(ArrayList<ArrayList<String>> data, 
            ArrayList<Integer> counter) {
        Node tree = new Node("null");
        for (int i = 0; i < data.size(); i++) {
            ArrayList<String> transaction = data.get(i);
            for (int j = 0; j < counter.get(i); j++) {
                Node branch = tree;
                for (String item : transaction) {
		    if(linkedlist.get(item)>=minSupp) {
                    	branch = branch.insertChild(item);
		    }
                }
            }
        }
        return tree;
    }

    void findFrequentItemsets(Node fpTree) {
        for (String item : linkedlist.keySet()) {
	    if(linkedlist.get(item)>=minSupp) {
            System.out.print(item + " -> ");
            findFrequentItemsets(fpTree, item);

            Node patternTree = createTree(patternBase, patternBaseCounter);
            patternTree.print();
            mine(item, patternTree);
            System.out.println("");
	    }
        }        
    }

    ArrayList<Pair<ArrayList<String>, Integer>> mine(String item, Node patternTree) {
        for (Node child : patternTree.children) {
            ArrayList<Node> path = new ArrayList<Node>();
            mine(item, child, path);
        }
        System.out.println(frequentItems);
        ArrayList<Pair<ArrayList<String>, Integer>> copy 
            = new ArrayList<Pair<ArrayList<String>, Integer>>(frequentItems);
        frequentItems.clear();
        return copy;
    }

    void mine(String item, Node patternTree, ArrayList<Node> path) {
        if (patternTree.count < minSupp) {
            return;
        }
        addToFrequent(item, patternTree);
        path.add(patternTree);
        if (path.size() > 1) {
            ArrayList<Node> copyPath = new ArrayList<Node>(path);
            addToFrequent(item, copyPath);
        }
        for (Node child : patternTree.children) {
            mine(item, child, path);
        }
    }

    void findFrequentItemsets(Node fpTree, String item) {
        patternBase.clear();
        patternBaseCounter.clear();
        ArrayList<String> path = new ArrayList<String>();
        findPatternBase(fpTree, item, path);
        System.out.println(patternBase);
    }

    void findPatternBase(Node currNode, String item, ArrayList<String> path) {
        if (currNode.itemname.equals(item)) {
            ArrayList<String> currPath = new ArrayList<String>(path);
            patternBase.add(removeNull(currPath));
            patternBaseCounter.add(currNode.count);
        } else {
            path.add(currNode.itemname);
            for (Node child : currNode.children) {
                findPatternBase(child, item, path);
            }
            path.remove(currNode.itemname);
        }
    }

    ArrayList<String> removeNull(ArrayList<String> arr) {
        if (arr.size() <= 1) {
            return new ArrayList<String>();
        } else {
            ArrayList<String> removed = new ArrayList<String>(arr.subList(1,
                        arr.size()));
            return removed;
        }
    }

    void addToFrequent(String item, Node node) {
        ArrayList<String> current = new ArrayList<String>();
        current.add(node.itemname);
        current.add(item);
        frequentItems.add(new Pair<ArrayList<String>, Integer>
                (current, node.count));
    }

    void addToFrequent(String item, ArrayList<Node> path) {
        ArrayList<String> current = new ArrayList<String>();
        for (Node node : path) {
            current.add(node.itemname);
        }
        current.add(item);
        frequentItems.add(new Pair<ArrayList<String>, Integer>
                (current, path.get(path.size()-1).count));
    }

    class Comp implements Comparator<String> {
        public int compare(String item1, String item2) {
            /*For reverse sorting*/
            return linkedlist.get(item2) - linkedlist.get(item1);
        }
    }

    void sortDatabase() {
        for (ArrayList<String> transaction : db) {
            Collections.sort(transaction, new Comp());
        }
    }

    void calculateFrequency() {
        for (ArrayList<String> transaction : db) {
            for (String item : transaction) {
                if (linkedlist.get(item) == null) {
                    linkedlist.put(item, 1);
                } else {
                    linkedlist.put(item, linkedlist.get(item) + 1);
                }
            }
        }
    }

    void getInput(String filename) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            String input;
            while ((input = br.readLine()) != null) {
                parseInput(input);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    void parseInput(String input) {
        String[] split = input.split(" ");
        ArrayList<String> transaction = new ArrayList<String>();
        for (String item : split) {
            transaction.add(item);
        }
        db.add(transaction);
    }

    public static void main(String[] args) {
        new Main().run();
    }
}