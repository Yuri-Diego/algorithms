package list;

// Implementacao Classica de uma Lista(list).

import java.util.NoSuchElementException;

public class List<T> {
    private int capacity;
    private Object[] items;
    private int size;


    public List() {
        this.capacity = 10;
        this.items = new Object[this.capacity];
        this.size = 0;

    }

    private void resize() {
        int newCapacity = capacity * 2;
        Object[] newData = new Object[newCapacity];
        System.arraycopy(items, 0, newData, 0, size);
        items = newData;
        capacity = newCapacity;
    }

    public void append(T item) {
        if (size == capacity) {
            resize();
        }
        items[size] = item;
        size++;
    }

    public void insert(T item, int index) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        if (size == capacity) {
            resize();
        }
        for (int i = size; i > index; i--) {
            items[i] = items[i - 1];
        }
        items[index] = item;
        size++;
    }

    public T pop(){
        if (size == 0) {
            throw new NoSuchElementException("list is empty");
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
        items[size - 1] = null;
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

