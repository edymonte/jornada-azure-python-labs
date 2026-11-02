# Preparação e solução de problemas

## Antes do encontro

1. Instale Docker Desktop (Windows/macOS) ou Docker Engine e o plugin Compose v2 (Linux).
2. Execute `docker version` e `docker compose version` no terminal.
3. Faça clone do projeto e entre na pasta.
4. Confirme que a porta **8080** não está ocupada.
5. Execute `docker compose up --build -d` e abra http://localhost:8080.

### Codespaces

Se preferir Codespaces, use um Codespace padrão e verifique **primeiro** se `docker version` e `docker compose version` funcionam. Abra a aba **Ports** e encaminhe a porta 8080. As condições e limites dependem do tipo de conta e do Codespace; não assumir gratuidades ou disponibilidade ilimitada.

### Erros comuns

- **Cannot connect to Docker daemon:** iniciar o Docker Desktop/daemon.
- **Port 8080 already allocated:** fechar o programa em 8080 ou alterar `8080:80` para `8088:80` em `compose.yaml`; abrir 8088.
- **Página não abre:** execute `docker compose ps` e `docker compose logs --tail=80`.
- **Imagem antiga:** `docker compose up --build -d`.
- **Permissão Docker no Linux:** revisar acesso ao daemon; evite comandos de permissão que não entende.

### Segurança

Este é um servidor didático, sem autenticação real e sem informações pessoais. Não publique a porta na internet como serviço de produção. O Docker pode consumir recursos locais; encerre com `docker compose down`.