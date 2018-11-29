# Cloud Formation Drift Checker

* This script does these things...

** Kicks detect_drift for all Cfn stacks in status ( CREATE_COMPLETE, UPDATE_COMPLETE, UPDATE_ROLLBACK_COMPLETE ) in all region.

** Wait for 1 minute

** Returns list of all DRIFTED stacks

* Usage

'''
cfn-drift-checker.py

'''