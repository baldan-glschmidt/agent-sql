# E720LOF

## Descrição

Ficha - Ligação Operações X Família Ferramentas

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOpr | String(006) | Não | Código da operação |
| CodFam | String(006) | Não | Código da família da ferramenta |
| CodFrt | String(014) | Não | Código da Ferramenta |
| DerFrt | String(007) | Não | Código da derivação da Ferramenta |
| ObsLof | String(240) | Sim | Observações |
| SitLof | String(001) | Não | Situação da Ligação |

---

## Chave Primária

- CodEmp
- CodOpr
- CodFam
- CodFrt
- DerFrt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E720LOF_001

**Tabela:** E720OPR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOpr | CodOpr |

### IR_E720LOF_002

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

