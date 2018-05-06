from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")


name = "imds_utils"
default_task = "publish"


@init
def set_properties(project):
    pass
