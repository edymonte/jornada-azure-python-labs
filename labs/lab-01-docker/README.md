# LAB 01 — Dois contêineres: o mesmo aplicativo, duas instâncias

**Objetivo:** compreender imagem, contêiner, réplica e mapeamento de portas; sem AKS e sem custos Azure.

## História

Uma loja de vídeos tem uma API simples que mostra o catálogo. Queremos rodar duas cópias do **mesmo código** para que mais de um processo possa atender solicitações.

## Antes de começar

Siga [a preparação do ambiente](../../docs/ambiente.md). Execute todos os comandos na **raiz do repositório**.

## Passo a passo

### 1. Construir a imagem

```bash
docker build -t jornada-catalogo:lab01 ./app
```

**O que aconteceu?** Docker leu a receita em `app/Dockerfile`, instalou dependências e produziu uma **imagem**.

### 2. Criar a primeira instância

```bash
docker run -d --name catalogo-a -e INSTANCE_NAME=Pedro -p 8081:5000 jornada-catalogo:lab01
```

Abra **http://localhost:8081**. A página mostra o nome da instância que atendeu.

### 3. Criar a segunda instância

```bash
docker run -d --name catalogo-b -e INSTANCE_NAME=Ryan -p 8082:5000 jornada-catalogo:lab01
docker ps
```

Abra **http://localhost:8082**. Compare o campo **Servidor** das páginas.

### 4. Simular falha

```bash
docker stop catalogo-a
docker ps
```

A porta 8081 para de responder, mas **8082 continua**. Atenção: aqui **ainda não existe balanceador** nem recuperação automática.

### 5. Reiniciar

```bash
docker start catalogo-a
```

### 6. Limpar

```bash
docker rm -f catalogo-a catalogo-b
```

## Pense e explique

- O que é a **imagem**? O que é o **contêiner**?
- Por que usamos portas diferentes?
- As duas páginas vieram de uma única máquina virtual? Um contêiner é uma máquina virtual? Explique.
- O que aprendemos ao parar `catalogo-a`?

## Evidências

Registrar no portal: captura ou saída de `docker ps`, comparação das duas páginas, descrição do que aconteceu ao parar uma instância e explicação em palavras próprias.

**Exemplo de uso real:** APIs de lojas podem executar cópias independentes para lidar com demanda, mas precisam de uma camada de balanceamento para distribuir tráfego.