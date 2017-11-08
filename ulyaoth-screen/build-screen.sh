# This script is supposed to run as the user "ulyaoth".

# Create build environment.
rpmdev-setuptree

# Download spec file.
wget https://raw.githubusercontent.com/ulyaoth/repository/master/ulyaoth-screen/SPECS/ulyaoth-screen.spec -O /home/ulyaoth/rpmbuild/SPECS/ulyaoth-screen.spec

# Download additional files specified in spec file.
spectool /home/ulyaoth/rpmbuild/SPECS/ulyaoth-screen.spec -g -R

# Install all requirements
if type dnf 2>/dev/null
then
  dnf builddep -y /home/ulyaoth/rpmbuild/SPECS/ulyaoth-screen.spec
elif type yum 2>/dev/null
then
  yum-builddep -y /home/ulyaoth/rpmbuild/SPECS/ulyaoth-screen.spec
fi

# Build the rpm.
rpmbuild -ba /home/ulyaoth/rpmbuild/SPECS/ulyaoth-screen.spec

# Copy the file to Ulyaoth home folder.
cp /home/ulyaoth/rpmbuild/SRPMS/* /home/ulyaoth/
cp /home/ulyaoth/rpmbuild/RPMS/x86_64/* /home/ulyaoth/
cp /home/ulyaoth/rpmbuild/RPMS/noarch/* /home/ulyaoth/