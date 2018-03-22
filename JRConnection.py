from Jiro.source.JRParser import Parser
from Jiro.source import Utils as JRUtils

def parse(verbose, script):
    if verbose:
        JRUtils.psinit()
    p = Parser(verbose)
    p.parse(script, True)

def help():
    JRUtils.psinit()
    JRUtils.ps_help("percscript")
