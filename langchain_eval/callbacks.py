import time

class EvaluationTracerCallback:
    def __init__(self):
        self.step_latencies = []
        self.start_time = None

    def on_chain_start(self, *args, **kwargs):
        self.start_time = time.perf_counter()

    def on_chain_end(self, *args, **kwargs):
        if self.start_time:
            self.step_latencies.append((time.perf_counter() - self.start_time) * 1000.0)

    def get_summary(self):
        return {
            "total_steps": len(self.step_latencies),
            "mean_latency_ms": round(sum(self.step_latencies)/len(self.step_latencies), 2) if self.step_latencies else 0.0
        }

    async def on_chain_start_async(self, *args, **kwargs):
        pass
