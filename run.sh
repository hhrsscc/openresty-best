PATH=/usr/local/openresty/nginx/sbin:$PATH
export PATH
nginx -p `pwd`/ -c $1
