#!/usr/bin/env python3
"""
Script to fix all test files by removing nested try-except blocks.
"""

import re
from pathlib import Path

def fix_file(file_path):
    """Fix a single test file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the nested try-except blocks
    pattern = r'try:\ntry:\ntry:\n\s+from ibm_cloud_sdk_core\.authenticators\.no_auth_authenticator import NoAuthAuthenticator\nexcept ImportError:\n\s+import pytest\n\s+pytest\.skip\([^)]+\)\nexcept ImportError:\n\s+import pytest\n\s+pytest\.skip\([^)]+\)\nexcept ImportError:\n\s+import pytest\n\s+pytest\.skip\([^)]+\)\nimport inspect\nimport json\nimport os\nimport pytest\nimport re\nimport responses\nimport urllib\ntry:\ntry:\ntry:\n\s+from ibm_cloud_networking_services\.[a-z_]+ import \*\nexcept ImportError:\n\s+import pytest\n\s+pytest\.skip\([^)]+\)\nexcept ImportError:\n\s+import pytest\n\s+pytest\.skip\([^)]+\)\nexcept ImportError:\n\s+import pytest\n\s+pytest\.skip\([^)]+\)'
    
    # Replacement text
    replacement = '''try:
    from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
    from ibm_cloud_networking_services.\\1 import *
except ImportError:
    import pytest
    pytest.skip("ibm_cloud_sdk_core or ibm_cloud_networking_services not installed", allow_module_level=True)

import inspect
import json
import os
import pytest
import re
import responses
import urllib'''
    
    # Extract module name from the file
    module_match = re.search(r'from ibm_cloud_networking_services\.([a-z_]+) import', content)
    if not module_match:
        print(f"Could not find module import in {file_path}")
        return False
    
    module_name = module_match.group(1)
    
    # Simple replacement approach
    lines = content.split('\n')
    new_lines = []
    i = 0
    fixed = False
    
    while i < len(lines):
        # Look for the start of the problematic section
        if not fixed and i < len(lines) - 5 and lines[i].strip() == 'try:' and lines[i+1].strip() == 'try:':
            # Skip all the nested try-except blocks
            skip_count = 0
            temp_i = i
            while temp_i < len(lines) and skip_count < 60:  # Look ahead max 60 lines
                if 'crn = ' in lines[temp_i] or 'class Test' in lines[temp_i]:
                    break
                temp_i += 1
                skip_count += 1
            
            # Add the fixed import block
            new_lines.append('try:')
            new_lines.append('    from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator')
            
            # Find the correct module import
            for check_line in lines[i:temp_i]:
                if f'from ibm_cloud_networking_services.{module_name} import' in check_line:
                    new_lines.append(f'    from ibm_cloud_networking_services.{module_name} import *')
                    break
            
            new_lines.append('except ImportError:')
            new_lines.append('    import pytest')
            new_lines.append('    pytest.skip("ibm_cloud_sdk_core or ibm_cloud_networking_services not installed", allow_module_level=True)')
            new_lines.append('')
            new_lines.append('import inspect')
            new_lines.append('import json')
            new_lines.append('import os')
            new_lines.append('import pytest')
            new_lines.append('import re')
            new_lines.append('import responses')
            new_lines.append('import urllib')
            
            i = temp_i
            fixed = True
        else:
            new_lines.append(lines[i])
            i += 1
    
    if fixed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f"Fixed {file_path}")
        return True
    else:
        print(f"No fix needed for {file_path}")
        return False

def main():
    test_dir = Path('/private/tmp/sdk-automation/python-sdk/test/unit')
    
    test_files = list(test_dir.glob('test_*.py'))
    test_files = [f for f in test_files if f.name != 'test_common.py']  # Skip test_common.py
    
    fixed_count = 0
    for test_file in sorted(test_files):
        if fix_file(test_file):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} out of {len(test_files)} files")

if __name__ == '__main__':
    main()
