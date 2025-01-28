package Queue;

// Implementacao Classica de uma Fila(queue) Circular.

public class queue<T> {
    private final Object[] items;
    private final int capacity;
    private int front;
    private int pointer;
    private int size;

    public queue(int capacity) {
        this.capacity = capacity;
        items = new Object[capacity];
        front = 0;
        pointer = 0;
        size = 0;
    }

    public void enqueue(T value) {
        if (size >= capacity) {
            throw new IndexOutOfBoundsException("Queue is full");
        }
        items[pointer] = value;
        pointer = (pointer + 1) % capacity;
        size++;
    }

    public T dequeue() {
        if (size == 0) {
            throw new IndexOutOfBoundsException("Queue is empty");
        }
        T value = (T) items[front];
        items[front] = null;
        front = (front + 1) % capacity;
        size--;
        return value;
    }

    public T peek() {
        if (size == 0) {
            throw new IndexOutOfBoundsException("Queue is empty");
        }
        return (T) items[front];
    }

    public int size() {
        return size;
    }
}
