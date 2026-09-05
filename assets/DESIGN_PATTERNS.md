# Design Patterns

Reference catalog of the 23 classic design patterns from *Design Patterns: Elements of Reusable Object-Oriented Software* (Gang of Four). Use these patterns to build decoupled, maintainable, and robust object-oriented systems.

---

## Creational Patterns

### 1. Abstract Factory
- **How it works**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes. Clients interact solely with abstract interfaces, while concrete factory subclasses instantiate the concrete products.
- **When to use**:
    * A system must be independent of how its products are created, composed, and represented.
    * A system must be configured with one of multiple families of products.
    * A family of related product objects must be enforced to be used together.
    * You want to provide a product library while revealing only interfaces, not implementations.
- **When not to use**:
    * You only need to create standalone, unrelated products (prefer Factory Method).
    * Product families extend frequently; adding new product types forces interface changes across all concrete factories.

### 2. Builder
- **How it works**: Separates the construction of a complex object from its representation so that the same construction process can create different representations. A director class orchestrates the step-by-step assembly through a generic builder interface.
- **When to use**:
    * The algorithm for creating a complex object must be independent of the parts and their assembly process.
    * The construction process must allow different representations for the constructed object.
- **When not to use**:
    * Objects are simple, uniform, or do not require a multi-step construction process.
    * The products do not share common assembly steps or construction abstractions.

### 3. Factory Method
- **How it works**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate. The creator defers instantiation logic to concrete subclasses through an overridden method.
- **When to use**:
    * A class cannot anticipate the concrete class of objects it must create.
    * A class wants its subclasses to specify the objects it creates.
    * Classes delegate responsibilities to helper subclasses, and you want to localize knowledge of which helper to instantiate.
- **When not to use**:
    * Object instantiation is trivial and does not vary across polymorphic boundaries.
    * Subclassing solely to instantiate a specific class adds unnecessary hierarchy complexity.

### 4. Prototype
- **How it works**: Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype. Clients instantiate products by requesting clones of pre-configured prototype objects.
- **When to use**:
    * A system must be independent of how its products are created, composed, and represented.
    * Classes to instantiate are specified at runtime (e.g., dynamic loading).
    * You want to avoid building parallel factory class hierarchies.
    * Instances of a class have only a few combinations of state.
- **When not to use**:
    * Objects have complex internal structures with circular references or pointers that do not support deep cloning cleanly.
    * Object instantiation via standard constructors is straightforward and fast.

### 5. Singleton
- **How it works**: Ensures a class has only one instance and provides a global point of access to it. The class encapsulates its own creation and provides a static method that returns its sole, lazily or eagerly initialized instance.
- **When to use**:
    * Exactly one instance of a class must exist, accessible to clients through a well-known access point.
    * The sole instance should be extensible by subclassing, and clients must be able to use an extended instance without code modification.
- **When not to use**:
    * The pattern introduces hidden global state and tight coupling across callers.
    * Multiple instances, concurrent isolations, or mock replacements for unit testing are required.

---

## Structural Patterns

### 6. Adapter
- **How it works**: Converts the interface of a class into another interface clients expect. It allows classes with incompatible interfaces to work together by wrapping an adaptee instance or inheriting its interface.
- **When to use**:
    * You want to use an existing class whose interface does not match the required target interface.
    * You want to build a reusable class that cooperates with unrelated or unforeseen classes.
- **When not to use**:
    * You have direct access to alter and refactor the interface of the original class.
    * The behavioral semantics of the two interfaces diverge fundamentally, requiring extensive logic rewrites rather than signature adaptation.

### 7. Bridge
- **How it works**: Decouples an abstraction from its implementation so that the two can vary independently. The abstraction maintains a reference to an implementor interface and delegates execution, avoiding compile-time bindings.
- **When to use**:
    * You want to avoid a permanent binding between an abstraction and its implementation.
    * Both abstractions and their implementations must be extensible independently via subclassing.
    * Changes in an implementation must have zero impact on client code.
- **When not to use**:
    * There is only a single, stable implementation with no requirement for runtime switching or platform independence.
    * The abstraction and implementation are tightly coupled by design, making separation artificial.

