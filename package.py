name = "alembic"

authors = [
    "Sony Pictures Imageworks"
]

# NOTE: <alembic_version>.sse.<SSE_version>

version = "1.8.5.sse.1.0.0"

description = \
    """
    Alembic is an open computer graphics interchange framework.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "hdf5-1.10.0",
    "boost-1.76.0",
    "openexr-3.1.12",
]

private_build_requires = [
]

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.11"],
]

uuid = "repository.alembic"

# Pass arguments to REZ build system:
# rez-build -i -- -DCMAKE_CXX_FLAGS="-D H5_BUILT_AS_DYNAMIC_LIB"
# rez-release -- -DCMAKE_CXX_FLAGS="-D H5_BUILT_AS_DYNAMIC_LIB"

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.ALEMBIC_ROOT = "{root}"
    env.ALEMBIC_LOCATION = "{root}"

    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
