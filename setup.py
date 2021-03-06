from setuptools import setup, find_packages


def scm_version():
    def local_scheme(version):
        if version.tag and not version.distance:
            return version.format_with("")
        else:
            return version.format_choice("+{node}", "+{node}.dirty")
    return {
        "relative_to": __file__,
        "version_scheme": "guess-next-dev",
        "local_scheme": local_scheme
    }


setup(
    name="nmigen-stdio",
    use_scm_version=scm_version(),
    author="whitequark",
    author_email="whitequark@whitequark.org",
    description="Industry standard I/O for nMigen",
    #long_description="""TODO""",
    license="BSD",
    setup_requires=["setuptools_scm"],
    install_requires=["nmigen>=0.0,<=0.5"],
    packages=find_packages(),
    project_urls={
        "Source Code": "https://github.com/m-labs/nmigen-stdio",
        "Bug Tracker": "https://github.com/m-labs/nmigen-stdio/issues",
    },
)
