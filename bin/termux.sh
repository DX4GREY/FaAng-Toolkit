uninstall(){
    echo "Uninstalling FaAng..."
    rm -rf $HOME/.faang
    rm -rf $PREFIX/bin/faang
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
