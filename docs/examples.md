# ⚡ Examples and performance

Run examples from the project root.

| File | Focus |
| --- | --- |
| `examples/custom-units/exp-1.py` | Core dimensional expressions |
| `examples/custom-units/exp-2.py` | Process-engineering units |
| `examples/custom-units/exp-3.py` | Warm-cache benchmark |
| `examples/custom-units/exp-4.py` | Diverse-unit catalog benchmark |
| `examples/mapper.py` | Reference discovery and mapping |

```powershell
python examples/custom-units/exp-4.py
```

Benchmark output is environment-dependent.  The dimensional examples validate
the `RefsX` catalog and warm the expression cache before timed conversions.
