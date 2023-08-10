#!/usr/bin/python3
import importlib.util

def print_names():
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    names = [name for name in dir(module) if not name.startswith("__")]
    
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_names()
