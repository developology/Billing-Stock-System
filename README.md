# Billing-Stock-System


#### 1. **Global Variable**

- **`BillingDict = {}`**
  - **Purpose**: This is an empty dictionary used to store billing information.
  - **Structure**: 
    - Keys: SKU numbers (unique product identifiers).
    - Values: Dictionaries containing product details.

#### 2. **Function: `InputFun()`**

- **Purpose**: Collects product details from the user and stores them in `BillingDict`.

- **Steps**:
  - **Loop**: Runs continuously until the user decides to stop.
    - **Inputs**:
      - **SKU**: Unique number for each product.
      - **Product Name**: Name of the product.
      - **QT**: Quantity of the product.
      - **SinglePrice**: Price for one unit of the product.
    - **Storing Data**: Adds the product details to `BillingDict` using the SKU as the key.
    - **Prompt for More Items**:
      - **User Input**:
        - If `y` or `Y`: Continues the loop to enter more products.
        - If `n` or `N`: Calls `AddMoreNo()` to search for items and then breaks the loop.
        - Any other input: Prints "Invalid Input" and breaks the loop.

#### 3. **Function: `AddMoreNo()`**

- **Purpose**: Searches for a product by its SKU and displays its details.

- **Steps**:
  - **Prompt for SKU**: Asks the user to enter the SKU number of the product they want to search.
  - **Search**:
    - **Iterates**: Goes through each SKU in `BillingDict`.
    - **Match Found**: If the SKU matches:
      - Displays total cost, product name, quantity, and single price.
      - Breaks out of the loop.
    - **No Match**: If no SKU matches:
      - The `else` block of the `for` loop executes, printing "No such SKU Number present."

### Summary

- **`BillingDict`**: Holds product data.
- **`InputFun()`**: Collects and stores product details, and controls the flow based on user input.
- **`AddMoreNo()`**: Searches for and displays product details or informs the user if the SKU is not found.


### Struture of the Dictionary 


![image](https://github.com/user-attachments/assets/00ab9754-2eb0-42bb-b9d9-f2773b2a8c9d)


### Input & Output Expected


![image](https://github.com/user-attachments/assets/298e36f5-549d-455f-a656-91591234b8d3)