### 8. Composite
- **How it works**: Composes objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly through a shared component interface.
- **When to use**:
    * You want to represent part-whole hierarchies of objects.
    * Clients should be able to ignore the difference between compositions of objects and individual leaf objects.
- **When not to use**:
    * The system requires strict compile-time type restrictions on which components can contain which children.
    * The data structure is flat and non-hierarchical.

### 9. Decorator
- **How it works**: Attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing by wrapping a target component and augmenting behavior before or after delegating requests.
- **When to use**:
    * To add responsibilities to individual objects dynamically and transparently without affecting other objects.
    * For responsibilities that can be withdrawn or combined dynamically.
    * When extension via subclassing causes a combinatorial explosion of classes.
- **When not to use**:
    * Code depends on object identity; a decorated component is not identical to the original object.
    * Architectures where having many small, similar-looking decorator wrappers hinders debugging and tracing.

### 10. Facade
- **How it works**: Provides a unified, simplified interface to a set of interfaces in a subsystem. Facade defines a higher-level entry point that makes the subsystem easier to use by routing calls to internal classes.
- **When to use**:
    * You want to provide a simple, high-level interface to a complex subsystem.
    * There are too many tight dependencies between clients and the implementation classes of an abstraction.
    * You want to layer your subsystems cleanly by defining entry points for each layer.
- **When not to use**:
    * Clients require direct access to low-level, fine-grained subsystem operations that the facade obscures.
    * The facade becomes an antipattern "God Object" aggregating unrelated subsystem responsibilities.

### 11. Flyweight
- **How it works**: Uses sharing to support large numbers of fine-grained objects efficiently. It splits object state into intrinsic state (shared and immutable, stored in the object) and extrinsic state (context-dependent, passed in by clients).
- **When to use**:
    * An application uses an enormous quantity of fine-grained objects.
    * Storage costs are prohibitive due to the object volume.
    * Most object state can be factored out and made extrinsic.
- **When not to use**:
    * Object count is moderate and memory consumption is not a system bottleneck.
    * The computational overhead of calculating and passing extrinsic state exceeds the storage savings.

### 12. Proxy
- **How it works**: Provides a surrogate or placeholder for another object to control access to it. The proxy implements the identical interface as the real subject, intercepting invocations to add mediation logic before or after forwarding.
- **When to use**:
    * **Remote Proxy**: Representing an object that exists in a distinct address space.
    * **Virtual Proxy**: Delaying instantiation of expensive objects until strictly necessary (lazy loading).
    * **Protection Proxy**: Controlling access permissions based on caller authorization.
    * **Smart Reference**: Performing housekeeping like reference counting, locking, or caching on access.
- **When not to use**:
    * Access to the real subject requires direct, low-latency execution without indirection overhead.
    * The additional indirection layer adds complexity without providing caching, security, or distribution benefits.

---

## Behavioral Patterns

### 13. Chain of Responsibility
- **How it works**: Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Receivers are chained sequentially; each handler processes the request or passes it down the chain.
- **When to use**:
    * More than one object may handle a request, and the specific handler is not known a priori.
    * You want to issue a request to one of several objects without specifying the receiver explicitly.
    * The set of candidate handlers should be configured dynamically at runtime.
- **When not to use**:
    * Every request must be guaranteed to be handled; unhandled requests can fall off the chain.
    * The call graph is simple and the single handling receiver is known ahead of time.

### 14. Command
- **How it works**: Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations. The command decouples the invoker from the target receiver.
- **When to use**:
    * You want to parameterize objects with an action to perform (callback replacement).
    * You want to specify, queue, schedule, or execute requests at different times.
    * You must support undo, redo, or transactional rollback capabilities.
    * You need to log changes to reconstruct system state after a crash.
- **When not to use**:
    * Requests are straightforward, synchronous function calls that do not require queuing, logging, or reversal.
    * Introducing a distinct class for every single action produces unnecessary class proliferation.

### 15. Interpreter
- **How it works**: Given a language, defines a representation for its grammar along with an interpreter that uses the representation to interpret sentences. The grammar rules are modeled as abstract syntax tree classes with interpret methods.
- **When to use**:
    * The grammar of the domain-specific language is simple and stable.
    * Efficiency is not a critical concern.
