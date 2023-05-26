#!/usr/bin/env python

import re
from os.path import exists, getmtime
from sys import argv
from subprocess import check_output, STDOUT

def _run(cmd):
    return check_output(cmd, stderr=STDOUT, shell=True)

def _stem_name(outdir, i):
    return outdir + "/" + str(i) + ".wav"

def _export_track(modfile, outdir, i):
    return _run("xmp -S " + str(i) + " " + modfile + " --nocmd -m -a 1 -o " + _stem_name(outdir, i)).decode("utf8")

def _stem_is_older(modfile, outdir, i):
    return not exists(_stem_name(outdir, i)) or (getmtime(modfile) > getmtime(_stem_name(outdir, i)))

def mod_make_stems(modfile, outdir, channel_count):
    return [_export_track(modfile, outdir, i)
            for i in range(channel_count)
            if _stem_is_older(modfile, outdir, i)]

def mod_get_channel_names(modfile, channels):
    with open(modfile, "rb") as m:
        f = m.read()
        try:
            i = f.index(bytearray("CNAM", "utf8"))
        except ValueError:
            return {}
        #for n in range(channels):
        #        print(f[i+n*20+8:i+(n+1)*20+8])
        channel_names = {}
        for n in range(channels):
            val = f[i+n*20+8:i+(n+1)*20+8]
            if val[:4] == b"XTPM" or val[:4] == b"IMPI":
                break
            try:
                name = val.decode("utf8").rstrip("\x00")
                if name:
                    channel_names[n] = name
            except UnicodeDecodeError:
                break
        return channel_names

def mod_get_info(modfile):
    if exists(modfile):
        info = _run("xmp --load-only -C " + modfile).decode("utf8")
        #print(info)
        channels = int(re.findall("Channels\ +: (\d+)", info)[0])
        commentlines = re.findall("> (.*?)[\n$]", info)
        comments = "\n".join(commentlines)
        infolines = {l[0]: l[2] for l in re.findall("(.*?)(\s*): (.*)", info)}
        return {"channelcount": channels,
                "comments": comments,
                "channelnames": mod_get_channel_names(modfile, channels),
                "info": infolines,
                "raw": info}

def modrender():
    from pprint import pprint
    from os import makedirs
    if len(argv) > 1:
        mod_info = mod_get_info(argv[1])
        pprint(mod_info)
        makedirs("stems", exist_ok=True)
        mod_make_stems(argv[1], "stems", mod_info["channelcount"])
    else:
        print("Usage: modrender MODFILE")

if __name__ == "__main__":
    modrender()
