uninstall(){
    echo "Uninstalling FaAng..."
    sudo rm -rf "$HOME/.local/bin/faang"
    sudo rm -rf "$HOME/.faang/"
    echo "FaAng uninstall task done"
}
case $# in
    1)
        if [ $1 == "--uninstall" ]; then
            uninstall
        fi
        ;;
    *)
        python $HOME/.faang
        ;;
esac
