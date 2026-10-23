# R017PEP

## Descrição

Permissão Alternativa por Posto de Trabalho

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| CodPrm | Number(005,0) | Não | Código da Permissão Alternativa |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Permissão |
| ObsPrm | String(080) | Sim | Observação |

---

## Chave Primária

- EstPos
- PosTra
- CodPrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017PEP_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R017PEP_002

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

