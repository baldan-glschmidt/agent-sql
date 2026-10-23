# W000DPR

## Descrição

Tabela para manutenção de processos publicados de workflow

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PROCID | Number(005,0) | Não | Identificador único do processo de workflow |
| PRCVER | Number(005,0) | Não | Versão do processo |
| PRCNAM | String(255) | Sim | Nome do processo de workflow |
| PUBDAT | Date | Sim | Data e hora da publicação do processo |
| PUBTIM | Number(005,0) | Sim | Tempo da publicação do processo |
| PUBUSU | Number(010,0) | Sim | Usuário que publicou o processo |
| PRCDAT | Image | Sim | Dados para execução do processo |
| PRCIMG | Image | Sim | Ícone do processo |
| PRCMET | Image | Sim | Metadados do processo |
| PRCSIG | Image | Sim | Assinatura do processo |

---

## Chave Primária

- PROCID
- PRCVER

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
