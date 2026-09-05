# Clean Code Principles

Reference catalog of core principles and SOLID design rules from *Clean Code: A Handbook of Agile Software Craftsmanship* by Robert C. Martin. Use these principles to build clean, readable, testable, and maintainable software.

---

## SOLID Principles

### 1. Single Responsibility Principle (SRP)
- **How it works**: A class or module must have one, and only one, reason to change. Each class encapsulates a single responsibility or actor concern, isolating changes to that specific domain.
- **When to use**:
    * Designing classes, services, or modules to enforce high cohesion.
    * A class handles multiple business domains, operational roles, or lifecycle concerns.
- **When not to use**:
    * Trivial data transfer structures where splitting introduces needless boilerplate.
    * Highly cohesive operations that naturally belong together, where splitting obscures the workflow.

### 2. Open-Closed Principle (OCP)
- **How it works**: Software entities should be open for extension, but closed for modification. New behaviors are added by extending interfaces or implementing abstract classes, rather than altering existing tested code.
- **When to use**:
    * Systems expected to grow with new formats, drivers, plugins, or business rules.
    * Code where changes to core logic risk introducing regressions in existing workflows.
- **When not to use**:
    * Simple, stable features with zero anticipation of polymorphism or variation.
    * Premature abstraction that adds interface layers before requirements diverge.

### 3. Liskov Substitution Principle (LSP)
- **How it works**: Subtypes must be substitutable for their base types without altering the correctness of the program. Derived classes must adhere to the contract, invariants, and expected behavior of the parent abstraction.
- **When to use**:
    * Building class hierarchies and relying on polymorphism.
    * Ensuring consumers can interact with base interfaces without type checking or special-case handling.
- **When not to use**:
    * The child class cannot fulfill the base contract (e.g., throwing `UnsupportedOperationException`); use composition instead of inheritance.
    * Extending classes purely for code reuse rather than genuine semantic subtyping.

### 4. Interface Segregation Principle (ISP)
- **How it works**: Clients should not be forced to depend upon interfaces they do not use. Large, fat interfaces are broken down into smaller, role-specific interfaces tailored to specific consumer needs.
- **When to use**:
    * Interfaces accumulate unrelated methods required by disparate callers.
    * Changes to a consumer's interface requirements force recompilation or re-testing of unrelated clients.
- **When not to use**:
    * Small, cohesive interfaces that already serve a single focused client role.
    * Over-splitting interfaces into single-method declarations when the operations are intrinsically atomic.

### 5. Dependency Inversion Principle (DIP)
- **How it works**: High-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions. Dependencies are injected via interfaces.
- **When to use**:
    * Decoupling core business logic from databases, external services, UI, or frameworks.
    * Facilitating unit testing and test-driven development via dependency injection and mocks.
- **When not to use**:
    * Stable, deterministic standard library dependencies (e.g., string or math utilities).
    * Trivial scripts where dependency injection harnesses create unjustified setup overhead.

---

## Core Clean Code Principles

### 1. The Boy Scout Rule
- **How it works**: Always leave the campground cleaner than you found it. Check in code that is cleaner than when you checked it out by making continuous, opportunistic micro-refactorings.
- **When to use**:
    * Every time you touch existing code, fix a bug, or add a feature.
    * Renaming unclear variables, decomposing bloated functions, and eliminating dead code during normal development.
- **When not to use**:
    * Scope-creeping large architectural rewrites into urgent, critical hotfixes.
    * Introducing breaking API changes without team coordination.

### 2. Small Functions & Do One Thing
- **How it works**: Functions should be small (ideally under 20 lines) and do only one thing well. Decompose algorithms into small support functions where each method executes a single logical step.
- **When to use**:
    * Any function handling multiple steps, multiple levels of abstraction, or nested branching logic.
    * Improving testability, cognitive load, and reusability of individual logic units.
- **When not to use**:
    * Fragmenting simple, straight-line operations where jumping across methods impairs readability.
    * Tightly coupled hardware or performance-critical loops where function call overhead is prohibitive.

### 3. Single Level of Abstraction (SLAP) & Stepdown Rule
- **How it works**: All statements within a function must operate at the same conceptual level of abstraction. High-level orchestrations delegate to mid-level helpers, which delegate to low-level primitives, reading as a top-down narrative.
- **When to use**:
    * Structuring master functions to read like high-level algorithm summaries.
    * Eliminating mixing of business concepts with raw byte manipulation, string formatting, or SQL queries.
