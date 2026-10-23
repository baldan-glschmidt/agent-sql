# USU_TCadSGI_D

## Descrição

Posto de Trabalho x Conhecimento - Detalhe

---

## Resumo

- Campos: 5
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_EstPos | Number(003,0) | Sim | Estrutura de Posto |
| USU_PosTra | String(024) | Sim | Posto de Trabalho |
| USU_DatIni | Date | Sim | Data de Início |
| USU_FamCnc | String(004) | Sim | Família de Conhecimento |
| USU_CodCnc | String(005) | Sim | Conhecimento |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### USU_IRUSU_TCad000

**Tabela:** USU_TCadSGI_C

| Origem | Destino |
|--------|---------|
| USU_EstPos | USU_EstPos |
| USU_PosTra | USU_PosTra |
| USU_DatIni | USU_DatIni |

