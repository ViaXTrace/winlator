import os, sys

gradle_path = "winlator-src/app/build.gradle"

if not os.path.exists(gradle_path):
    print(f"ERROR: {gradle_path} not found")
    sys.exit(1)

with open(gradle_path, "r") as f:
    content = f.read()

if "packagingOptions" in content:
    print("packagingOptions already present — skipping")
    sys.exit(0)

patch = '''    packagingOptions {
        pickFirst 'lib/**/*.so'
    }

'''

if "    lintOptions {" in content:
    content = content.replace("    lintOptions {", patch + "    lintOptions {")
    with open(gradle_path, "w") as f:
        f.write(content)
    print("SUCCESS: packagingOptions injected before lintOptions")
elif "}" in content:
    # Fallback: insert before closing brace of android block
    last_brace = content.rfind("\n}")
    content = content[:last_brace] + "\n" + patch.rstrip() + "\n}"
    with open(gradle_path, "w") as f:
        f.write(content)
    print("SUCCESS: packagingOptions injected (fallback)")
else:
    print("ERROR: could not find insertion point")
    sys.exit(1)
