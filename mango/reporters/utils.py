def render_tree(tree, d=0, space='  '):
    ret = ''
    if (tree == None or len(tree) == 0):
        ret += space * d + " -\n"
    else:
        for key, val in tree.items():
            if (isinstance(val, dict)):
                ret += space * d + key + '\n'
                ret += render_tree(val, d+1)
            else:
                ret += space * d + f'{key}: {val}'
    return ret
