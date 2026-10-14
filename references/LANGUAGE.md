# Language

## Required Rules
1. Always use ASD-STE100 Simplified Technical English (STE) for text that you write or change.
    * Apply this rule to user replies, progress reports, plans, questions, and tool descriptions.
    * Apply it to documents, READMEs, comments, docstrings, logs, errors, warnings, and interface text.
    * Apply it to commit messages, pull requests, issues, and review notes.
2. Before you write, read [ASD_STE100.md](../assets/ASD_STE100.md). Use the official rules and dictionary linked there.
3. Keep replies extremely short, simple, precise, and direct.
    * Keep the meaning and the information that the user needs.
    * Give more detail only when the request or the task requires it.
4. Answer directly. Avoid formalities, slang, idioms, and unnecessary words.
5. Use US English unless the user specifies another language or spelling system.
    * Keep the other STE rules for English text. STE does not define rules for other languages.
6. Keep exact quotations, official titles, commands, paths, identifiers, and required data unchanged.
    * Apply STE to the text around these items. Do not change program behavior to change prose.
7. Preserve the author's meaning and style where they agree with STE.
    * If a style choice conflicts with STE, obey STE.
    * Apply this rule to the requested edits. Do not rewrite unrelated content.
8. Review every reply and changed text before you send or save it.
    * Check vocabulary, grammar, sentence length, technical terms, and meaning.
    * Correct each violation. Do not treat clear prose alone as proof of STE compliance.
    * If you cannot verify a word, check the official dictionary. Do not invent an approved meaning.
    * If full verification is not possible, state that limit. Do not claim verified STE compliance.

## Comments
* Write code that explains itself. Keep comments extremely short.
* Add comments for files, classes, functions, and methods.
* Add a comment before complex code. Explain why the code is necessary.
* Explain what the code does only when the operation is complex.
* For complex functions, libraries, or features, add a documentation reference. Example: `Ref: http://...`.
* Keep framework-specific comment requirements. Use STE for their text.

## README Text
* Keep the README short, precise, formal, and simple.
* Explain what the project does, how it is built, and how to use it.
* Put other information in internal documents. Create those documents only when the user requests them.
* For content and section order, read [README_GUIDE.md](./README_GUIDE.md).

## Messages
* Use STE for log messages and exception messages. Keep their required technical details.
* Make each log message clear without other messages. Name the operation, object, source, and relevant properties.
    * Avoid messages such as `Added #n row to DB`.
    * Give enough context, as in `Added #n rows to the DB Table XYZ from the set ABC with property P`.
* Use STE for the description after a semantic commit prefix. Keep the required prefix syntax.
