# E075PPF

## Descrição

Cadastros - Produtos - Ligação Produto/Derivação ao Fabricante

---

## Resumo

- Campos: 19
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc.) |
| CodFab | String(010) | Não | Código do Fabricante |
| CodFor | Number(009,0) | Não | Código do fornecedor |
| ProFab | String(021) | Não | Código do produto no Fabricante |
| DesPpf | String(250) | Não | Descrição do produto  no Fabricante |
| ObsPpf | String(240) | Sim | Observação |
| UniMed | String(003) | Sim | Código de Unidade de Medida do produto no Fabricante |
| CodClf | String(003) | Sim | Código interno da classificação fiscal do produto no Fabricante |
| CodBar | Number(013,0) | Sim | Código de barras EAN13 do Fabricante |
| PrzGfa | Number(004,0) | Sim | Prazo de garantia de fábrica dada pelo fabricante |
| PrzTfa | Number(004,0) | Sim | Prazo de garantia de fábrica dada pelo fabricante para troca |
| QtdMlt | Number(012,5) | Sim | Quantidade múltipla do produto no fabricante |
| CodMot | Number(006,0) | Sim | Código do motivo da situação da ligação Produto x Fabricante |
| ObsMot | String(250) | Sim | Observação do motivo da situação da ligação Produto x Fabricante |
| SitPpf | String(001) | Sim | Situação da ligação do Produto x Fabricante |
| DatTfa | Date | Sim | Data de término de fabricação do produto pelo fabricante |
| IndEsc | String(001) | Sim | Indicador de Produção em Escala Relevante |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodFab
- CodFor
- ProFab

---

## Índices

### E075PPFIndice1

**Tipo:** Não unico

Campos:
- CodFab

---

## Relacionamentos

### IR_E075PPF_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E075PPF_003

**Tabela:** E076FAB

| Origem | Destino |
|--------|---------|
| CodFab | CodFab |

