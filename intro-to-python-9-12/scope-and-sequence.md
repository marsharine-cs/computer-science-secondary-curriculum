# Introduction to Python — Scope and Sequence

**Grades 9–12** · 36 lessons · One semester

Prepared by Marsharine A. Simpson — State Computer Science credentials, Florida and New Jersey

---

## Course description

A first course in text-based programming for high school students with no prior coding experience. Students progress from single-line output to designing multi-function programs that process real datasets. The course prioritizes working code over vocabulary: every unit ends with students having built something that runs.

The sequence assumes no installed software. All work is browser-based, which keeps the course viable on managed Chromebooks and in districts where installations require IT approval.

**Every code example and error message in this curriculum was produced by execution on Python 3.12** before inclusion. Interpreter output is captured from real runs.

---

## Prerequisites and technical requirements

**Student prerequisites:** None. Basic keyboard familiarity and file navigation. Algebra I concurrent or complete is helpful but not required.

**Teacher prerequisites:** No prior Python experience required. Each lesson includes a worked solution, expected output, and the errors students commonly produce with real interpreter messages.

**Technology:** Any device with a modern browser and a browser-based Python environment such as Replit, Google Colab, or Trinket. No local installation. An offline alternative is provided for restricted-internet districts.

---

## Course structure

| Unit | Title | Lessons | Weeks |
|---|---|---|---|
| 1 | Getting Started with Python | 5 | 2 |
| 2 | Variables and Data | 6 | 2.5 |
| 3 | Making Decisions | 6 | 2.5 |
| 4 | Repetition and Loops | 6 | 2.5 |
| 5 | Functions and Decomposition | 6 | 2.5 |
| 6 | Lists and Working with Data | 5 | 2 |
| 7 | Capstone Project | 2 | 2 |
| | **Total** | **36** | **16** |

---

## Unit 1 — Getting Started with Python

**Essential question:** What does it mean to give a machine unambiguous instructions?

| # | Lesson | Students will be able to |
|---|---|---|
| 1.1 | Programs, Precision, and Ambiguity | Explain why computers require unambiguous instructions and identify ambiguity in written procedures |
| 1.2 | Your First Program | Write and run a program producing formatted output using `print()` |
| 1.3 | Reading Errors as Information | Interpret a traceback, locate the fault, and correct it |
| 1.4 | Documentation and Readable Code | Write comments that explain intent and justify design decisions |
| 1.5 | Unit 1 Checkpoint | Produce a documented multi-line program that runs without error |

**Unit deliverable:** A documented program producing formatted output.

**Teaching note:** Lesson 1.3 is deliberately early. Most beginners quit at their first traceback because nobody taught them to read one. Framing errors as information rather than failure changes retention across the entire course.

**Grades 6–8 adaptation:** The Lesson 1.1 warm-up becomes a physical demonstration rather than analysis of a written procedure. Extend the unit to seven lessons and add a session on environment navigation.

---

## Unit 2 — Variables and Data

**Essential question:** How does a program store, transform, and report information?

| # | Lesson | Students will be able to |
|---|---|---|
| 2.1 | Variables and Assignment | Create clearly named variables and trace how assignment changes their value |
| 2.2 | Strings and Text Manipulation | Build and modify strings using concatenation, indexing, and f-strings |
| 2.3 | Numeric Types and Operators | Evaluate arithmetic expressions including integer division and modulo |
| 2.4 | Input and Program Interaction | Use `input()` to build programs that respond to a user |
| 2.5 | Type Conversion and Type Errors | Convert between types and diagnose the errors that result when they don't |
| 2.6 | Unit 2 Checkpoint | Build a program that accepts input, computes a result, and reports it clearly |

**Unit deliverable:** A calculation tool — unit converter, GPA calculator, or budget estimator.

**Teaching note:** Lesson 2.5 addresses the most common beginner bug in Python. `input()` returns a string, so arithmetic on it fails. Front-loading it prevents weeks of confusion.

**Grades 6–8 adaptation:** Omit modulo and integer division; reintroduce them in the loops unit where they have concrete use.

---

## Unit 3 — Making Decisions

**Essential question:** How does a program choose between paths?

| # | Lesson | Students will be able to |
|---|---|---|
| 3.1 | Boolean Logic and Comparison | Evaluate comparison and boolean expressions and predict their results |
| 3.2 | Conditional Execution with `if` | Write programs that execute code selectively |
| 3.3 | `else`, `elif`, and Exhaustive Branching | Handle multiple mutually exclusive conditions completely |
| 3.4 | Compound Conditions | Combine conditions with `and`, `or`, and `not` |
| 3.5 | Nested Conditionals and When to Refactor | Structure nested decisions and recognize when nesting should be flattened |
| 3.6 | Unit 3 Checkpoint + Pseudocode Bridge | Build a branching program and translate it into AP CSP pseudocode |

**Unit deliverable:** A decision-logic program — eligibility checker, grading tool, or classification system.

**Teaching note:** Lesson 3.6 introduces the pseudocode bridge that continues through the rest of the course. Students write Python first, then express the same logic in College Board notation.

**Grades 6–8 adaptation:** Drop the pseudocode bridge; extend 3.6 into a two-session project.

---

## Unit 4 — Repetition and Loops

**Essential question:** How do we express repeated work without repeating ourselves?

