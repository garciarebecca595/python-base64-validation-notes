# Decode Base64 strictly: implementation

## What the example does

validate=True rejects non-alphabet characters. The decoded bytes must also be valid UTF-8; binary data needs a different output representation.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"aGVsbG8="
```

Expected result:

```json
"hello"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
