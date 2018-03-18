from PercScript.source.PSParser import Parser
from PercScript.source import Utils as PSUtils

def parse(verbose, script):
    if verbose:
        PSUtils.psinit()
    p = PSParser.Parser(verbose)
    p.parse(script, True)

def help():
    PSUtils.psinit()
    PSUtils.ps_help("percscript")
