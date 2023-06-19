#!/usr/bin/python
# -*- coding: utf-8 -*-

import anyconfig
import json
import pathlib
import re
import os
import sys
import yaml

from argparse import ArgumentParser


class Dumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(Dumper, self).increase_indent(flow, False)


def represent_str(dumper, instance):
    if "\n" in instance:
        instance = re.sub(" +\n| +$", "\n", instance)
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", instance, style="|"
            )
    else:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", instance
            )


class EasyConvert:
    def __init__(self, path=None, f='yaml', dest=None):
        self.path = pathlib.Path(path)
        self.format = f
        if dest:
            self.dest = pathlib.Path(dest)
            conf = self.load_config()
            self.dump_config(conf)
        else:
            conf = self.load_config()
            print(self.dumps_config(conf))

    def dump_config(self, conf):
        if self.format == "yaml":
            yaml.add_representer(str, represent_str)
            if self.dest:
                return self.dest.write_text(
                    yaml.dump(
                        conf, Dumper=Dumper,
                        default_flow_style=False, sort_keys=False
                    )
                )
        elif self.format == "json":
            if self.dest:
                return anyconfig.dump(conf, self.dest,  "json")


    def dumps_config(self, conf):
        if self.format == "yaml":
            yaml.add_representer(str, represent_str)
            return anyconfig.dumps(
                conf,
                "yaml",
                Dumper=Dumper,
                default_flow_style=False,
                sort_keys=False,
                sequence=4,
                offset=2
            )
        elif self.format == "json":
            return anyconfig.dumps(conf, "json", indent=2)
        else:
            return None

    def load_config(self):
        if self.path:
            try:
                conf = anyconfig.load(self.path)
            except (yaml.YAMLError, json.decoder.JSONDecodeError,
                    yaml.parser.ParserError) as e:
                sys.stderr.write(e)
                return False
            return conf
        return False

def parser():
    usage = 'python3 {} <type> <command> [option]\n'.format(os.path.basename(__file__))
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument('-i', '--input', type=str,
                           dest='input_file', required=True,
                           help='Set path of file to be converted')
    argparser.add_argument('-o', '--output', type=str,
                           dest='output_file', required=False,
                           help='user name')
    argparser.add_argument('-f', '--format', type=str,
                           dest='format', required=False,
                           help='file format, json or yaml')
    args = argparser.parse_args()
    return args

def main():
    args = parser()
    ez_convert = EasyConvert(args.input_file, args.format,  args.output_file)

if __name__ == "__main__":
    main()
