#!/bin/sh

ROOT_DIR=/usr/share/nginx/html

echo "Replacing env constants in JS"
for file in $ROOT_DIR/js/app.*.js* $ROOT_DIR/index.html ;
do
    echo "Before replacement:"
    grep -o "process.env.VUE_APP_DOMAIN" "$file"

    sed -i 's|process\.env\.VUE_APP_DOMAIN|'test\"${VUE_APP_DOMAIN}\"'|g' $file
    echo $VUE_APP_DOMAIN
    echo "After replacement:"
    grep -o "process.env.VUE_APP_DOMAIN" "$file"
done

exec nginx -g "daemon off;"