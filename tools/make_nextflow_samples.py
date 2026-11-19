"""Instructor helper: regenerate samples_files/nextflow.log and trace.txt (synthetic, deterministic)."""
import random
from datetime import datetime, timedelta

random.seed(42)
samples = [f"sample{i:02d}" for i in range(1, 9)]
procs = [("FASTQC", 40, 4), ("FASTP", 60, 8), ("SPADES", 600, 16), ("PROKKA", 300, 8), ("AMRFINDER", 90, 4)]
t0 = datetime(2026, 3, 12, 9, 14, 3)
log, trace = [], []
ts = lambda t: t.strftime("%b-%d %H:%M:%S.") + f"{random.randint(0, 999):03d}"
log.append(f"{ts(t0)} [main] INFO  nextflow.cli.CmdRun - Launching `main.nf` [amazing_curie] DSL2 - revision: 3f9a1c2b")
log.append(f"{ts(t0)} [main] DEBUG nextflow.executor.ExecutorFactory - Extension executors providing []")
log.append(f"{ts(t0)} [main] INFO  nextflow.Session - Session UUID: 7c1d2e9a-55b0-4a1f-9d3c-0e8a41b2c6aa")
task_id, t = 0, t0 + timedelta(seconds=2)
trace.append("\t".join(["task_id", "hash", "name", "status", "exit", "submit", "duration", "realtime", "%cpu", "peak_rss"]))
failed_once = {("SPADES", "sample03"), ("PROKKA", "sample06")}
for s in samples:
    for p, base, mem in procs:
        for attempt in (1, 2):
            task_id += 1
            h = f"{random.randint(0, 255):02x}/{random.randint(0, 0xffffff):06x}"
            t += timedelta(seconds=random.randint(1, 6))
            dur = int(base * random.uniform(0.6, 1.6))
            name = f"{p} ({s})" + (f" (retry {attempt - 1})" if attempt == 2 else "")
            log.append(f"{ts(t)} [Task submitter] INFO  nextflow.Session - [{h}] Submitted process > {name}")
            fail = (p, s) in failed_once and attempt == 1
            exit_code = (137 if p == "SPADES" else 1) if fail else 0
            t_end = t + timedelta(seconds=dur)
            t_end_max = max(t_end, t_end_max if "t_end_max" in globals() else t_end)
            if fail:
                log.append(f"{ts(t_end)} [Task monitor] ERROR nextflow.processor.TaskProcessor - Error executing process > '{p} ({s})' Caused by: Process `{p} ({s})` terminated with an error exit status ({exit_code})")
                log.append(f"{ts(t_end)} [Task monitor] WARN  nextflow.processor.TaskProcessor - Process `{p} ({s})` failed, retrying (attempt 2)")
            else:
                log.append(f"{ts(t_end)} [Task monitor] DEBUG nextflow.processor.TaskProcessor - Task completed > TaskHandler[id: {task_id}; name: {name}; status: COMPLETED; exit: 0]")
            trace.append("\t".join(map(str, [task_id, h, name, "FAILED" if fail else "COMPLETED", exit_code, t.strftime("%Y-%m-%d %H:%M:%S"), f"{dur}s", f"{int(dur * .9)}s", f"{random.uniform(40, 380):.1f}%", f"{mem * random.uniform(.5, 1.5):.1f} GB"])))
            if not fail:
                break
log = sorted(log, key=lambda l: l[:19])  # chronological, like a real log
log.append(f"{log[-1][:7]}{t_end_max.strftime('%H:%M:%S')}.500 [main] INFO  nextflow.Session - Execution complete -- Goodbye")
open("samples_files/nextflow.log", "w", newline="\n").write("\n".join(log) + "\n")
open("samples_files/trace.txt", "w", newline="\n").write("\n".join(trace) + "\n")
