#!/bin/bash
install_pip() {
    echo "[*] Starting pip installation..."
    if [ -x "$(command -v pip)" ]; then
        echo "[*] pip is already installed."
    else
        echo "[*] Installing pip..."
        if [ -x "$(command -v python3)" ]; then
            sudo apt update -y > /dev/null 2>&1
            sudo apt install python3-pip -y > /dev/null 2>&1
        elif [ -x "$(command -v python)" ]; then
            sudo apt update -y > /dev/null 2>&1
            sudo apt install python-pip -y > /dev/null 2>&1
        fi
    fi
}

install_packages() {
    echo "[*] Starting package installation using pip..."
    if [ -x "$(command -v pip)" ]; then
        echo "[*] Installing package..."
        python -m pip install -r requirements.txt > /dev/null 2>&1
        echo "[*] Package installation completed."
    else
        echo "[*] pip is not installed. Cannot proceed with package installation."
    fi
}

run_faang_script() {
    echo "[*] Installation success"
}

install_kali() {
    echo "[*] Starting Python installation on Kali Linux..."
    sudo apt update -y > /dev/null 2>&1
    sudo apt install python3 -y
    python3 --version

    install_pip
    install_packages
    run_faang_script
    
    sh install_to_bin.sh
}

install_termux() {
    echo "[*] Starting Python installation on Termux..."
    pkg update -y > /dev/null 2>&1
    pkg install python -y
    python --version

    install_pip
    install_packages
    run_faang_script

    sh install_to_bin.sh
}

install_ubuntu() {
    echo "[*] Starting Python installation on Ubuntu..."
    sudo apt update -y > /dev/null 2>&1
    sudo apt install python3 -y
    python3 --version

    install_pip
    install_packages
    run_faang_script
    
    sh install_to_bin.sh
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
            echo "[*] Unsupported platform: $platform"
            ;;
    esac
}

detect_platform
