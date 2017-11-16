# This script is supposed to run as the user "ulyaoth".

# Create build environment.
rpmdev-setuptree

# Download spec file.
wget https://raw.githubusercontent.com/ulyaoth/repository/master/ulyaoth-hiawatha/SPECS/ulyaoth-hiawatha.spec -O /home/ulyaoth/rpmbuild/SPECS/ulyaoth-hiawatha.spec
wget https://raw.githubusercontent.com/ulyaoth/repository/master/ulyaoth-hiawatha/SPECS/ulyaoth-hiawatha-letsencrypt.spec -O /home/ulyaoth/rpmbuild/SPECS/ulyaoth-hiawatha-letsencrypt.spec

# Remove old cmake
if type dnf 2>/dev/null
then
  sudo dnf remove -y cmake*
elif type yum 2>/dev/null
then
  sudo yum remove -y cmake*
fi

# Install all requirements
if type dnf 2>/dev/null
then
  sudo dnf builddep -y /home/ulyaoth/rpmbuild/SPECS/ulyaoth-hiawatha.spec
elif type yum 2>/dev/null
then
  sudo yum-builddep -y /home/ulyaoth/rpmbuild/SPECS/ulyaoth-hiawatha.spec
fi

# Download additional files specified in spec file.
spectool /home/ulyaoth/rpmbuild/SPECS/ulyaoth-hiawatha.spec -g -R

# Build the rpm.
rpmbuild -ba /home/ulyaoth/rpmbuild/SPECS/ulyaoth-hiawatha.spec
rpmbuild -ba /home/ulyaoth/rpmbuild/SPECS/ulyaoth-hiawatha-letsencrypt.spec