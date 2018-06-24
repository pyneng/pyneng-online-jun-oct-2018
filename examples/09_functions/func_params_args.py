def delete_exclamation_from_cfg(in_cfg, out_cfg):
    with open(in_cfg) as in_file, open(out_cfg, 'w') as out_file:
        for line in in_file:
            if not line.startswith('!'):
                out_file.write(line)


delete_exclamation_from_cfg('r1.txt', 'result.txt')
