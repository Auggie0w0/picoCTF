#!/bin/bash

caesar_cipher() {
    echo "Enter the text to decrypt:"
    read text
    echo "Trying all 26 shifts..."
    echo "------------------------"
    for i in {0..25}; do
        shifted=$(echo "$text" | tr '[A-Za-z]' \
            $(printf '%c-%c' $(( 65 + i )) 90; printf '%c-%c' 65 $(( 64 + i )); \
             printf '%c-%c' $(( 97 + i )) 122; printf '%c-%c' 97 $(( 96 + i ))))
        echo "Shift $i: $shifted"
    done
}

base64_decoder() {
    echo "Enter Base64 string to decode:"
    read encoded
    decoded=$(echo "$encoded" | base64 -d)
    echo "Decoded string:"
    echo "$decoded"
    
    echo "Try multiple layers of decoding? (y/n)"
    read choice
    if [ "$choice" = "y" ]; then
        current="$encoded"
        counter=1
        while true; do
            if ! decoded=$(echo "$current" | base64 -d 2>/dev/null); then
                break
            fi
            echo "Layer $counter: $decoded"
            current="$decoded"
            ((counter++))
        done
    fi
}

while true; do
    clear
    echo "=== Decoder Menu ==="
    echo "1. Caesar Cipher"
    echo "2. Base64 Decoder"
    echo "3. Exit"
    echo "==================="
    echo "Choose an option (1-3):"
    read option

    case $option in
        1)
            caesar_cipher
            ;;
        2)
            base64_decoder
            ;;
        3)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid option"
            ;;
    esac
    
    echo
    echo "Press Enter to continue..."
    read
done