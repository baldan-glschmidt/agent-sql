# W000PRI

## Descrição

Tabela para manutenção de instâncias de processos em execução

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| PROCID | Number(005,0) | Sim | Identificador do processo de workflow |
| PRCVER | Number(005,0) | Sim | Versão do processo |
| PRSTAT | Number(005,0) | Sim | Status da execução do processo |
| UPDDAT | Date | Sim | Data da última alteração na execução do processo |
| UPDTIM | Number(005,0) | Sim | Tempo da última alteração no processo |
| INITDT | Image | Sim | Dados iniciais do processo |
| INIUSU | Number(010,0) | Sim | Código do usuário que iniciou o processo |
| LSTCTX | Image | Sim | Dados da execução do processo |
| PRIKEY | String(030) | Sim |  |

---

## Chave Primária

- PRCIID

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
