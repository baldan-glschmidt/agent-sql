# E075LMF

## Descrição

Cadastros - Ligação Minifábricas X Família/Produtos

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFam | String(006) | Não | Código da família de produto |
| CodPro | String(014) | Não | Código do produto |
| CodMnf | String(010) | Não | Código da Minifábrica |
| LimMnf | Number(014,5) | Sim | Limitador de Capacidade da Minifábrica |
| SitLmf | String(001) | Não | Situação da Ligação da Minifábrica |

---

## Chave Primária

- CodEmp
- CodFam
- CodPro
- CodMnf

---

## Índices

### E075LMFIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodMnf

---

## Relacionamentos

### IR_E075LMF_001

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E075LMF_003

**Tabela:** E012MNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMnf | CodMnf |

