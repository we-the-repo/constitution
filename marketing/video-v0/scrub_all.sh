#!/bin/bash
cd "$(dirname "$0")"
export HOME=/workspace
for t in 2 6 10 13 17 22 27 32 36 42; do
  python3 render.py --scrub $t 2>&1 | tail -1
done
