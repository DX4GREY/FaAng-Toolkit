#!/bin/bash
install_pip() {
    echo "Starting pip installation..."
    if [ -x "$(command -v pip)" ]; then
        echo "pip is already installed."
    else
        echo "Installing pip..."
        if [ -x "$(command -v python3)" ]; then
            sudo apt update > /dev/null 2>&1
            sudo apt install python3-pip > /dev/null 2>&1
        elif [ -x "$(command -v python)" ]; then
            sudo apt update > /dev/null 2>&1
            sudo apt install python-pip > /dev/null 2>&1
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
        echo "Package installation completed."
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
    sudo cp -r "$(cd "$(dirname "$0")" && pwd)/bin/linux.sh" "$HOME/.local/bin/faang"
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

    cp -r "$(cd "$(dirname "$0")" && pwd)/FaAng" $HOME/.faang
    cp -r "$(cd "$(dirname "$0")" && pwd)/bin/termux.sh" $PREFIX/bin/faang
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