| # | Lesson | Students will be able to |
|---|---|---|
| 4.1 | Recognizing Repetition | Identify repeated code and explain why repetition is a design problem |
| 4.2 | `for` Loops and `range()` | Write definite loops that repeat a known number of times |
| 4.3 | `while` Loops and Conditions | Write indefinite loops that repeat until a condition changes |
| 4.4 | Infinite Loops and Termination | Diagnose non-terminating loops and reason about termination conditions |
| 4.5 | Loops with Conditionals | Combine iteration and selection to filter, count, and accumulate |
| 4.6 | Unit 4 Checkpoint + Pseudocode Bridge | Select the appropriate loop type, justify the choice, and translate to pseudocode |

**Unit deliverable:** An interactive program using both loop types — simulation, game, or menu system.

**Teaching note:** Lesson 4.6 requires students to justify their loop choice, not just make one. Justification is the habit that supports algorithm comparison later.

**Grades 6–8 adaptation:** Split 4.5 across two sessions. Accumulator patterns take longer to land at this age.

---

## Unit 5 — Functions and Decomposition

**Essential question:** How do we decompose a large problem into solvable parts?

| # | Lesson | Students will be able to |
|---|---|---|
| 5.1 | Defining and Calling Functions | Write a function and call it from elsewhere in a program |
| 5.2 | Parameters and Arguments | Pass values into functions to make them general rather than specific |
| 5.3 | Return Values and Composition | Return results and use them within larger expressions |
| 5.4 | Scope and Variable Lifetime | Predict which variables are accessible where, and explain why |
| 5.5 | Decomposition Before Code | Break a multi-step problem into functions during planning, not after |
| 5.6 | Unit 5 Checkpoint | Refactor an earlier program into documented functions |

**Unit deliverable:** A refactored version of a Unit 3 or 4 program, reorganized into functions with documentation.

**Teaching note:** Lesson 5.6 uses students' own prior code. Refactoring something they wrote makes the value of decomposition concrete in a way a fresh problem cannot.

**Grades 6–8 adaptation:** Omit scope entirely. Return to it only if students hit scope errors organically.

---

## Unit 6 — Lists and Working with Data

**Essential question:** How do programs manage collections of information?

| # | Lesson | Students will be able to |
|---|---|---|
| 6.1 | Lists and Indexing | Create lists and access elements by index, including negative indexing |
| 6.2 | Modifying and Building Lists | Add, remove, and update list elements |
| 6.3 | Iterating Over Collections | Loop through lists to process every element |
| 6.4 | Searching, Filtering, and Aggregating | Find matching elements, build filtered lists, and compute summary values |
| 6.5 | Unit 6 Checkpoint + Pseudocode Bridge | Build a data-processing program and translate list operations to pseudocode |

**Unit deliverable:** A data analysis program operating on a real dataset — class grades, sports statistics, or survey results.

**Teaching note:** Use a genuine dataset rather than invented numbers. Real data produces messier, more instructive results.

**Grades 6–8 adaptation:** Limit to 6.1–6.3. Filtering and aggregation belong in a follow-on course.

---

## Unit 7 — Capstone Project

**Essential question:** Can I design and build a program that solves a problem I selected?

| # | Lesson | Focus |
|---|---|---|
| 7.1 | Planning, Decomposition, and Proposal | Students scope a project, decompose it into functions, and submit a plan for approval |
| 7.2 | Build, Test, Document, Present | Students implement, test against cases, document design decisions, and demonstrate |

**Deliverable:** An original working program with written documentation and a short presentation of design decisions.

**Suggested duration:** Two weeks of class time with structured checkpoints, not two sessions.

---

## Assessment plan

| Type | Frequency | Purpose |
|---|---|---|
| Exit tickets | Every lesson | Formative check, 3–5 minutes |
| Unit checkpoints | End of each unit | Applied performance task, not vocabulary recall |
| Pseudocode bridges | Units 3, 4, 6 | AP notation fluency |
| Code reviews | Units 3, 5, 7 | Students read and critique working code |
| Capstone | End of course | Summative, scored across planning, function, and documentation |

Assessment weights working programs over syntax recall. Students may reference documentation during checkpoints, which reflects professional practice.

---

## Differentiation

**Students working ahead:** Each checkpoint includes an extension requiring the unit's concept applied to an unfamiliar problem. Advanced students may serve as debugging partners, which reinforces their own understanding.

**Students needing support:** Each lesson includes a scaffolded version with partial code supplied, plus a reduced checkpoint assessing the same objective at lower complexity.

**English language learners:** Vocabulary introduced with visual models before symbolic notation. Worked-example comments written in plain sentences.

**Students with prior experience:** Redirect toward code quality, documentation, and helping peers rather than racing ahead in content.

---

## Pacing alternatives

| Format | Adaptation |
|---|---|
| Full year (72 sessions) | Expand each lesson across two sessions; add a second capstone |
| Quarter (18 sessions) | Units 1–5 only; capstone replaced by the Unit 5 checkpoint |
| Pre-AP CSP | As written; follow with the remaining Big Ideas and the Create Performance Task |
| After-school or club | Units 1–4 plus a project; 12 sessions |
| Grades 6–8 | Apply the adaptation notes above; extends to roughly 44 lessons |

---

## Standards

Designed with reference to the CSTA K–12 Computer Science Standards, Level 3A, and the AP® Computer Science Principles framework, Big Ideas 1 and 3. Framework identifiers are listed per lesson in the full curriculum so a district can run its own crosswalk.

This is not a complete AP Computer Science Principles course. See [NOTICES_AND_ATTRIBUTION.md](../NOTICES_AND_ATTRIBUTION.md) for full attribution, trademark, and non-endorsement statements.

---

*Portfolio sample. See [LICENSE](../LICENSE) for terms of use.*

© 2026 Marsharine A. Simpson
