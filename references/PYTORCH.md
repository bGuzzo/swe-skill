# PyTorch Guidelines

1. Follow best practices when declaring models using the OOP provided by the package.

2. For math operations, always use descriptive comments, as some operations are complex (like `einsum`).
    * Use a comment to state the input and output shapes of the operation.
    * Use a comment to explain the operation, such as summation and aggregation over a specific dimension, vector product, etc.
    * Use different files and classes to compose a single model, then nest or loop the components to assemble the final model.

3. For complex operations or operations that require a deep understanding, always use a comment to reference the documentation page.
    * Example: `Ref: http://...`.

---