# Python and Bash – Core Python Programming

**Name:** Vade Peer  
**Course:** DevOps Course  
**Topic:** Conditionals, Dictionaries, and File Handling

## Objective

Practise core Python programming using conditionals, dictionaries, and file handling for reading and writing text files.

## 1. Grade Checker

### Command
```bash
python3 grade_checker.py
```

### Tests documented in the assignment
- Score `90` → Grade `A`
- Score `50` → Grade `F`
- Score `99` → Grade `A`
- Score `81` → Grade `B`

### Explanation
The program uses `if/elif/else` to determine A, B, C, D, or F based on the entered score.

## 2. Student Grades

### Command
```bash
python3 student_grades.py
```

### Demonstrated operations
- Existing students are stored in a dictionary.
- A new student and grade are added.
- An existing student's grade is updated.
- An `if/else` check determines whether the student exists.
- All student grades are printed.

### Example documented result
- Alice: `92`
- Bob: `72`
- Charlie: `91`
- Vade: `80`

### Explanation
The program uses a dictionary, adds a new student and grade, checks for an existing student with if/else, updates a grade, and prints all grades.

## 3. Write to a File

### Command
```bash
python3 write_file.py
```

### Verification
```bash
ls -l student_notes.txt
cat student_notes.txt
```

### Explanation
The program opens a file in write mode, uses `write()` to add content, and closes the file.

## 4. Read from a File

### Command
```bash
python3 read_file.py
```

### Verification
```bash
cat student_notes.txt
```

### Explanation
The program opens the file in read mode, uses `file.read()` to obtain its contents, displays them, and closes the file.

## Screenshots

The Microsoft Word documentation submitted with the project contains the terminal screenshots and command/output evidence for the completed tasks.

## GitHub Repository

https://github.com/Vadepeer/Dev_ops_Assignment

## Source Files

- `grade_checker.py`
- `student_grades.py`
- `write_file.py`
- `read_file.py`
- `requirements.txt`

## Submission

The complete project folder should be compressed as `Python_and_Bash_VadePeer.zip` for portal submission. The ZIP should contain the source code and the Word documentation with mandatory screenshots.
