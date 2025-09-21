#!/bin/bash
exec socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"timeout 300 python3 chall.py"

