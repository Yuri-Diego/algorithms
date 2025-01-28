package Stack;

// Implementacao classica de uma Pilha

public class Stack<T> {
    private final Object[] items;
    private final int maxLength;
    private int pointer;

    public Stack(int maxLength) {
        this.maxLength = maxLength;
        this.items = new Object[maxLength];
        this.pointer = 0;
    }

    public boolean isEmpty(){
        return pointer == 0;
    }

    public void push(T item){
        if(pointer >= maxLength){
            throw new IndexOutOfBoundsException("Stack full");
        }
        items[pointer++] = item;
    }

    public T pop(){
        if(isEmpty()){
            throw new IndexOutOfBoundsException("Stack is empty");
        }
        T item = (T) items[--pointer];
        items[pointer] = null;
        return item;
    }

    public T peek(){
        if(isEmpty()){
            throw new IndexOutOfBoundsException("Stack is empty");
        }
        return (T) items[pointer - 1];
    }

    public int size(){
        return pointer;
    }
}
