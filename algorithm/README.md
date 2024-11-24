# FindingPair

`FindingPair` is a Python class designed to find a pair of numbers in a list whose sum equals a given target. The class includes three different approaches, each with its own efficiency characteristics.

---

## Class Overview

### Initialization
The class is initialized with:
- `nums`: A list of integers to search within.
- `target`: The target sum to find.

```python
finder = FindingPair(nums=[2, 5, 3, 8, 6, 11], target=8)
```

---

## Methods

### 1. `approach_one()`
This method iterates through the list, checking for each number whether its complement (difference from the target) exists in the list. It skips pairs where both numbers are the same.

#### Time Complexity
- Outer loop: \(O(n)\)
- Inner `in` operation: \(O(n)\) for each number
- Overall: \(O(n^2)\)

#### Space Complexity
- Overall: \(O(1)\)

#### Example
```python
finder.approach_one()  # Output: (2, 6)
```

---

### 2. `approach_two()`
This method uses a dictionary to track numbers seen so far and checks whether the complement is already in the dictionary.

#### Time Complexity
- Loop through `nums`: \(O(n)\)
- Dictionary operations (`in` and assignment): \(O(1)\) each
- Overall: \(O(n)\)

#### Space Complexity
- Uses a dictionary to store up to \(n\) elements.
- Overall: \(O(n)\)

#### Example
```python
finder.approach_two()  # Output: (3, 5)
```

---

### 3. `approach_three()`
This method first sorts the list and then uses two pointers to find the pair.

#### Time Complexity
- Sorting: \(O(n log n)\)
- Two-pointer traversal: \(O(n)\)
- Overall: \(O(n log n)\)

#### Space Complexity
- Overall: \(O(1)\) if sorting in place
```python
self.nums.sort()
```
- \(O(n)\) otherwise
```python
nums = sorted(self.nums)
```

#### Example
```python
finder.approach_three()  # Output: (2, 6)
```

---

## Usage Example

```python
numbers = [2, 5, 3, 8, 6, 11]
target = 8
finder = FindingPair(nums=numbers, target=target)

print(f'Approach One => pair with {target} as summation is: {finder.approach_one()}')
print(f'Approach Two => pair with {target} as summation is: {finder.approach_two()}')
print(f'Approach Three => pair with {target} as summation is: {finder.approach_three()}')
```

### Sample Output
```
Approach One => pair with 8 as summation is: (2, 6)
Approach Two => pair with 8 as summation is: (3, 5)
Approach Three => pair with 8 as summation is: (2, 6)
```

---

## Conclusion
The `FindingPair` class provides flexible solutions to finding pairs with a given sum:
- Use **Approach One** for simplicity.
- Use **Approach Two** for speed.
- Use **Approach Three** for space efficiency.
