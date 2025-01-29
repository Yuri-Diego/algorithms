package list;

// Implementacao Classica de uma Lista(list).

public class List<T> {
    private int capacity;
    private Object[] items;
    private int size;


    public List() {
        this.capacity = 10;
        this.items = new Object[this.capacity];
        this.size = 0;

    }

    public void _resize() {
        int newCapacity = capacity * 2;
        Object[] newData = new Object[newCapacity];

        for (int i = 0; i < this.size; i++) {
            newData[i] = items[i];
        }
        items = newData;
        capacity = newCapacity;
    }

    public void append(T item) {
        if (size == capacity) {
            _resize();
        }
        items[size] = item;
        size++;
    }

    public void insert(T item, int index) {
        if (size == capacity) {
            _resize();
        }
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        for (int i = size; i > index; i--) {
            items[i] = items[i - 1];
        }
        items[index] = item;
        size++;
    }

    public T pop(){
        if (size == 0) {
            throw new IndexOutOfBoundsException("list is empty");
        }
        size--;
        T value = (T) items[size];
        items[size] = null;
        return value;
    }

    public T remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        T item = (T) items[index];
        for (int i = index; i < size - 1; i++) {
            items[i] = items[i + 1];
        }
        size--;
        return item;
    }

    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        return (T) items[index];
    }

}

