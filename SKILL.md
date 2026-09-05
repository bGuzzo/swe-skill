---
name: swe-skill
description: SWE skill to enforce strict code style, quality, and patterns across all sessions. It dictates every aspect of SWE and code writing tasks. The guidelines of this skill can be used with all languages, although currently only Python has a strong specification.

compatibility: All agentic tools; it is meant to be compatible with all harnesses.

license: GNU Affero GPL v3 (2007)

metadata: 
    author: brunoguzzo18@#gmail.com
    version: "0.1-alpha"
---

# SWE Skill
Your role is to write high-quality, simple, reliable, and efficient code like an experienced software engineer. 

### Core Principles 
1. The software should be like a Toyota: reliable, never breaks, and even if it breaks, it should be possible to keep going. 
    * Enforce strict fault tolerance and fallback/recovery logic to recover from an erroneous state. 
    * Example: Apollo AGC computer recovery capability for the moon landing.

2. All imports should be enforced at the beginning of the file; never use mid-file imports. Same for constants;

4. Never use plain strings inside a code file; always declare values at the top of the file after the imports;

5. Always declare the type of the variable or method you are operating on, as done in languages like Java or C.
    * If the language is not strictly typed (like Python), always state the data types;
    * It is better to accept verbosity to let the user understand what data type he is manipulating;

6. Prefer OOP (like Java). Usage of functional programming (like Python) is allowed when a file or a method/function is stateless and does not need to access state to perform its task;
    * Even when not using OOP, files should be arranged according to a single purpose, like what happens with a single file containing a sole Java class;

7. Avoid huge files at all costs, roughly 500 lines maximum. Prefer a Java-like file structure where each file owns a small set of responsibilities. If a file grows bigger, split it.

8. Package Style & Code Architecture: Prefer a Spring Boot-like packaging structure; TODO: add details and references;

9. Loose Coupling:

10. Layering:

11. Logging:

12. Edge Cases:

13. Defensive Programming:

14. Function structures:

15. Low cognitive load:

16. Exception handling:

17. Comment style:

18. Design patterns: 

19. Agent behavior and guidelines:

20. Testing: 

21. Commit messages and orchestration: 










