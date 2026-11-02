# Roteiro de mentoria — aproximadamente 60 minutos

## 0–10 min — O problema que uma empresa tenta resolver

Peça aos alunos que imaginem duas pessoas abrindo ao mesmo tempo um catálogo de streaming. Pergunte: **de onde vêm os filmes listados? E se a aplicação que responde falhar?** Os vídeos reais podem chegar via CDN, mas a experiência também depende de serviços para catálogo, login, recomendações e históricos.

**Não começar pelos comandos.** Primeiro pedir que expliquem o que acham que acontece nos bastidores.

## 10–20 min — Arquitetura

Abra [o desenho da arquitetura](arquitetura.md) e percorra as setas: navegador → balanceador → réplicas da API. Depois discuta por que dados persistentes exigem banco separado.

Explique:
- **Imagem Docker:** receita imutável do aplicativo.
- **Contêiner:** processo isolado criado a partir da imagem.
- **VM:** máquina virtual com sistema operacional próprio, executada por um hipervisor.
- **Pod:** unidade básica de execução do Kubernetes, que pode conter um ou mais contêineres.
- **AKS:** serviço gerenciado de Kubernetes do Azure — **não é usado nos dois primeiros LABs**.

## 20–35 min — LAB 01

Abrir [LAB 01](../labs/lab-01-docker/README.md): iniciar duas cópias da API e comparar suas respostas. Cada aluno aponta qual serviço respondeu.

## 35–45 min — LAB 02

Abrir [LAB 02](../labs/lab-02-balanceamento/README.md): demonstrar que o Nginx distribui pedidos e observar o que ocorre ao interromper uma réplica. Não prometer disponibilidade absoluta: a configuração e a saúde das réplicas importam.

## 45–55 min — Perguntas individuais

**Pedro Henrique (compute):**
1. Qual a diferença entre uma imagem e um contêiner?
2. Por que duas cópias do mesmo aplicativo podem funcionar ao mesmo tempo?
3. Contêiner é uma VM mais rápida? Explique por que não.

**Ryan Felipe (dados):**
1. Qual informação do catálogo precisaria ser guardada depois que um contêiner fosse removido?
2. O histórico do usuário deve ficar apenas na memória do contêiner? Por quê?
3. Para guardar usuários e pedidos, quando um banco relacional faria sentido?

## 55–60 min — Registro no portal

Cada aluno registra: **o que executou**, **o que observou**, **por que existe essa solução**, **uma dúvida real**, **autoavaliação de 1 a 5**.

**Critério:** `LIBERAR PRÓXIMA AULA` apenas quando nota 4–5 **e** explicação escrita convincente; caso contrário, `REVISAR ANTES DE AVANÇAR`. Até lá, manter a atividade central AZ-900 sem avanço formal.

## Exemplos para conectar com a vida real

- **Loja virtual:** réplicas da API de produtos ajudam a atender picos de Black Friday.
- **Banco:** serviços de consulta podem escalar independentemente do banco de dados.
- **Jogos:** APIs de perfil podem ter múltiplas réplicas, mas partidas com estado precisam de arquitetura específica.
- **Streaming:** catálogo e autenticação podem ser escalados; a entrega do vídeo em si geralmente envolve CDN, armazenamento e protocolos específicos.