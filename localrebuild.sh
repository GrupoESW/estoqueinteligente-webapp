branch=dev
repo=estoqueinteligente-webapp

 sed -i "s/FROM REPO:base/FROM ${repo}:base/g" Dockerfile
        docker build -t ${repo}:${branch} -f Dockerfile .
    
        if docker inspect "${repo}_${branch}_a" >/dev/null 2>&1; then
          docker run -d \
              --name ${repo}_${branch}_b \
              --network nginx-proxy \
              --restart always \
              -e "VIRTUAL_HOST=${branch}.${repo/*-/}.dispensainteligente.com.br" \
              ${repo}:${branch}
              #-e "LETSENCRYPT_HOST=${branch}.${repo/*-/}.dispensainteligente.com.br" \
          docker rm -f ${repo}_${branch}_a || true
        else
          docker run -d \
              --name ${repo}_${branch}_a \
              --network nginx-proxy \
              --restart always \
              -e "VIRTUAL_HOST=${branch}.${repo/*-/}.dispensainteligente.com.br" \
              ${repo}:${branch}
              #-e "LETSENCRYPT_HOST=${branch}.${repo/*-/}.dispensainteligente.com.br" \
          docker rm -f ${repo}_${branch}_b || true
        fi