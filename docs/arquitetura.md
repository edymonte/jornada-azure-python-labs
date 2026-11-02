# Arquitetura ilustrada — nosso streaming fictício

## Desenho 1 — duas pessoas, múltiplas requisições

```mermaid
flowchart TB
 U1["👦 Usuário A — laptop"] --> LB["🌐 Balanceador Nginx"]
 U2["👧 Usuário B — celular"] --> LB
 subgraph APP["Aplicação do catálogo (Docker Compose — LAB 02)"]
  LB -->|requisição 1| A["📦 Contêiner api-a"]
  LB -->|requisição 2| B["📦 Contêiner api-b"]
 end
 A -.-> DB[("🗄️ Banco — módulo futuro")]
 B -.-> DB
 CDN["📺 Vídeo e imagens — CDN em serviço real"] -.-> U1
 CDN -.-> U2
```

As setas representam **pedidos individuais**. Não significam que o usuário A pertence ao contêiner A. Atualizar o navegador pode produzir respostas de instâncias diferentes. O Docker Compose é o orquestrador **destes laboratórios**, não AKS.

## Desenho 2 — como isso evoluiria para Kubernetes

```mermaid
flowchart TB
 U["Navegadores"] --> IN["Entrada HTTP / Ingress"]
 IN --> S["Service — distribuição para endpoints saudáveis"]
 subgraph AKS["Cluster AKS — ambiente futuro, não provisionado"]
  S --> P1["Pod catálogo-1 / contêiner Flask"]
  S --> P2["Pod catálogo-2 / contêiner Flask"]
  S --> P3["Pod catálogo-3 / contêiner Flask"]
 end
 P1 -.-> DB[("Banco de dados gerenciado")]
 P2 -.-> DB
 P3 -.-> DB
```

**Separar os conceitos:** Nginx no LAB 02 é um proxy/balanceador. Kubernetes Service pode distribuir tráfego para Pods, enquanto Ingress ou Gateway oferece entrada HTTP. O AKS administra a plataforma de Kubernetes; não garante por si só zero downtime, ausência de falhas ou custos baixos.

## Cinco perguntas para discutir olhando as figuras

1. O que muda se 10 usuários acessarem em vez de 2?
2. O que aconteceria se tivéssemos apenas uma instância?
3. Uma única pessoa pode ser atendida por Pods diferentes? **Sim, entre requisições.**
4. Qual problema o banco de dados resolve que uma réplica não resolve?
5. Qual parte desta figura enviaria os bytes de um filme longo? **Em uma plataforma de vídeo real, normalmente um caminho de entrega por CDN — não necessariamente os Pods da API.**