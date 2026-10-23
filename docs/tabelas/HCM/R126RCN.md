# R126RCN

## Descrição

Requisições - Requisitos Conhecimentos

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código da Requisição |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| PtsRcn | Number(002,0) | Sim | Pontuação do Conhecimento |

---

## Chave Primária

- CodRqu
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126RCN_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

### IR_R126RCN_002

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

