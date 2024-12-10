# gendia
A Python CLI to generate a tree structured diagram for any directory!

---
Imagine this: you are on Discord and is request help from someone about a project you are working on. You want to show the structure of your project directory to the person. You can't just send a screenshot of the directory because it's too big and the person won't be able to see the whole structure. You can't just send a text file with the structure because it's too boring and the person won't be able to understand it easily. What do you do? You use `gendia`!


Heres an example of a tree structured diagram generated by `gendia`:

```
project
├── src
│   ├── main.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── helper.py
│   │   └──  helper2.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_main.py
│   │   └──  test_helper.py
│   └── README.md
├── LICENSE
└── .gitignore
```

Not just that, it is color coded! The directories are in blue, and different file types are in different colors. This makes it easier to understand the structure of the directory.

## Installation
To add `gendia` to your project, run:
```bash
pip install gendia
```
This should install `gendia` to your project. You can now use it to generate tree structured diagrams for your directories.

## Usage
To use `gendia`, run:
```bash
gendia path/to/directory
```
This should generate a tree structured diagram for the directory you specified. You can also specify the output file by using the `-o` flag:
```bash
gendia path/to/directory -o output.txt
```
This should generate a tree structured diagram for the directory you specified and save it to `output.txt`.

`--nohidden` flag can be used to show hidden files and directories:
```bash
gendia path/to/directory --nohidden
```