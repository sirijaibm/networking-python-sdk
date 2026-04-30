#!/usr/bin/env python3
"""Simple line-by-line fix for all test files."""

from pathlib import Path

def fix_file(file_path):
    """Fix a single test file by rebuilding imports section."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find where the problematic imports start and end
    start_idx = None
    end_idx = None
    module_name = None
    
    for i, line in enumerate(lines):
        # Find the start of nested try blocks
        if start_idx is None and line.strip() == 'try:' and i+1 < len(lines) and lines[i+1].strip() == 'try:':
            start_idx = i
        
        # Find the module import
        if 'from ibm_cloud_networking_services.' in line and ' import' in line:
            import_parts = line.split('.')
            if len(import_parts) >= 2:
                module_part = import_parts[1].split()[0]
                module_name = module_part
        
        # Find where imports end (look for crn = or class Test or _service =)
        if start_idx is not None and end_idx is None:
            if ('crn = ' in line or 'class Test' in line or '_service = ' in line or 
                (line.strip() and not line.strip().startswith(('try:', 'except', 'import', 'from', 'pytest')))):
                end_idx = i
                break
    
    if start_idx is not None and end_idx is not None and module_name:
        # Build the fixed import section
        fixed_imports = [
            'try:\n',
            '    from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator\n',
            f'    from ibm_cloud_networking_services.{module_name} import *\n',
            'except ImportError:\n',
            '    import pytest\n',
            '    pytest.skip("ibm_cloud_sdk_core or ibm_cloud_networking_services not installed", allow_module_level=True)\n',
            '\n',
            'import inspect\n',
            'import json\n',
        ]
        
        # Check if original had 'import os'
        has_os = any('import os' in line for line in lines[start_idx:end_idx])
        if has_os:
            fixed_imports.append('import os\n')
        
        fixed_imports.extend([
            'import pytest\n',
            'import re\n',
            'import responses\n',
        ])
        
        # Check if original had 'import urllib'
        has_urllib = any('import urllib' in line for line in lines[start_idx:end_idx])
        if has_urllib:
            fixed_imports.append('import urllib\n')
        
        # Rebuild the file
        new_lines = lines[:start_idx] + fixed_imports + lines[end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print(f"✓ Fixed {file_path.name} (module: {module_name})")
        return True
    else:
        print(f"✗ Could not fix {file_path.name} (start={start_idx}, end={end_idx}, module={module_name})")
        return False

def main():
    test_dir = Path('/private/tmp/sdk-automation/python-sdk/test/unit')
    
    # Get all test files except test_alerts_v1.py (already fixed) and test_common.py (different structure)
    test_files = [f for f in test_dir.glob('test_*.py') 
                  if f.name not in ['test_alerts_v1.py', 'test_common.py']]
    
    fixed_count = 0
    for test_file in sorted(test_files):
        if fix_file(test_file):
            fixed_count += 1
    
    print(f"\n{'='*60}")
    print(f"Fixed {fixed_count} out of {len(test_files)} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
