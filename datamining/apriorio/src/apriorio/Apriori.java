package apriorio;

import java.io.*;
import java.util.*;

public class Apriori {

    public static void main(String[] args) throws Exception {
        Apriori ap = new Apriori(args);
    }

    private List<int[]> itemsets;
    private String transaFile;
    private int numItems; // number of different items in the dataset
    private int numTransactions;
    private double minSup;

    public Apriori(String[] args) throws Exception {
        String a[] = new String[2];
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter file name and min support");
        a[0] = sc.next();
        a[1] = sc.next();
        configure(a);
        go();
    }

    private void configure(String[] args) throws Exception {
        transaFile = args[0];

        minSup = (Double.valueOf(args[1]).doubleValue());
        if (minSup > 1 || minSup < 0) {
            throw new Exception("minSup: bad value");
        }

        // read file to find number of transacions
        numItems = 0;
        numTransactions = 0;
        BufferedReader data_in = new BufferedReader(new FileReader(transaFile));
        while (data_in.ready()) {
            String line = data_in.readLine();
            if (line.matches("\\s*")) {
                continue; // skip blank lines
            }
            numTransactions++;
            StringTokenizer t = new StringTokenizer(line, " ");
            while (t.hasMoreTokens()) {
                int x = Integer.parseInt(t.nextToken());
                //log(x);
                if (x + 1 > numItems) {
                    numItems = x + 1;
                }
            }
        }

        System.out.println("Input configuration: " + numItems + " items, " + numTransactions + " transactions, ");
        System.out.println("minsup = " + minSup + "%");

    }

    private void go() throws Exception {

        createItemsetsOfSize1();
        int itemsetNumber = 1; //the current itemset being looked at
        int nbFrequentSets = 0;

        while (itemsets.size() > 0) {

            calculateFrequentItemsets();

            if (itemsets.size() != 0) {
                nbFrequentSets += itemsets.size();
                log("Found " + itemsets.size() + " frequent itemsets of size " + itemsetNumber + " (with support " + (minSup * 100) + "%)");;
                createNewItemsetsFromPreviousOnes();
            }

            itemsetNumber++;
        }
        log("Found " + nbFrequentSets + " frequents sets for support " + (minSup * 100)/* + "% (absolute " + Math.round(numTransactions * minSup) + ")"*/);

    }

    private void createItemsetsOfSize1() {
        itemsets = new ArrayList<int[]>();
        for (int i = 0; i < numItems; i++) {
            int[] cand = {i};
            itemsets.add(cand);
        }
    }

    // passes through the data to measure the frequency of sets in
    // and filters those who are under the minimum support
    private void calculateFrequentItemsets() throws Exception {

        log("Passing through the data to compute the frequency of " + itemsets.size() + " itemsets of size " + itemsets.get(0).length);

        List<int[]> frequentCandidates = new ArrayList<int[]>(); //the frequent candidates for the current itemset

        boolean match; //whether the transaction has all the items in an itemset
        int count[] = new int[itemsets.size()]; //the number of successful matches, initialized by zeros

        // load the transaction file
        BufferedReader data_in = new BufferedReader(new InputStreamReader(new FileInputStream(transaFile)));

        boolean[] trans = new boolean[numItems];

        // for each transaction
        for (int i = 0; i < numTransactions; i++) {

            String line = data_in.readLine();
            line2booleanArray(line, trans);

            // check each candidate
            for (int c = 0; c < itemsets.size(); c++) {
                match = true; // reset match to false
                // tokenize the candidate so that we know what items need to be
                // present for a match
                int[] cand = itemsets.get(c);
                //int[] cand = candidatesOptimized[c];
                // check each item in the itemset to see if it is present in the
                // transaction
                for (int xx : cand) {
                    if (trans[xx] == false) {
                        match = false;
                        break;
                    }
                }
                if (match) { // if at this point it is a match, increase the count
                    count[c]++;
                    //log(Arrays.toString(cand)+" is contained in trans "+i+" ("+line+")");
                }
            }

        }

        data_in.close();

        for (int i = 0; i < itemsets.size(); i++) {
            // if the count% is larger than the minSup%, add to the candidate to
            // the frequent candidates
            if ((count[i] / (double) (numTransactions)) >= minSup) {
                // foundFrequentItemSet(itemsets.get(i), count[i]);
                System.out.println(Arrays.toString(itemsets.get(i)) + " Support: " + ((count[i] / (double) numTransactions)) + " " + count[i]);
                frequentCandidates.add(itemsets.get(i));
            }
            //else log("-- Remove candidate: "+ Arrays.toString(candidates.get(i)) + "  is: "+ ((count[i] / (double) numTransactions)));
        }

        //new candidates are only the frequent candidates
        itemsets = frequentCandidates;
    }

    /**
     * if m is the size of the current itemsets, generate all possible itemsets
     * of size n+1 from pairs of current itemsets replaces the itemsets of
     * itemsets by the new ones
     */
    private void createNewItemsetsFromPreviousOnes() {
        // by construction, all existing itemsets have the same size
        int currentSizeOfItemsets = itemsets.get(0).length;
        log("Creating itemsets of size " + (currentSizeOfItemsets + 1) + " based on " + itemsets.size() + " itemsets of size " + currentSizeOfItemsets);

        HashMap<String, int[]> tempCandidates = new HashMap<String, int[]>();

        // compare each pair of itemsets of size n-1
        for (int i = 0; i < itemsets.size(); i++) {
            for (int j = i + 1; j < itemsets.size(); j++) {
                int[] X = itemsets.get(i);
                int[] Y = itemsets.get(j);

                assert (X.length == Y.length);

                //make a string of the first n-2 tokens of the strings
                int[] newCand = new int[currentSizeOfItemsets + 1];
                for (int s = 0; s < newCand.length - 1; s++) {
                    newCand[s] = X[s];
                }

                int ndifferent = 0;
                // then we find the missing value
                for (int s1 = 0; s1 < Y.length; s1++) {
                    boolean found = false;
                    // is Y[s1] in X?
                    for (int s2 = 0; s2 < X.length; s2++) {
                        if (X[s2] == Y[s1]) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) { // Y[s1] is not in X
                        ndifferent++;
                        // we put the missing value at the end of newCand
                        newCand[newCand.length - 1] = Y[s1];
                    }

                }

                // we have to find at least 1 different, otherwise it means that we have two times the same set in the existing candidates
                assert (ndifferent > 0);

                if (ndifferent == 1) {
                    // HashMap does not have the correct "equals" for int[] :-(
                    // I have to create the hash myself using a String :-(
                    // I use Arrays.toString to reuse equals and hashcode of String
                    Arrays.sort(newCand);
                    tempCandidates.put(Arrays.toString(newCand), newCand);
                }
            }
        }

        //set the new itemsets
        itemsets = new ArrayList<int[]>(tempCandidates.values());
        log("Created " + itemsets.size() + " unique itemsets of size " + (currentSizeOfItemsets + 1));

    }

    /**
     * put "true" in trans[i] if the integer i is in line
     */
    private void line2booleanArray(String line, boolean[] trans) {
        Arrays.fill(trans, false);
        StringTokenizer stFile = new StringTokenizer(line, " "); //read a line from the file to the tokenizer
        //put the contents of that line into the transaction array
        while (stFile.hasMoreTokens()) {

            int parsedVal = Integer.parseInt(stFile.nextToken());
            trans[parsedVal] = true; //if it is not a 0, assign the value to true
        }
    }

    private void log(String message) {
        System.out.println(message);
    }
}