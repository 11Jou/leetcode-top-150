import java.util.ArrayList;

class MinStack {

    private ArrayList<Integer> stack;
    private ArrayList<Integer> minStack;



    public MinStack() {
        stack = new ArrayList<Integer>();
        minStack = new ArrayList<Integer>();

    }
    
    public void push(int val) {

        stack.add(val);

        if (minStack.isEmpty() || val <= minStack.get(minStack.size() - 1)){
            minStack.add(val);
        }
    }
    
    public void pop() {

        if (stack.isEmpty()) return;

        int removed = stack.remove(stack.size() - 1);

        if(removed == minStack.get(minStack.size() - 1)){
            minStack.remove(minStack.size() - 1);
        }    
    }
    
    public int top() {

        return stack.get(stack.size() - 1);
    }
    
    public int getMin() {

        return minStack.get(minStack.size() - 1);
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
