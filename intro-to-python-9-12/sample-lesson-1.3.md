# Lesson 1.3 — Reading Errors as Information

**Introduction to Python** · Unit 1: Getting Started · Grades 9–12 · One 50-minute session

*This is a full instructional portfolio sample based on Lesson 1.3 from the course.*

---

## Why this lesson exists

Early error messages can become a major source of frustration for beginning programmers when they have not yet learned how to read them. This lesson introduces traceback reading as a structured debugging skill rather than a signal to start changing code at random.

It is placed early in the course so students establish a read-before-fix routine before later programming tasks become more complex.

---

## Learning objectives

Students will be able to:

1. Locate the line number and position of an error from a traceback
2. Distinguish a syntax error from a runtime error
3. Correct at least four common Python error types
4. Describe an error in their own words before attempting a fix

---

## Vocabulary

| Term | Definition |
|---|---|
| Traceback | The report Python produces when a program fails |
| Syntax error | Code that breaks Python's writing rules; nothing runs |
| Runtime error | Valid code that fails while executing |
| Debug | To find and correct a fault in a program |

---

## Procedure

### Warm-up — 6 minutes

Project this traceback with no code visible:

```text
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print("I am " + age)
          ~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```

Ask three questions and take answers before explaining anything:

- Which line failed?
- What was Python trying to do?
- What is it complaining about?

Students can answer all three without knowing what a TypeError is. That is the point of the lesson: **the message contains useful diagnostic information.**

### Direct instruction — 10 minutes

Every traceback tells you four things: which file, which line, what code was running, and what went wrong.

Read it **bottom-up**. The last line names the error type and describes it. Everything above is the path Python took to get there.

**Syntax errors** mean the code breaks Python's writing rules. Nothing runs at all — Python reports these before executing a single line.

**Runtime errors** mean the code is written legally but fails while running. Some of the program may have executed already.

Emphasize: an error message is not a punishment. It is one of the most specific sources of diagnostic information available while debugging. Professional developers read tracebacks routinely.

### Modeling — 12 minutes

Work through each of these live. For every one, read the message aloud, ask the class what it means, *then* fix it.

**NameError — undefined variable**

```python
print(student_name)
```

```text
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(student_name)
          ^^^^^^^^^^^^
NameError: name 'student_name' is not defined
```

Runtime error. Python ran, reached the name, and had nothing stored under it.

**NameError — capitalization**

```python
Print("Hello")
```

```text
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    Print("Hello")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

Same error type, different cause. Python even suggests the fix — a good moment to point out that reading the *whole* message pays.

**TypeError — mixing types**

```python
age = 16
print("I am " + age)
```

```text
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print("I am " + age)
          ~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```

Note the squiggles under the whole expression and the caret at the operator. Python is showing where the incompatibility occurs. Preview only — Unit 2 handles the fix.

**IndentationError**

```python
print("first")
    print("second")
```

```text
  File "main.py", line 2
    print("second")