- **When not to use**:
    * Ultra-low-level driver or kernel code where raw operations are the explicit concern.
    * Creating redundant wrapper methods that merely forward arguments without abstracting anything.

### 4. Don't Repeat Yourself (DRY)
- **How it works**: Every piece of knowledge must have a single, unambiguous, authoritative representation within a system. Factor out duplicated logic, structures, and algorithms into shared abstractions.
- **When to use**:
    * Identical or near-identical business rules, validation routines, or algorithms appear in multiple locations.
    * Changes to a requirement force manual edits across multiple files.
- **When not to use**:
    * Accidental duplication where two pieces of code look similar but evolve for completely different business reasons.
    * Creating tight coupling between unrelated microservices or modules solely to share minor boilerplate.

### 5. Command Query Separation (CQS)
- **How it works**: A function should either perform an action (command) or answer a question (query), but never both. Mutating state and returning data are strictly separated to eliminate hidden side effects.
- **When to use**:
    * Designing public APIs, service methods, and entity operations.
    * Eliminating confusing side effects in getters or validation checks.
- **When not to use**:
    * Atomic concurrent operations (e.g., `queue.pop()` or `compareAndSet`) where state modification and return value must execute atomically.
    * Standard builder fluent APIs chaining mutation calls.

### 6. Explain Yourself in Code (Comments as Failure)
- **How it works**: Code should be self-documenting. Use descriptive identifiers, small functions, and clear structure to express intent directly in code; treat comments as an admission of failure to express intent cleanly.
- **When to use**:
    * When tempted to write a comment explaining what a code block does; extract it into a well-named function instead.
    * Clarifying intent solely through clear function, class, and variable names.
- **When not to use**:
    * Legal disclaimers, license headers, and public API specifications.
    * Documenting non-obvious business rationale, mathematical invariants, or external issue tickets (`Ref: http://...`).

### 7. Law of Demeter (Principle of Least Knowledge)
- **How it works**: A method should only call methods on its own object, parameters passed to it, objects it instantiates, or direct instance components. Avoid chained navigation through third-party objects (train wrecks).
- **When to use**:
    * Decoupling callers from the internal object graph and structure of collaborators.
    * Preventing cascading failures when nested object representations change.
- **When not to use**:
    * Fluent interfaces, builders, or query language DSLs designed specifically for method chaining.
    * Simple Data Transfer Objects (DTOs) and data structures with public data and no behavior.

### 8. Clean Error Handling & No Nulls
- **How it works**: Prefer exceptions to return codes; isolate error handling into distinct try/catch blocks. Never return `null` and never pass `null` into methods; use empty collections, Optional wrappers, or Null Objects instead.
- **When to use**:
    * Normal application workflows where error cases should not clutter the primary execution path.
    * Eradicating ubiquitous defensive null checks and preventing `NullPointerException` crashes.
- **When not to use**:
    * Performance-critical internal loops where throwing exceptions incurs prohibitive stack-trace overhead.
    * Interfacing with legacy third-party libraries that explicitly mandate null indicators.

### 9. F.I.R.S.T. Clean Tests
- **How it works**: Unit tests must follow the F.I.R.S.T. criteria: Fast (run in milliseconds), Independent (no order dependencies), Repeatable (pass in any environment), Self-Validating (boolean pass/fail), and Timely (written with or before production code).
- **When to use**:
    * Designing all automated unit and integration test suites.
    * Establishing a trustworthy regression harness that enables confident, fearless refactoring.
- **When not to use**:
    * High-level black-box performance, smoke, or stress tests that inherently require long runtimes.
    * Disposable exploratory scripts not meant for regression pipelines.

### 10. Separate Construction from Use
- **How it works**: Decouple the startup logic of instantiating and wiring objects from the runtime logic of using them. Centralize object creation in `main`, factory classes, or Dependency Injection containers.
- **When to use**:
    * Managing service lifecycles, configuration loading, and dependency wiring.
    * Allowing components to be swapped out easily for testing or environment-specific alternatives.
- **When not to use**:
    * Creating transient, lightweight value objects (e.g., coordinate pairs, strings, or domain primitives).
    * Standalone CLI utilities with minimal configuration and no swappable dependencies.
