import java.util.*;

public class graph {
    int v;
    LinkedList<Integer> adj[];

    graph(int v) { // new graph(5);
        this.v = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; i++) { // 0,1,2,3,4
            adj[i] = new LinkedList<>();
        }
    }

    void addEdge(int v, int w) { // v - vertices, w - weight
        adj[v].add(w);
    }

    void bfs(int s) {
        boolean visited[] = new boolean[v];
        LinkedList<Integer> queue = new LinkedList<>();
        visited[s] = true;
        queue.add(s);

        while(!queue.isEmpty()){
            int x = queue.poll();
            System.out.print(x + " ");

            Iterator<Integer> i = adj[x].listIterator();
            while(i.hasNext()){
                int n = i.next();
                if(!visited[n]){
                    visited[n] = true;
                    queue.add(n);
                }
            }
            
        }
    }

    void DFSUtil(int v, boolean visited[]) {
        visited[v] = true;
        System.out.print(v + " ");

        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }

    void dfs(int i){
        boolean visited[] = new boolean[v];
        DFSUtil(i, visited);
    }

    public static void main(String[] args) {
        graph g = new graph(5);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(1, 0);
        g.addEdge(1, 4);
        g.addEdge(3, 1);
        g.addEdge(4, 1);
        g.addEdge(4,2);

        g.bfs(0);
        System.out.println();
        g.dfs(0);
    }

}
