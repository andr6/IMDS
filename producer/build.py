from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")


name = "imds_producer"
default_task = "publish"


@init
def set_properties(project):
    pass

@init
def initialize(project):
    project.depends_on("pika")
    project.depends_on("pyinotify")
    project.depends_on("cPickle")
    project.depends_on("shutil")
    project.depends_on("sqlite3")
