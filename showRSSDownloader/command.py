from distutils.cmd import Command

class ShowRSSDownloader(Command):
    description = "run my command"
    user_options = tuple()

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Hola mundo")
