import yara

def Compile(in_uncompiled_rules, out_compiled_rules):
    rules = yara.compile(in_uncompiled_rules)
    rules.save(out_compiled_rules)
