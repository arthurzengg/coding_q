def solution(commands):
    # We'll map:
    #  cp -> cpCount
    #  ls -> lsCount
    #  mv -> mvCount
    cp_count = 0
    ls_count = 0
    mv_count = 0

    # Cache the final (base) command triggered by each line
    final_command = [None] * len(commands)

    def get_final_command(i):
        # If we've already resolved line i, just return it
        if final_command[i] is not None:
            return final_command[i]

        cmd = commands[i]
        if cmd.startswith('!'):
            # it's of the form "!k"
            k = int(cmd[1:])  # parse the integer after '!'
            base = get_final_command(k - 1)  # 1-based index
            final_command[i] = base
            return base
        else:
            # it is either 'cp', 'ls', or 'mv'
            final_command[i] = cmd
            return cmd

    # Main loop: for each typed line, find out what real command it triggers
    for i in range(len(commands)):
        base_cmd = get_final_command(i)
        if base_cmd == "cp":
            cp_count += 1
        elif base_cmd == "ls":
            ls_count += 1
        elif base_cmd == "mv":
            mv_count += 1
        else:
            # if input is guaranteed only cp/ls/mv/!k, we shouldn't get here
            pass

    return [cp_count, ls_count, mv_count]

print(solution(["ls", "cp", "mv", "!3", "mv", "!1", "!6"]))