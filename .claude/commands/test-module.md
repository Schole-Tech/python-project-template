Run tests for a specific module.

Usage: /test-module <module_path>

Example: /test-module src/myproject/core.py

Steps:
1. Identify the test file that corresponds to the given module path
2. Run: uv run pytest <test_file_path> -v
3. If tests fail, analyze the output and suggest fixes
4. If no test file exists, create one following the project test patterns
