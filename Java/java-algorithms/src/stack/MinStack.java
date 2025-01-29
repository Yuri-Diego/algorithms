package stack;

public class MinStack<T extends Comparable<T>> {
    private final Stack<T> stack;
    private final Stack<T> minStack;

    public MinStack(int maxLength) {
        this.stack = new Stack<T>(maxLength);
        this.minStack = new Stack<T>(maxLength);
    }

    public void push(T item) {
        stack.push(item);
        if (minStack.isEmpty() || item.compareTo(minStack.peek()) <= 0 ) {
           minStack.push(item);
        } else {
            minStack.push(minStack.peek());
        }
    }

    public T pop() {
        if (stack.isEmpty()) {
            throw new IndexOutOfBoundsException("Stack is empty");
        }
        minStack.pop();
        return stack.pop();
    }

    public T getMin() {
        if (stack.isEmpty()) {
            throw new IndexOutOfBoundsException("Stack is empty");
        }
        return minStack.peek();
    }
}
