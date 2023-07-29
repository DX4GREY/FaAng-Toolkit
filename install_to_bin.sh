detect_platform() {
    platform=$(uname -o)
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_linux
            ;;
        "Ubuntu")
            install_linux
            ;;
        *)
            echo "[*] Unsupported platform: $platform"
            ;;
    esac
}
install_linux(){
    sudo echo "sudo python $HOME/.faang/main.py \$1 \$2 \$3 \$4 \$5" > $HOME/.local/bin/faang
    sudo echo 'echo "[*] Uninstalling faang..." && sudo rm -rf $HOME/.faang && sudo rm -rf $HOME/.local/bin/faang && sudo rm -rf $HOME/.local/bin/faang-uninstaller && echo "[*] faang uninstall task done"' > $HOME/.local/bin/faang-uninstaller
    sudo cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.faang"
    sudo chmod +x $HOME/.local/bin/faang
    sudo chmod +x $HOME/.local/bin/faang-uninstaller
}
install_termux(){
    cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.faang"
    echo "python $HOME/.faang/main.py \$1 \$2 \$3 \$4 \$5" > $PREFIX/bin/faang
    echo 'echo "[*] Uninstalling faang..." && rm -rf $HOME/.faang && rm -rf $PREFIX/bin/faang && rm -rf $PREFIX/bin/faang-unisntaller && echo "[*] faang uninstall task done"' > $PREFIX/bin/faang-uninstaller
    chmod +x $PREFIX/bin/faang
    chmod +x $PREFIX/bin/faang-uninstaller
}
detect_platform