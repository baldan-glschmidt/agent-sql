# R017BPT

## Descrição

Postos de Trabalho - Benefícios

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do posto de trabalho |
| CmpIni | Date | Não | Competência de início do pacote de benefícios |
| CodPac | Number(004,0) | Não | Código do Pacote de Benefícios |
| CmpTer | Date | Sim | Competência de término do pacote de benefícios |
| PosFil | Number(001,0) | Sim | Informar se os benefícios também estarão disponíveis para os postos filhos |

---

## Chave Primária

- EstPos
- PosTra
- CmpIni
- CodPac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017BPT_003

**Tabela:** R167CPB

| Origem | Destino |
|--------|---------|
| CodPac | CodPac |

