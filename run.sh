#!/bin/bash

case "$1" in

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
    
    build_reporter)
        docker build -t kpop-reporter ./reporter
        ;;

    run_reporter)
        mkdir -p data
        docker run --rm -v "$(pwd)/data:/data" kpop-reporter
        ;;
    
    structure)
        find . -path ./.git -prune -o -print
        ;;
    clear_data)
        rm -f data/*.csv data/*.html
        ;;

    inside_generator)
        docker run --rm -v "$(pwd)/data:/data" kpop-generator ls -la /data
        ;;
    inside_reporter)
        docker run --rm -v "$(pwd)/data:/data" kpop-reporter ls -la /data
        ;;
    *)
        echo "Invalid command"
        ;;
esac