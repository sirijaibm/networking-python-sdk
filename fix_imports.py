#!/usr/bin/env python3
import os
import re

test_dir = 'test/unit'
files = [f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.py')]

fixed_count = 0
for filename in files:
    filepath = os.path.join(test_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if pytest is imported inside except block
    if 'except ImportError:\n    import pytest' in content:
        # Split content to find the docstring and imports
        lines = content.split('\n')
        new_lines = []
        in_try_block = False
        try_block_start = -1
        
        for i, line in enumerate(lines):
            if line.strip() == 'try:' and not in_try_block:
                # Found the try block, insert pytest import before it
                new_lines.append('')
                new_lines.append('import pytest')
                new_lines.append('')
                new_lines.append(line)
                in_try_block = True
                try_block_start = i
            elif in_try_block and line.strip().startswith('except ImportError:'):
                # In except block, skip the "import pytest" line
                new_lines.append(line)
                # Skip next lines until we find the pytest.skip line
                j = i + 1
                while j < len(lines):
                    if 'import pytest' in lines[j]:
                        # Skip this line
                        j += 1
                        continue
                    elif 'pytest.skip' in lines[j]:
                        new_lines.append(lines[j])
                        j += 1
                        break
                    else:
                        new_lines.append(lines[j])
                        j += 1
                # Continue from where we left off
                for k in range(j, len(lines)):
                    if k == j and lines[k].strip() == '':
                        # Skip empty line after except block
                        continue
                    # Check if this is the duplicate pytest import after except
                    if 'import pytest' in lines[k] and k > try_block_start + 5:
                        # Skip duplicate pytest import
                        continue
                    new_lines.append(lines[k])
                break
            else:
                new_lines.append(line)
        
        new_content = '\n'.join(new_lines)
        
        if new_content != content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Fixed: {filename}")
            fixed_count += 1
        else:
            print(f"No change: {filename}")
    else:
        print(f"Already correct: {filename}")

print(f"\nFixed {fixed_count} out of {len(files)} files")
