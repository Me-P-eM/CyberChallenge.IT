# Generic
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
echo "wireshark-common wireshark-common/install-setuid boolean true" | sudo debconf-set-selections
sudo DEBIAN_FRONTEND=noninteractive apt install -y curl php python3.12 python3-pip git binwalk gimp wireshark tshark ht ltrace gdb patchelf elfutils ruby-dev
python3 -m pip install pyshark pwntools ropper pycryptodome mtp --break-system-packages
sudo gem install one_gadget seccomp-tools
mkdir -p /home/user/tools


# Install JDK 23
sudo wget -O /opt/jdk-23_linux-x64_bin.deb https://download.oracle.com/java/23/latest/jdk-23_linux-x64_bin.deb
(cd /opt && sudo dpkg -i jdk-23_linux-x64_bin.deb)
sudo rm /opt/jdk-23_linux-x64_bin.deb


# Install Visual Studio Code
sudo apt-get install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg
sudo apt install apt-transport-https
sudo apt update
sudo apt install code


# Install Ngrok
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok


# Install Docker
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
wget https://desktop.docker.com/linux/main/amd64/docker-desktop-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64
sudo apt-get update
sudo apt-get install ./docker-desktop-amd64.deb
sudo usermod -aG docker $USER
newgrp docker


# Install Stegsolve
wget -O /home/user/tools/stegsolve.jar http://www.caesum.com/handbook/Stegsolve.jar
chmod +x /home/user/tools/stegsolve.jar


# Install JohnTheRipper
git clone https://github.com/openwall/john -b bleeding-jumbo /home/user/tools/john
(cd /home/user/tools/john/src && ./configure && make -s clean && make -sj8)


# Install Burp Suite Community
wget -O /home/user/tools/burpsuite.sh 'https://portswigger-cdn.net/burp/releases/download?product=community&version=2024.10.3&type=Linux'
(cd /home/user/tools && sh burpsuite.sh)
rm /home/user/tools/burpsuite.sh
mv /home/user/BurpSuiteCommunity /home/user/tools/


# Install Postman
wget -O /home/user/tools/postman.tar.gz https://dl.pstmn.io/download/latest/linux_64
(cd /home/user/tools && tar -xf postman.tar.gz)
rm /home/user/tools/postman.tar.gz


# Install pwndbg
git clone https://github.com/pwndbg/pwndbg /home/user/tools/pwndbg
(cd /home/user/tools/pwndbg && ./setup.sh)


# Install Ghidra
wget -O /home/user/tools/ghidra.zip https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.2.1_build/ghidra_11.2.1_PUBLIC_20241105.zip
(cd /home/user/tools && unzip ghidra.zip)
rm /home/user/tools/ghidra.zip


# Install SageMath
sudo apt install -y automake bc binutils bzip2 ca-certificates cliquer cmake curl ecl eclib-tools fflas-ffpack flintqs g++ gengetopt gfan gfortran git glpk-utils gmp-ecm lcalc libatomic-ops-dev libboost-dev libbraiding-dev libbz2-dev libcdd-dev libcdd-tools libcliquer-dev libcurl4-openssl-dev libec-dev libecm-dev libffi-dev libflint-dev libfreetype-dev libgc-dev libgd-dev libgf2x-dev libgiac-dev libgivaro-dev libglpk-dev libgmp-dev libgsl-dev libhomfly-dev libiml-dev liblfunction-dev liblrcalc-dev liblzma-dev libm4rie-dev libmpc-dev libmpfi-dev libmpfr-dev libncurses-dev libntl-dev libopenblas-dev libpari-dev libpcre3-dev libplanarity-dev libppl-dev libprimesieve-dev libpython3-dev libqhull-dev libreadline-dev librw-dev libsingular4-dev libsqlite3-dev libssl-dev libsuitesparse-dev libsymmetrica2-dev zlib1g-dev libzmq3-dev libzn-poly-dev m4 make nauty openssl palp pari-doc pari-elldata pari-galdata pari-galpol pari-gp2c pari-seadata patch perl pkg-config planarity ppl-dev python3-setuptools python3-venv r-base-dev r-cran-lattice singular sqlite3 sympow tachyon tar tox xcas xz-utils texlive-latex-extra texlive-xetex latexmk pandoc dvipng
git clone --branch master https://github.com/sagemath/sage.git /home/user/tools/sagemath
(cd /home/user/tools/sagemath && make configure && ./configure && MAKE="make -j8" make && sudo ln -sf /home/user/tools/sagemath/sage /usr/local/bin)


# Install Binary Ninja
wget -O /home/user/tools/binaryninja.zip https://cdn.binary.ninja/installers/binaryninja_free_linux.zip
(cd /home/user/tools && unzip binaryninja.zip)
rm /home/user/tools/binaryninja.zip

# Fix capstone
python3 -m pip install capstone==5.0.3 --break-system-packages