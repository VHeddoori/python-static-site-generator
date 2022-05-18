import typer
from ssg.site import Site
import ssg.parsers

def main(source="content", dest="dist"):
    config = {"source": source,
              "dest": dest,
              "parsers": [ssg.parsers.ResourceParser()]
               }
    Site(**config).build()

def load_parser(self, extension):
    for parser in self.parsers:
            if parser.valid_extension(extension):
                return parser
            
def run_parser(self, path):
    parser = self.load_parser(path.suffix)
    if parser is not None:
        parser.parse(path, self.source, self.dest)
    else:
        print("Not Implemented")
        
def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)

typer.run(main)