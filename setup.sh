#!/bin/bash
BASHCMD = "python $HOME/.faang"

LINUXCMD = "sudo python $HOME/.faang"

install_pip() {
    echo "Starting pip installation..."
    if [ -x "$(command -v pip)" ]; then
        echo "pip is already installed."
    else
        echo "Installing pip..."
        if [ -x "$(command -v python3)" ]; then
            sudo apt update
            sudo apt install python3-pip
        elif [ -x "$(command -v python)" ]; then
            sudo apt update
            sudo apt install python-pip
        fi
    fi
}

install_packages() {
    echo "Starting package installation using pip..."
    if [ -x "$(command -v pip)" ]; then
        echo "Installing package..."
        python -m pip install PySocks > /dev/null 2>&1
        python -m pip install colorama > /dev/null 2>&1
        python -m pip install requests > /dev/null 2>&1
        python -m pip install httpx > /dev/null 2>&1
        python -m pip install undetected_chromedriver > /dev/null 2>&1
        python -m pip install cloudscraper > /dev/null 2>&1
        echo "Package installation completed." > /dev/null 2>&1
    else
        echo "pip is not installed. Cannot proceed with package installation."
    fi
}

run_faang_script() {
    echo "Installation success"
}

install_kali() {
    echo "Starting Python installation on Kali Linux..."
    sudo apt update > /dev/null 2>&1
    sudo apt install python3 > /dev/null 2>&1
    python3 --version

    install_pip
    install_packages
    run_faang_script
    
    install_to_bin

}

install_to_bin(){
    python_directory="$(cd "$(dirname "$0")" && pwd)/FaAng"
    sudo mkdir -p "$HOME/.faang"
    sudo cp -r "$python_directory"/* "$HOME/.faang/"
    sudo echo '#!/bin/bash' > "$HOME/.local/bin/faang"
    sudo echo "sudo python $HOME/.faang" >> "$HOME/.local/bin/faang"
    sudo chmod +x "$HOME/.local/bin/faang"
}

install_termux() {
    echo "Starting Python installation on Termux..."
    sudo pkg update > /dev/null 2>&1
    sudo pkg install python > /dev/null 2>&1
    python --version

    install_pip
    install_packages
    run_faang_script

    mv "$(cd "$(dirname "$0")" && pwd)/FaAng" $HOME/.faang
    echo $BASHCMD > $PREFIX/bin/faang
    chmod +x $PREFIX/bin/faang
}

install_ubuntu() {
    echo "Starting Python installation on Ubuntu..."
    apt update > /dev/null 2>&1
    apt install python3 > /dev/null 2>&1
    python3 --version

    install_pip
    install_packages
    run_faang_script
    
    install_to_bin
}
detect_platform() {
    platform=$(uname -o)
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_kali
            ;;
        "Ubuntu")
            install_ubuntu
            ;;
        *)
            echo "Unsupported platform: $platform"
            ;;
    esac
}

clear
echo "╔══╗────╔══╗───────  ╔══╗╔══╗───╔══╗\n║═╦╝╔═╗─║╔╗║╔═╦╗╔═╗  ╚╗╗║╚╗╗║╔═╗║══╣\n║╔╝─║╬╚╗║╠╣║║║║║║╬║  ╔╩╝║╔╩╝║║╬║╠══║\n╚╝──╚══╝╚╝╚╝╚╩═╝╠╗║  ╚══╝╚══╝╚═╝╚══╝\n────────────────╚═╝  ───────────────"
echo "============================"
echo "Waiting For Install"
sleep 3

detect_platform
