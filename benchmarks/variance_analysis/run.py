"""
TritonBench variance analysis.
Generates two types of variance data: 1. intra-benchmark variance, 2. inter-benchmark variance.

Intra-benchmark variance is the variance among the repeated runs within a single benchmark.
Inter-benchmark variance is the variance among the p50 of repeated runs when running the same benchmark multiple times.

We will run the benchmark in three modes:
1. The default mode (triton.testing.do_bench), which is the fastest mode but includes host-overhead
2. The CUDAGraph mode, has less host-overhead, but does not support all operators, has 10 latency data points per benchmark run
3. The Profiler mode, is the slowest and most accurate, only has 1 data point per benchmark run

For each mode, we record the following metrics:
1. p10 latency (if applicable)
2. p50 latency
3. p90 latency (if applicable)
4. variance (if applicable) = (max - min) / min
5. std (if applicable)
6. inter-benchmark variance (if repeat > 1) = (max - min) / min
7. inter-benchmark std (if repeat > 1)
"""

RUN_CONFIG = "autogen.json"


def get_parser():
    parser = argparse.ArgumentParser(
        description="Run TritonBench and generate variance analysis data."
    )
    parser.add_argument("--op", type=str, required=True, help="Operator to benchmark. Need to be names in autogen.yaml")
    parser.add_argument("--repeat", type=int, default=5, help="Number of repetitions per benchmark run")


if __name__ == "__main__":
    pass