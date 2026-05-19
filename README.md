# Dictionary-Based Database Management System
**Language:** Python &nbsp;|&nbsp; **Author:** Esiri Angel Ediri  
**University:** Prairie View A&M University

---

## Overview
A command-line database system built entirely on Python's built-in dictionary data structure. Supports full CRUD operations with input validation, sorted display, and recursive retry on failed lookups.

---

## Features

| Feature | Description |
|---------|-------------|
| Add | Insert a key-value record; prompts to overwrite if key exists |
| View | Display all records sorted by key **or** value, with total count |
| Search | Look up any record by key with match/no-match feedback |
| Update | Change the value of an existing record |
| Delete | Remove a record by key; offers retry if key not found |
| Validation | Rejects empty keys, invalid menu choices, and handles edge cases |

---

## How to Run

**Terminal:**
```bash
python dict_dbms.py
```

**Jupyter / Google Colab:**
```python
# Paste the full script into a cell and run — or import it:
%run dict_dbms.py
```

---

## Sample Session

```
============================================
  DATABASE MANAGEMENT SYSTEM
============================================
  1.  Add record
  2.  View all records
  3.  Search by key
  4.  Update / Delete record
  0.  Exit
--------------------------------------------
  Select option: 1
  Enter key   : student_id
  Enter value : 001
  [✓] Record added  →  'student_id' : '001'
```

---

## Concepts Demonstrated
- Python dictionary CRUD operations
- Input validation and duplicate key handling
- `sorted()` with `lambda` key functions
- Modular function design
- Recursive retry pattern
- Type hints (`dict`, `str`, `None`)
