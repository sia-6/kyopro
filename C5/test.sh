#!/bin/zsh

if [[ $1 -eq 26 ]]; then
    (cat <<EOF
4
17
31
35
49
EOF
) | python3 ./A26.py
fi

if [[ $1 -eq 27 ]]; then
    (cat <<EOF
700 900
EOF
) | python3 ./A27.py
    (cat <<EOF
117 432
EOF
) | python3 ./A27.py
    (cat <<EOF
998244353 1000000000
EOF
) | python3 ./A27.py
fi

if [[ $1 -eq 28 ]]; then
    (cat <<EOF
4
+ 57
+ 43
* 100
- 1
EOF
) | python3 ./A28.py
fi

if [[ $1 -eq 29 ]]; then
    (cat <<EOF
2 8
EOF
) | python3 ./A29.py
    (cat <<EOF
7 3
EOF
) | python3 ./A29.py
    (cat <<EOF
2 42
EOF
) | python3 ./A29.py
fi
