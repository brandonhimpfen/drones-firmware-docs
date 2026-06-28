from drone_fw.manifest import validate_manifest

def test_valid_manifest():
    manifest = {"name":"fw","version":"1.0.0","target":"board","artifact":{"filename":"fw.bin","format":"bin"},"checksum":{"algorithm":"sha256","value":"a"*64},"build":{"commit":"abc","timestamp":"now","toolchain":"gcc"}}
    assert validate_manifest(manifest) == []

def test_missing_fields():
    assert validate_manifest({})
