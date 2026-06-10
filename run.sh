#!/bin/bash

case $1 in

    build_generator)
        docker build -t kpop-generator ./generator
        ;;
    
    run_generator)
        docker run --rm -v "$(pwd)/data:/data" kpop-generator
        ;;
    create_local_data)
        mkdir -p local_data
        python generator/generator.py local_data
        ;;
    
    *)
        echo "Invalid command"
        ;;
esac