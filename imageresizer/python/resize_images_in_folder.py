import os
import traceback
import subprocess
import sys

class ResizeImage:

    def __init__(self, source_path, width=3072, height=1296):

        self.ffmpeg_exc_path = self.get_os_path()

        self.width = width
        self.height = height
        self.source_dir = source_path.replace("\\", "/")
        self.overwrite = True

    def handle_subprocess(self, exc_cmd):
        """ Handles the execution of a command via subprocess

        :param exc_cmd: Is a String or a list of string items to be used as the execution command
        :return: Two values, the first is a boolean representing the result of the command using 0 or False if the
        was no error in the execution and 1 or True if an erroer was found and the second returned parameter is
        the error output string found.
        """

        etype = None
        process = None

        print "About to execute ffmpeg cmd..."
        try:
            process = subprocess.Popen(exc_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()
            if process.returncode:
                # Tag for a command error result
                etype = 'cmd'
        except:
            # Exception for any execution problemn within subprocess and the os.
            out = traceback.format_exc()
            # Tag for a os execution error
            etype = 'exc'
        finally:
            print "ffmpeg cmd: ", exc_cmd

        # Format the output error result based on the type of error found.
        if etype is not None:
            if etype == 'cmd':
                erroutput = 'Command execution error:\n{}'.format(out)
            else:
                erroutput = 'Module execution error:\n{}'.format(out)
        else:
            erroutput = out

        print erroutput

        return process.returncode

    def get_os_path(self, os_folder="resources", bin_mode="ffmpeg"):

        root_folder = os.getcwd()
        module_folder = os.path.dirname(os.path.dirname(__file__))
        print "root_folder", root_folder
        print "module_folder: ", module_folder
        bin_folder = "\\".join((root_folder, module_folder, os_folder, bin_mode))
        bin_folder = bin_folder.replace("\\", "/")
        print bin_folder

        return bin_folder

    def ensure_folder(self, path):
        dir = os.path.dirname(path)

        if not os.path.exists(dir):
            os.makedirs(dir)

    def create_command_from_files(self):
        for root, dirs, files in os.walk(self.source_dir):
            for f in files:
                source_file = ("/".join((root, f))).replace("\\", "/")
                new_file = self.create_resized_name(source_file)
                self.ensure_folder(new_file)
                # skip to the next path when file exists and overwrite is not enabled
                if not os.path.exists(new_file) or self.overwrite:
                    cmd = self.create_command(source_file, new_file)
                    yield source_file, cmd
                else:
                    print "Skiping image, overwirde is enabled!",  new_file


    def create_resized_name(self, path):
        print path
        print self.source_dir
        new_dirname = os.path.dirname(path).split(self.source_dir)[1]
        if new_dirname:
            new_dirname = new_dirname[1:]
        sufix = "{width}x{height}".format(width=self.width, height=self.height)

        dir_root = os.path.dirname(self.source_dir)
        dir_new_base = "_".join((os.path.basename(self.source_dir), sufix))

        new_root_path = "\\".join((dir_root, dir_new_base, new_dirname))

        basename, ext = os.path.splitext(os.path.basename(path))
        name_tuple = (basename, '_', sufix, ext)
        new_name = "".join(name_tuple)
        new_path = os.path.join(new_root_path, new_name)

        return new_path


    def create_command(self, source, destination):

        ffmpeg_exc = self.get_os_path()

        params = "-y " \
                 "-noautorotate " \
                 "-i " \
                 "{source_path} " \
                 "-vf scale={width_size}:{height_size} " \
                 "{new_path}"

        command = " ".join((ffmpeg_exc, params))
        format_data = {
            "source_path": source,
            "width_size": self.width,
            "height_size": self.height,
            "new_path": destination
        }

        return command.format(**format_data)

    def execute(self):
        resized = 0
        for path, cmd in self.create_command_from_files():
            print "\nProcessing: {}".format(path)
            if self.handle_subprocess(cmd):
                print 'ERROR resizing image: {} !!!'.format(path)
            else:
                resized = resized + 1

            print "Image process finished!"

        return resized
