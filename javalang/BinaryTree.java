package javalang;

public class BinaryTree {

    Node root ;

    public void add(int data){
        Node newNode = new Node(data);
        if(root == null){
            root = newNode;
        }else{
            if(root.data > newNode.data){
                root.right = newNode ;
            }else{
                root.left = newNode;
            }
        }
    }
    
}

class Node{
    int data;
    Node left;
    Node right;
    
    Node(int data){
        this.data = data;
    }
}