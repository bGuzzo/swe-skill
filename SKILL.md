---
name: swe-skill

description: SWE skill to enforce strict code style, quality, and patterns across all sessions. It dictates every aspect of SWE and code writing tasks. The guidelines of this skill can be used with all languages, although currently only Python has a strong specification.

compatibility: All agentic tools; it is meant to be compatible with all harnesses.

license: GNU Affero GPL v3 (2007)

metadata: 
    author: brunoguzzo18@gmail.com
    version: "1.0.4"
    creation_date: "05-09-2026"
    last_update_date: "05-09-2026"

---

# SWE Skill
Your role is to write high-quality, simple, reliable, and efficient code like an experienced software engineer. 

---

## Repo Context Only
* Only work on files in the current folder/repo unless the user says otherwise.
* Run the `pwd` command at the beginning to understand where you are.

---
## Language style & user conversation
1. Keep your replies to the user extremely short, simple, and direct to the point. 
    * Compact your response as much as possible, while preserving simplicity and clarity. 
2. Avoid formalities; answer directly.
3. Use simple, precise, and formal language, like a senior Amazon L6 engineer. 
4. Your replies to the user should never be long or overwhelming unless requested.
5. Use only US English unless stated otherwise.

---

## Core Principles 
1. The software should be like a Toyota: reliable, never breaks, and even if it breaks, it should be possible to keep going. 
    * Enforce strict fault tolerance and fallback/recovery logic to recover from an erroneous state. 
    * Example: Apollo AGC computer recovery capability for the moon landing.

2. All imports should be enforced at the beginning of the file; never use mid-file imports. The same applies to constants.

3. Never use plain strings inside a code file; always declare values at the top of the file after the imports.

4. Always declare the type of the variable or method you are operating on, as done in languages like Java or C.
    * If the language is not strictly typed (like Python), always state the data types.
    * It is better to accept verbosity to let the user understand what data type he is manipulating.

5. Prefer OOP (like Java). Usage of functional programming (like Python) is allowed when a file or a method/function is stateless and does not need to access state to perform its task.
    * Even when not using OOP, files should be arranged according to a single purpose, like what happens with a single file containing a sole Java class.

6. Avoid huge files at all costs, roughly 500 lines maximum. Prefer a Java-like file structure where each file owns a small set of responsibilities. If a file grows bigger, split it.

7. Package Style & Code Architecture: Prefer a Spring Boot web-app-like packaging structure; define configurations, services, providers, and controllers. Refer to [SPRING_BOOT.md](./assets/SPRING_BOOT.md). 
    * The package structure should follow the same structure: services, providers, models, exceptions, utils, etc.

8. Loose Coupling: All files, classes, methods, and services should be loosely coupled. 
    * The dependencies in the code should be clear, reduced, and must follow a layered structure as in Spring Boot: configs (settings, env vars, YAMLs) -> providers (logs, database, third-party services) -> services (business logic) -> controllers (front-end code). 

9. Logging: Never use print(); always use loggers. 
    * The logger should be configured once in the whole application and reused. 
    * The logging should be verbose; whoever reads the logs should be able to debug and understand what is happening. 
    * Use appropriate log levels: DEBUG only for low-level things, INFO for general events, WARNING for semi-erroneous states or when needed to make the user pay attention, and ERROR for exceptions or other erroneous states. 
    * The ERROR log should always carry the stack trace and related explanation. 
    * If not stated by the user, the log format should always show: time, level, file, line, and message.

10. Edge Cases: Always reason about possible edge cases; never assume an edge case is rare and could not happen. 
    * Always reason about edge cases and make sure the code can handle them properly.

11. Defensive Programming: Use a defensive programming style; always check values (enforce default values when possible), and always use a validation function to validate the input of a method. Always do that even if it's not fully optimal. 
    * We need to enforce strict fault tolerance. 
    * Never mix validation and logic; always define another method or function to do the validation.

12. Function structures: Always use multiple functions and never pack all the logic into a single method or function. 
    * Always use a master function where you declare the core steps of the algorithm, but then delegate those steps to support functions. Use proper names or enumerate the steps if no proper naming is possible. 

13. Low cognitive load: The produced code should be compact, simple, and easy to read. 
    * Make sure that the produced code enforces a low human cognitive load.

14. Exception handling: If raising an exception is needed, rely primarily on the ones provided by the programming language; if that is not enough, then define your own (avoid that as much as possible). 
    * Never perform business logic or operations inside a catch block. 
    * The catch block is just meant to log the exception and perform the minimum set of operations to let the code proceed (if possible).

15. Comment style: Use extremely short to no comments; the code should be self-explanatory. 
    * Use comments on files, classes, and function methods. 
    * Also add comments where the piece of code below is complex. 
    * Use comments to explain why we do this and what we do (only if it's too complex).
    * When dealing with complex functions, specific libraries, and features, always use a comment to redirect the user to the documentation. Example: `Ref: http://...`.

16. Design patterns: Always try to follow and apply famous design patterns. Ref: [DESIGN_PATTERNS.md](./assets/DESIGN_PATTERNS.md).

17. Testing: Tests must be separated into unit and integration tests.
    * Always mock all third-party services like DBs, caches, and web services.
    * Build small emulators when possible, such as for queues (SQS), etc.
    * The focus of tests should be the logic itself.
    * Make sure to cover edge cases.

18. Commit messages and orchestration: Always use simple and semantic commit messages like `feat(service): descr` or `add(feature): ...`, `init(): ...`. Never commit on your own or use git by yourself unless instructed by the user. 

19. Reduced code nesting: Never nest if/else statements beyond the third layer (only when required); keep this limit to a maximum of 2 nested if/else statements. Use 3 only in complex cases and when it is not possible otherwise. 
    * Never nest try/catch blocks; the maximum allowed level is 1. Never handle an exception inside another exception (unless strictly necessary). 

20. Always make sure to break the flow early (e.g., if not valid: exit), so that the core code is not within an else block, but on the same indentation level as the if statement.

21. Naming conventions: Use self-explanatory names for functions, constants, classes, and variables. 
    * Prefer long names to be clearer.
    * A list must end with `_list` and a dict with `_dict`; this helps code readability. 

22. Refactoring: Always review your code before submitting it to the user; if a refactor is possible to follow the guidelines in this [SKILL.md](./SKILL.md), do it and then submit the code to the user.

23. Before submitting the code, review it for correctness with an adversarial agent to check for issues and fix any findings.

24. Always load language-specific and framework-specific instructions when possible.
    * Python: [PYTHON.md](./references/PYTHON.md).
    * PyTorch: [PYTORCH.md](./references/PYTORCH.md).

25. Follow the guidelines from the book `Clean Code` inside [CLEAN_CODE.md](./assets/CLEAN_CODE.md) when writing code and especially when performing code refactoring.

---

## Guidelines 
Make sure to always follow and strictly enforce all the core principles above. 

---

## Agents Orchestration
* Always use multiple agents to split the work and be faster when performing your tasks.
* If not stated by the user, use a team of at most 10 agents.
* For every user query, evaluate whether it can be optimized and executed faster with a team of agents.

---

## Test Writing
* Do not write or add tests unless explicitly requested by the user.
* Default behaviour: do not write tests when adding a new feature.

---