- **When not to use**:
    * The grammar contains complex rules; class hierarchies for complex grammars become unmanageable (use parser generators like ANTLR).
    * High-throughput parsing performance is required.

### 16. Iterator
- **How it works**: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. The iterator maintains traversal state while the aggregate focuses solely on storage.
- **When to use**:
    * To access an aggregate object contents without exposing its internal representation.
    * To support multiple active traversals over the same aggregate simultaneously.
    * To provide a uniform polymorphic interface for traversing distinct data structures.
- **When not to use**:
    * The underlying structure is a simple array and standard index iteration is sufficient.
    * Extra object allocations and pointer indirections compromise high-performance memory loops.

### 17. Mediator
- **How it works**: Defines an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, centralizing interaction logic inside the mediator.
- **When to use**:
    * A set of objects communicate in well-defined but complex, unstructured ways with high interdependencies.
    * Reusing an object is difficult because it couples to many other collaborator objects.
    * A behavior distributed across several classes should be customizable without excessive subclassing.
- **When not to use**:
    * Colleagues have simple, unidirectional interactions that do not form complex webs.
    * The mediator absorbs too much domain logic and devolves into an unmaintainable monolith.

### 18. Memento
- **How it works**: Without violating encapsulation, captures and externalizes an object internal state so that the object can be restored to this state later. The originator creates and consumes mementos, while the caretaker stores them opaquely.
- **When to use**:
    * A snapshot of an object state must be saved to allow subsequent restoration.
    * Direct access to the internal state would expose private implementation details and break encapsulation.
- **When not to use**:
    * Originator state is large and saving frequent snapshots causes severe memory footprint or CPU overhead.
    * Changes can be tracked via simple undo commands without full state dumps.

### 19. Observer
- **How it works**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. The subject maintains an observer list and broadcasts events.
- **When to use**:
    * An abstraction has two aspects, one dependent on the other, and separating them enables independent variation and reuse.
    * A change to one object requires changing an unknown number of other objects.
    * An object must notify other objects without making assumptions about their concrete types.
- **When not to use**:
    * Updates occur at high velocity, risking cascade storms or unexpected cyclic update loops.
    * Observers require fine-grained update context, but simple broadcast models force costly full-state re-fetches.

### 20. State
- **How it works**: Allows an object to alter its behavior when its internal state changes. The object will appear to change its class by delegating state-dependent execution to an interchangeable concrete state object.
- **When to use**:
    * An object behavior depends on its state, and it must change its behavior dynamically at runtime based on that state.
    * Operations contain large, multipart conditional branches (`if/else` or `switch`) dependent on object state.
- **When not to use**:
    * The state machine has few states and transitions that rarely change; simple conditionals are clearer.
    * State transitions do not modify actual behavioral logic.

### 21. Strategy
- **How it works**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently of clients that use it by delegating algorithmic execution to a strategy interface.
- **When to use**:
    * Many related classes differ only in their execution behavior.
    * You need different variants of an algorithm (e.g., space-time trade-offs).
    * An algorithm uses private data that clients should not access.
    * A class defines multiple behaviors that appear as large conditional branches in its methods.
- **When not to use**:
    * The algorithm never changes and there is only a single implementation.
    * Clients cannot make informed decisions about which strategy to select.

### 22. Template Method
- **How it works**: Defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the overall algorithmic structure.
- **When to use**:
    * To implement invariant parts of an algorithm once and defer variable behavior to subclasses.
    * To factor out common behavior across subclasses and eliminate code duplication.
    * To control subclass extension points using explicit hook methods.
- **When not to use**:
    * Subclasses need to alter the sequencing or structural flow of the algorithm.
    * Composition is preferred over inheritance to avoid tight base-class coupling.

### 23. Visitor
- **How it works**: Represents an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates, using double dispatch.
- **When to use**:
    * An object structure contains many classes with differing interfaces, and operations depend on their concrete types.
    * Many distinct, unrelated operations must be performed on the structure, and you want to avoid polluting element classes.
    * The element classes rarely change, but new operations are frequently added.
- **When not to use**:
    * The element class hierarchy changes frequently; adding an element forces signature changes across the entire visitor hierarchy.
    * Elements cannot expose sufficient internal state to visitors without violating encapsulation.
