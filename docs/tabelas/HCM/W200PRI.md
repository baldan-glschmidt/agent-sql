# W200PRI

## Descrição

Tabela para manutenção do histórico de execução de processos

---

## Resumo

- Campos: 12
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
| PRCNAM | String(255) | Sim | Nome do processo de workflow |
| INIDAT | Date | Sim | Data de início da execução |
| INITIM | Number(005,0) | Sim | Tempo de início de execução do processo |
| USUINI | Number(010,0) | Sim | Usuário iniciador do processo |
| ENDDAT | Date | Sim | Data do fim de término da execução |
| ENDTIM | Number(005,0) | Sim | Tempo de término de execução do processo |
| STATUS | Number(005,0) | Sim | Status final da execução do processo |
| ENDMSG | String(2000) | Sim | Motivo do cancelamento |
| USUCAN | Number(010,0) | Sim | Usuário que cancelou o processo |

---

## Chave Primária

- PRCIID

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
