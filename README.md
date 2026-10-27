# langchain-eval-plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A production callback plugin for **LangChain** and **LlamaIndex** that traces step-by-step latency, measures retrieval faithfulness, and monitors token costs in real time.

---

## Quickstart

```python
from langchain_eval.callbacks import EvaluationTracerCallback

tracer = EvaluationTracerCallback()
# Attach to any LangChain execution
# chain.run("Query", callbacks=[tracer])
print(tracer.get_summary())
```

---

## License

MIT License (c) 2024 Soujanya Gupta.

<!-- PR #12: docs: clarify benchmark metric configuration options -->

<!-- PR #25: perf: optimize memory buffer reuse during batch evaluation -->
