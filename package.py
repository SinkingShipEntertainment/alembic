name = "alembic"

authors = [
    "Sony Pictures Imageworks"
]

version = "1.7.10"

description = \
    """
    Alembic is an open computer graphics interchange framework.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    #c.build_thread_count = "physical_cores"

requires = [
    "hdf5-1.10.0",
    "openexr-2.3.0",
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.alembic"

# Pass arguments to REZ build system:
# rez-build -i -- -DCMAKE_CXX_FLAGS="-D H5_BUILT_AS_DYNAMIC_LIB"
# rez-release -- -DCMAKE_CXX_FLAGS="-D H5_BUILT_AS_DYNAMIC_LIB"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.ALEMBIC_ROOT = "{root}"
    env.ALEMBIC_LOCATION = "{root}"

    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
