#!/bin/bash

# Fix all test files except test_alerts_v1.py and test_common.py
cd /private/tmp/sdk-automation/python-sdk/test/unit

for file in test_*.py; do
    if [ "$file" != "test_alerts_v1.py" ] && [ "$file" != "test_common.py" ]; then
        echo "Processing $file..."
        
        # Extract module name from filename (e.g., test_caching_api_v1.py -> caching_api_v1)
        module=$(echo "$file" | sed 's/test_//' | sed 's/\.py//')
        
        # Use Python to do the regex replacement
        python3 << EOF
import re

with open('$file', 'r') as f:
    content = f.read()

# Pattern to match nested try-except blocks
pattern = r'try:\ntry:\ntry:\n\s+from ibm_cloud_sdk_core\.authenticators\.no_auth_authenticator import NoAuthAuthenticator.*?except ImportError:\n\s+import pytest\n\s+pytest\.skip\([^)]+\)\nimport inspect'

# Check if file needs fixing
if re.search(pattern, content, re.DOTALL):
    # Find the module import line
    module_match = re.search(r'from ibm_cloud_networking_services\.([a-z_0-9]+) import', content)
    if module_match:
        module_name = module_match.group(1)
        
        # Replacement
        replacement = f'''try:
    from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
    from ibm_cloud_networking_services.{module_name} import *
except ImportError:
    import pytest
    pytest.skip("ibm_cloud_sdk_core or ibm_cloud_networking_services not installed", allow_module_level=True)

import inspect'''
        
        # Replace the pattern
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open('$file', 'w') as f:
            f.write(content)
        print(f"Fixed $file with module {module_name}")
    else:
        print(f"Could not find module in $file")
else:
    print(f"No fix needed for $file")
EOF
    fi
done

echo "Done!"