IndentationError: unexpected indent
```

Syntax error. No traceback header, because nothing ran. Whitespace is structural in Python.

**SyntaxError — unterminated string**

```python
print("Hello)
```

```text
  File "main.py", line 1
    print("Hello)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

The caret marks where Python lost the thread.

Draw the pattern out explicitly: **syntax errors show a file and line but no "Traceback" header. Runtime errors show the traceback.** This distinction gives students a quick way to categorize many beginner errors.

### Guided practice — 15 minutes

**Debugging gauntlet.** Distribute five broken programs. For each, students write down three things before touching the code:

1. Line number of the fault
2. Error type
3. What the message means, in their own words

Only then do they fix it.

Enforce the order. Students who fix first and read second may solve a simple error without learning the diagnostic process; later programs require a more systematic debugging routine.

### Closing — 5 minutes

Exit ticket. Collect before students leave.

---

## Debugging gauntlet

**Program 1**
```python
print("Welcome to class")
print("Today is Monday"
print("Let's begin")
```

**Program 2**
```python
print("The answer is")
Print(42)
```

**Program 3**
```python
print("Line one")
   print("Line two")
```

**Program 4**
```python
print("Total: " + 100)
```

**Program 5**
```python
print('Mismatched quotes")
```

---

## Gauntlet answer key

**1.** Line 2. `SyntaxError: '(' was never closed`. Missing closing parenthesis.

*Note: Python reports line 2 even though a student may expect line 3 — the parser keeps looking for the close and gives up at the next statement. Worth discussing. The reported line is where Python noticed, not always where the original mistake occurred.*

**2.** Line 2. `NameError: name 'Print' is not defined`. Capital P. Runtime error — line 1 prints before it fails.

**3.** Line 2. `IndentationError: unexpected indent`. Leading spaces. Syntax error — nothing prints.

**4.** Line 1. `TypeError: can only concatenate str (not "int") to str`. Accept `print("Total:", 100)` as a fix.

**5.** Line 1. `SyntaxError: unterminated string literal`. Opens single, closes double.

---

## Student handout

### Reading the Message

**Part 1 — Traceback anatomy**

For this traceback, identify each part:

```text
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print(total_score)
          ^^^^^^^^^^^
NameError: name 'total_score' is not defined
```

File: _______  Line number: _______  Code that failed: _______

Error type: _______  What it means, in your words: _______

**Part 2 — Predict the error**

Without running these, write which error type each will produce and why:

```python
print("Hello"
```

```python
print(Hello)
```

```python
  print("Hello")
```

**Part 3 — Break it on purpose**

Write a program that produces a `NameError`. Then write one producing a `SyntaxError`. Explain the difference between what happens when each runs.

---

## Exit ticket

1. Where in a traceback do you find the most useful information — top or bottom? Why?
2. What is the difference between a syntax error and a runtime error?
3. This appears: `NameError: name 'total' is not defined`. Give one likely cause.
4. Your program shows no error but prints the wrong number. Is this a syntax error, a runtime error, or neither?

---

## Exit ticket answer key

**1.** Bottom. The final line names the error type and describes it; the lines above trace the path.

**2.** Syntax errors break Python's writing rules and prevent the program from running at all. Runtime errors occur in legally written code while it executes.

**3.** Variable never assigned, a typo in the name, or a capitalization mismatch. Any one is full credit.

**4.** Neither — it is a logic error. Accept any answer conveying that the program works but produces the wrong result. This connects directly to Lesson 1.1. Students who say "runtime error" need that distinction revisited.

---

## Differentiation

**Support:** Reduce the gauntlet to three programs. Supply the error type and have students locate only the line and the fix.

**Extension:** Have students write a broken program for a partner to debug, then compare how quickly the partner found it. Introduce `ZeroDivisionError` and `IndexError` as preview.

**English language learners:** Provide a reference card translating error type names into plain language. Technical vocabulary may be the primary barrier for some students even when the underlying debugging concept is accessible.

**Prior experience:** Ask them to explain why Python reports line 2 in Program 1 rather than line 3. That parser behavior gives experienced students a deeper question without moving ahead to unrelated content.

---

## Teacher notes

**This lesson establishes a foundational debugging routine for the course.** Early tracebacks can become a significant point of frustration when students have not yet learned how to interpret them. Placing this lesson third gives students a structured read-before-fix process before programs become more complex.

**Enforce read-before-fix.** The instinct is often to change something and re-run without interpreting the message. That can produce accidental fixes without building a transferable debugging process. The habit developed here is to read, describe, then revise.

**Use consistent language:** "The error message is useful information." Repeating that idea when students ask for help can make it part of the class debugging routine.

**Program 1's line number surprise is worth the detour** if the class is engaged. It teaches that the reported line is where Python noticed, not always where the original mistake occurred.

---

## Grades 6–8 adaptation

Cut TypeError entirely — it depends on type concepts from Unit 2 and can add unnecessary cognitive load at this point for younger learners. Reduce the gauntlet to three programs. Extend across two sessions, using the second for partner debugging.

---

## A note on the error messages in this lesson

Every traceback shown here was produced by running the code on **Python 3.12** — including caret positions, squiggle underlines, and Python's own "Did you mean" suggestions. None of it was written from memory or approximated.

Python error messages change between versions. If a classroom environment reports something slightly different, that is expected, and it is worth showing students.

---

### Standards versioning note

The course was originally developed with references to the CSTA K–12 Computer Science Standards, Revised 2017. CSTA published revised PK–12 standards in 2026, and the course's lesson-level CSTA references are being remapped as part of quality assurance. See [NOTICES_AND_ATTRIBUTION.md](../NOTICES_AND_ATTRIBUTION.md) for details.

---

*Portfolio sample. See [LICENSE](../LICENSE) for terms of use and [NOTICES_AND_ATTRIBUTION.md](../NOTICES_AND_ATTRIBUTION.md) for standards attribution.*

© 2026 Marsharine A. Simpson
